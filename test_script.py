"""Unit tests for the module."""

from pathlib import Path
import pytest
from chol_dictionary import *


def test_chol_conversion():
    cases = get_chol_test_cases()
    converter = CholConverter(rules='conversion_rules.txt')
    for original, converted in cases.items():
        assert converter.convert(original) == converted


def get_chol_test_cases():
    """Parse the file test_cases.txt for unit tests of converting Ch'ol into
    the new ortography.
    """
    cases_file = Path('test_cases.txt')
    cases = dict()
    reading = []
    with open(cases_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            if len(reading) < 2 and line.strip() != '': # reading test case
                reading.append(line.strip())
            elif len(reading) == 2: # record test case
                cases[reading[0]] = reading[1]
                reading = []
    return cases


def test_full_conversion():
    case = "\\oi t'an\n"
    converter = SourceConverter(rules='conversion_rules.txt')
    result = converter._convert_line(case)
    assert result == "\\oi ty'añ"
    result = converter._convert_line(case, latex=True)
    assert result[0] == '\\'
    assert result[-1] == '}'


def test_realphabetize(tmpdir):
    test_case = r"""\_sh something

\lx B
\alf B

\lx bbäk
\cg s
\tl carbón
\dt 22/May/2007

\lx A
\alf A

\lx abälel
\nd Sab.
\cg s
\tl noche
\re ak'älel
\dt 22/May/2007
    """
    source = tmpdir.join("test_source.txt")
    source.write(test_case)
    converter = SourceConverter(rules='conversion_rules.txt')
    target = tmpdir.join("target.txt")
    target_alf = tmpdir.join("target_alf.txt")
    converter.realphabetize(source, target)
    result = target.read()
    expected = r"""\_sh something

\lx A
\alf A

\lx abälel
\nd Sab.
\cg s
\tl noche
\re ak'älel
\dt 22/May/2007

\lx B
\alf B

\lx bbäk
\cg s
\tl carbón
\dt 22/May/2007

"""
    assert result == expected
