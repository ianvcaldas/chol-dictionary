"""Module to convert the Ch'ol dictionary from old ortography to new
ortography, as well as to format the whole thing in LaTeX.
"""

import sys
from pathlib import Path
from collections import OrderedDict as odict


class CholConverter():
    """Singleton class for converting Ch'ol expressions into new ortography."""


    def __init__(self, rules):
        self.rules, self.exceptions = self._parse_rules(rules)


    def _parse_rules(self, filepath):
        """Parse a file with conversion rules.

        Args:
            filepath: Path to file containing rules.

        Returns:
            An ordered dictionary where keys are the original elements and
            values are what the elements are supposed to be converted into.
        """
        rules = odict()
        exceptions = []
        with open(Path(filepath), 'r') as f:
            for line in f:
                if line.startswith('#') or line.strip() == '':
                    continue
                if line.startswith('='):
                    exceptions.append(line.split()[1])
                    continue
                old, new = [s.strip().replace('_', ' ') for s in line.split(' -> ')]
                rules[old] = new
        return rules, exceptions 


    def convert(self, expression, capitalize=False):
        """Convert expression from old Ch'ol ortography into new.

        Args:
            expression: Text to be converted.
            capitalize: Whether to capitalize the first word of the converted text.

        Returns:
            The text in new ortography.
        """
        if expression[0].isupper():
            capitalize = True
        result = ' ' + expression.lower()
        for ix, exc in enumerate(self.exceptions):
            result = result.replace(exc, f'TMP{ix}')
        for source, modified in self.rules.items():
            result = result.replace(source, modified)
        for ix, exc in enumerate(self.exceptions):
            result = result.replace(f'TMP{ix}', exc)
        result = result.strip()
        if capitalize:
            result = result.capitalize()
        return result



class SourceConverter():
    """Converts the source for the Ch'ol dictionary into new source.

    Args:
        latex: Whether the output should be in LaTeX format.
        rules: File where the conversion rules are kept.
        latex_header: File where the LaTeX header is written, only if output in
        LaTeX.
    """

    def __init__(self, latex=False,
                 rules='conversion_rules.txt',
                 latex_header='latex_header.tex'):
        self.chol = CholConverter(rules=rules)
        self.latex = latex
        if latex:
            self.latex_header = self._get_latex_header(latex_header)
            self.latex_closing = self._get_latex_closing()


    def _get_latex_header(self, headerfile):
        """Parse the file containing the LaTeX header."""
        with open(Path(headerfile), 'r') as f:
            header = ''.join([line for line in f])
        return header


    def _get_latex_closing(self):
        s = "\\end{multicols*}\n\\end{document}"
        return s


    def convert_source(self, source, output=None):
        """Convert a source file into the new ortography.

        Args:
            source: Path to the source file.
            output: Path to the output file. If None, write to stdout.

        Returns:
            Nothing.
        """
        if output is None:
            out = sys.stdout
        else:
            out = open(Path(output), 'w')
        if self.latex:
            out.write(self.latex_header + '\n')
        with open(Path(source), 'r') as f:
            for ix, line in enumerate(f):
                if line.strip() == '':
                    out.write(line)
                    continue
                new_line = self._convert_line(line)
                if new_line is not None:
                    out.write(new_line + '\n')
        if self.latex:
            out.write(self.latex_closing)
        out.close()

    def _convert_line(self, line):
        """Parse and convert a single line in the dictionary source.

        Args:
            line: The raw string representing the source line.
        Returns:
            The converted line, including converting to LaTeX if wanted.
        """
        # Codes to ignore when converting to LaTeX
        skip_codes = ['\\_sh',
                      '\\_DateStampHasFourDigitYear',
                      '\\dt',
                      '\\dib',
                      '\\pie',
                      '\\nt',
                     ]
        elements = line.split()
        code = elements[0]
        content = ' '.join(elements[1:])
        if content == '': # happens sometimes
            return None
        # Replace unicode characters with common ones
        content = content.replace('ꞌ', "'") 
        if self._is_chol(code):
            content = self.chol.convert(content)
        if self.latex:
            if code in skip_codes:
                return None
            new_line = self._to_latex(code, content)
        else:
            new_line = ' '.join([code, content])
        return new_line


    def _is_chol(self, code):
        """Determine whether the current dictionary line is written in Ch'ol.

        Args:
            code: The annotation for the line.
            
        Returns:
            True if the code corresponds to a Ch'ol line, False otherwise.
        """
        return code in ['\\lx', '\\oi', '\\re', '\\su', '\\vdl',
                        '\\vp', '\\fbl', '\\alf']

    
    def _to_latex(self, code, content):
        """Convert source dictionary line to a LaTeX line.

        Args:
            code: Annotation for the line from the original source.
            content: The line itself.

        Returns:
            The LaTeX-formatted line.
        """
        commands = {
            'lx': 'entry',
            'mt': 'maintitle',
            'alf': 'alphaletter',
            'ac': 'onedefinition',
            'hm': 'defsuperscript',
            'dd': 'nontranslationdef',
            'cg': 'partofspeech',
            'tl': 'spanishtranslation',
            'ca': 'clarification',
            'oi': 'cholexample',
            'to': 'exampletranslation',
            'vdn': 'dialectvariant',
            'vdl': 'dialectword',
            're': 'alsosee',
            'nd': 'relevantdialect',
            'cu': 'culturalinformation',
            'su': 'secondaryentry',
            'cs': 'secondpartofspeech',
            'ts': 'secondtranslation',
            'vp': 'variation',
            'fgn': 'conjugationtense',
            'fbl': 'conjugationverb',
            'fgl': 'otherconjugation',
        }
        two_letter_code = code.replace('\\', '')
        # This skips the lexical entry for alphabet letters
        if two_letter_code == 'lx' and content.isupper():
            return None
        latex_command = commands[two_letter_code]
        content = content.replace('_', ' ')
        content = content.replace('²', '\\textsuperscript{2}')
        content = content.replace('³', '\\textsuperscript{3}')
        new_line = f'\\{latex_command}{{{content}}}'
        return new_line


if __name__ == '__main__':
    conv = SourceConverter(latex=True)
    conv.convert_source('original_source/chol_to_sp.txt',
                        'new_source/latex_chol_to_sp.tex')
