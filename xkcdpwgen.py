#!/usr/bin/env python
# coding: utf-8

# In[33]:


import argparse
import random
from random import randrange

parser = argparse.ArgumentParser(prog = 'xkcdpwgen', description='xx')

parser.add_argument('-w', '--words', type=int, default=4, help='xx')
parser.add_argument('-c', '--caps', type=int, default=0, help='xx')
parser.add_argument('-n', '--numbers', type=int, default=0, help='xx')
parser.add_argument('-s', '--symbols', type=int, default=0, help='xx')

args = parser.parse_args()

def randomWord():
    lines = open('words.txt').read().splitlines()
    return random.choice(lines)

def insertRandom(str, inserted):
    randomIndex = random.randint(0, len(str))
    return str[0:randomIndex] + inserted + str[randomIndex:]

words = []
for i in range(0, args.words):
    if (args.caps > 0):
        words.append(randomWord().capitalize())
        args.caps -= 1
    else:
        words.append(randomWord())
        
for i in range(0, args.numbers):
    n = random.choice(["0","1","2","3","4","5","6","7","8","9"])
    if (args.numbers > 0):
        words.insert(randrange(len(words)+1), n)
        args.numbers -= 1

password = ""
for x in words:
    password += x

while args.symbols > 0:
    s = random.choice(["~","!","@","#","$","%","^","&","*",".",":",";"])
    password = insertRandom(password, s)
    args.symbols -= 1

print(password)


# In[ ]:




