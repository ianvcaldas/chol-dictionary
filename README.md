
Ch'ol Dictionary
================

This is a script to update the the ortography of the existing Ch'ol dictionary
into the modern ortography. The script works in 3 steps: first, the ortography
is updated in a MDF source file. Second, the entries are reordered to restore
alphabetical ordering. Third, the MDF source is converted into LaTeX for
printing.


## Running the script

Make sure you have [Python 3](https://www.python.org) installed. The script was
developed under Python 3.7 and that version is recommended for full
functionality. To check your version of Python, run `python3 --version`.

To run the script, clone or download the repository and run the main script
with Python 3 from within it:

    git clone https://github.com/ianvcaldas/chol-dictionary.git
    cd chol-dictionary
    python3 make_dictionary.py

### Running the tests

In case you want to run the test cases, to make sure all ortography conversions
are working as intended, make sure you have
[pytest](https://docs.pytest.org/en/latest/) installed and run it from within
the script repository:

    cd chol-dictionary
    pytest

Custom cases to test ortography conversions can be added by the user by editing
the file `test_cases.txt`.


## Ortography update

Ortography update is done by a series of regular expression string
replacements. All replacements are done according to the file
`conversion_rules.txt`.

The script loops through the entire dictionary source file in MDF format, and
if the current line represents a field in Ch'ol, the ortography for the entry
is updated. If it represents any other kind of field, the ortography is left
alone. The output of the ortography update is another file in MDF format.


## Realphabetization

After we've produced a new file in MDF format, the order of entries might not
be alphabetical anymore due to the ortography changes. To correct this, we do
this "realphabetization". This part of the script reorders entries based on
standard alphabetical order and prints a new source in MDF format.

### Known bugs with realphabetization

Some words have multiple numbered entries indexed by the MDF field `\hm`. After
realphabetization, these entries might stop being in the right order. We
believe only the following entries, in the Ch'ol to Spanish dictionary, are
affected: joch', ñak, wersa, \*wuty, and yolokña.


## Conversion to LaTeX

The last part of the script converts the source into LaTeX for ease of
compilation and typesetting. The file `latex_header.tex` includes all the
formatting and typesetting code and is automatically added to the dictionary
when the script `make_dictionary.py` is run. In order to change the LaTeX
formatting, one would need to change `latex_header.py`, then re-run
`make_dictionary.py` to generate a new `.tex` file, then compile that file
using any LaTeX compiler.


## License

[Diccionario chꞌol de Tumbalá, Chiapas, con variaciones dialectales de Tila y
Sabanilla](https://www.sil.org/resources/archives/35328) is licensed under [CC
BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) and
attributed to the original authors and speakers. The dictionary with updated
ortography is a derivative work of the above and likewise under CC BY-NC-SA
4.0.
