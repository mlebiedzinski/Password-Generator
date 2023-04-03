# Password-Generator

CY2550 Foundations of Cybersecurity <br>
Project 3 <br> 
Feburary 28th, 2023 <br> 
( Python ) <br> 

This program generates passwords using the XKCD method. It excepts a variety of optional arguments in order to vary the password: <br> 
-h, --help  |                   show this help message and exit <br> 
-w WORDS, --words WORDS  |       include WORDS words in the password (default=4) <br> 
-c CAPS, --caps CAPS  |          capitalize the first letter of CAPS random words (default=0) <br> 
-n NUMBERS, --numbers NUMBERS |  insert NUMBERS random numbers in the password (default=0) <br> 
-s SYMBOLS, --symbols SYMBOLS |  insert SYMBOLS random symbols in the password (default=0) <br> 
<br> 
an example input would be... <br> 
<br> 
python xkcdpwgen.py -w 2 -c 2 -n 3 -s 1 <br> 
This would return a password consisting of 2 random words with 2 capital letters, 3 numbers, and 1 symbol!
