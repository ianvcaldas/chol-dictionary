
Ch'ol Dictionary
================

The goal of this project is to update the the ortography of the existing Ch'ol
dictionary into the modern ortrography. The previous source is in folder
`original_source`, while our converted source is in folder `new_source`. 


## TODO
* Check the Spanish-to-Ch'ol source to see if there's anything different there.
* Add command-line arguments to the main script.
* Write the LaTeX header with minimal formatting.
* Think about more elaborate formatting, e.g. for printing.


## Rules for ortography update

We use simple replacement rules that are codified in the file
`conversion_rules.txt`.


## Test cases

Of course, we want to double check whether our updates actually work. The file
`test_cases.txt` contains a series of manually curated checks. Before updating,
we make sure every single test in that file passes successfully.
