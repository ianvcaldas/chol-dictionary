
Ch'ol Dictionary
================

The goal of this project is to update the the ortography of the existing Ch'ol
dictionary into the modern ortrography.

The script works in 3 steps: first, the ortography is updated. Second,
realphabetization. Third, conversion to LaTeX.

Caveats:
* realphabetize and add_alpha are written specificall for this dictionary
  structure and don't necessarily generalize


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

We use simple replacement rules that are codified in the file
`conversion_rules.txt`.


## Realphabetization

* Realphabetization bugs:
    * Entries (1) and (2) out of order: joch', ñak, wersa, \*wuty, yolokña


## Conversion to LaTeX

The source is converted into LaTeX for ease of compilation and typesetting. The
file `latex_header.tex` includes all the formatting and typesetting code and is
automatically added to the dictionary when the script `make_dictionary.py` is
run. In order to change the LaTeX formatting, one would need to change
`latex_header.py`, then re-run `make_dictionary.py` to generate a new `.tex`
file, then compile that file using any LaTeX compiler.


## License

[Diccionario chꞌol de Tumbalá, Chiapas, con variaciones dialectales de Tila y
Sabanilla](https://www.sil.org/resources/archives/35328) is licensed under [CC
BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) and
attributed to the original authors and speakers. The dictionary with updated
ortography is a derivative work of the above and likewise under CC BY-NC-SA
4.0.
