
Ch'ol Dictionary
================

The goal of this project is to update the the ortography of the existing Ch'ol
dictionary into the modern ortrography. The previous source is in folder
`original_source`, while our converted source is in folder `new_source`. 


## TODO
* Add command-line arguments to the main script.
* Add regular expression support.
* Realphabetize.
    * Write whole-document realphabetizer (WDR) that keeps entries as
attributes.
    * Write AlphaLetter class that implements sorting and merging.
    * Modify WDR to generate and keep AlphaLetter objects.
    * Modify WDR to sort and merge AlphaLetters as needed.
    * Implement printint out WDR to file.


## Rules for ortography update

We use simple replacement rules that are codified in the file
`conversion_rules.txt`.


## Test cases

Of course, we want to double check whether our updates actually work. The file
`test_cases.txt` contains a series of manually curated checks. Before updating,
we make sure every single test in that file passes successfully.


## License

[Diccionario chꞌol de Tumbalá, Chiapas, con variaciones dialectales de Tila y
Sabanilla](https://www.sil.org/resources/archives/35328) is licensed under [CC
BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) and
attributed to the original authors and speakers. The dictionary with updated
ortography is a derivative work of the above and likewise under CC BY-NC-SA
4.0.
