# Password-Generator

( Python )

This program generates passwords using the XKCD method. It excepts a variety of optional arguments in order to vary the password: \\
-h, --help                      show this help message and exit \\
-w WORDS, --words WORDS         include WORDS words in the password (default=4)
-c CAPS, --caps CAPS            capitalize the first letter of CAPS random words (default=0)
-n NUMBERS, --numbers NUMBERS   insert NUMBERS random numbers in the password (default=0)
-s SYMBOLS, --symbols SYMBOLS   insert SYMBOLS random symbols in the password (default=0)

an example input would be...

./xkcdpwgen -w 2 -c 2 -n 3 -s 1
This would return a password consisting of 2 random words with 2 capital letters, 3 numbers, and 1 symbol!
