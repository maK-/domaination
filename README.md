# domaination
This is a very simple cli tool for doing various things with subdomain lists
>I just threw a few various shell scripts I had into the one tool

#What do I use it for?

> This takes a list of subdomains and splits them, then counts the most
> frequently occuring, could be interesting to brute **\*.whatever.domain**
> This just prints the output of ones that occur more than once
> (You can add the **-1** flag to view just the ones that occur once.)

`./domaination.py -l [sublist] -g`

> This takes that list and a list of already found subdomains and a list of
> individual words/subdomains and generates a list to then be resolved.

`./domaination.py -l [sublist] -g -s [wordlist]`

> This prints out a list of any domains containing a wildcard asterix \*

`./domaination.py -l [sublist] -w`

> This takes a list of subdomains and a list of words, then generates lists,
> replacing the \* in any domains with the word. (Useful for wildcard certs)

`./domaination.py -l [sublist] -w -s [wordlist]`

> This generates a list of sorted unique words found within a list of 
> already found subdomains, think the output of sublister for example.

`./domaination.py -l [sublist] -gs`

> This simply generates a list of http/https urls from a list of subdomains

`./domaination.py -l [sublist] -gu`


# Help output

> usage: domaination.py [-h] [-s SUBS] [-l LISTS] [-g] [-1] [-w] [-gs] [-gu]

> optional arguments:

>  -h, --help            show this help message and exit

>  -s SUBS, --subs SUBS  A list of subdomains

>  -l LISTS, --lists LISTS A list of already scraped subdomains

>  -g, --gen             Generate the lists

>  -1, --genone          Display only single entries from list

>  -w, --wildcard        Generate a list from only wildcard cert domains

>  -gs, --getsubs        Get a list of unique subdomains from list

>  -gu, --geturls        Generate a list of urls from subdomains


