#!/usr/bin/env python
# Challenge generator for BtS 2020. 
# You can test result here: https://fatiherikli.github.io/brainfuck-visualizer/#KysrKysgKysrKysgICAgICAgICAgICAgaW5pdGlhbGl6ZSBjb3VudGVyIChjZWxsICMwKSB0byAxMApbICAgICAgICAgICAgICAgICAgICAgICB1c2UgbG9vcCB0byBzZXQgNjAvOTAvNTAvMTIwCiAgICAgPiArKysrKyArICAgICAgICAgICAgICAgYWRkICA2IHRvIGNlbGwgIzEKICAgICA+ICsrKysrICsrKysgICAgICAgICAgICBhZGQgIDkgdG8gY2VsbCAjMgogICAgID4gKysrKysgICAgICAgICAgICAgICAgIGFkZCAgNSB0byBjZWxsICMzCiAgICAgPiArKysrKyArKysrKyArKyAgICAgICAgYWRkICAxMiB0byBjZWxsICM0Cjw8PDwgLSAgICAgICAgICAgICAgICAgIGRlY3JlbWVudCBjb3VudGVyIChjZWxsICMwKQpdCgo=
# Author: Arqsz

# Memory: [loop, upper letters, lower letters, numbers, special]

# ---------------------------------
# FILL MEMEORY
# +++++ +++++             initialize counter (cell #0) to 10
# [                       use loop to set 60/90/50/120
#     > +++++ +               add  6 to cell #1
#     > +++++ ++++            add  9 to cell #2
#     > +++++                 add  5 to cell #3
#     > +++++ +++++ ++        add  12 to cell #4
# <<<< -                  decrement counter (cell #0)
# ]

import unicodedata as u

try:
    with open('flag.txt', 'r') as r:
        flag = r.read().strip()
except FileNotFoundError:
    flag = "temp{temp_flag}"
hacker_name = 'Hacker4dAm'
file_name = 'email.txt'

class MEMORY_CELLS:
    UPPER_LETTERS = 1
    LOWER_LETTERS = 2
    NUMBERS = 3
    SPECIALS = 4

def encrypt(text):
    memory = [0, 60, 90, 50, 120]
    prev_cell = 0
    result = ''
    for sign in text:
        if u.category(sign) == 'Ll': # Small letters
            diff = MEMORY_CELLS.LOWER_LETTERS - prev_cell # Difference between current cell and previous cell 
            if diff < 0:
                result += '<' * abs(diff)
            else:
                result += '>' * diff
            diff = ord(sign) - memory[MEMORY_CELLS.LOWER_LETTERS] # Difference between memory value and ord of sign
            if diff < 0:
                result += '-' * abs(diff)
            else:
                result += '+' * diff
            memory[MEMORY_CELLS.LOWER_LETTERS] = ord(sign)
            prev_cell = MEMORY_CELLS.LOWER_LETTERS # Set previous memory cell to current
            result += '.' # Print sign from memory
        elif u.category(sign) == 'Lu': # Uppercase letters
            diff = MEMORY_CELLS.UPPER_LETTERS - prev_cell # Difference between current cell and previous cell 
            if diff < 0:
                result += '<' * abs(diff)
            else:
                result += '>' * diff
            diff = ord(sign) - memory[MEMORY_CELLS.UPPER_LETTERS] # Difference between memory value and ord of sign
            if diff < 0:
                result += '-' * abs(diff)
            else:
                result += '+' * diff
            memory[MEMORY_CELLS.UPPER_LETTERS] = ord(sign)
            prev_cell = MEMORY_CELLS.UPPER_LETTERS # Set previous memory cell to current
            result += '.' # Print sign from memory
        elif u.category(sign) == 'Nd': # Numbers
            diff = MEMORY_CELLS.NUMBERS - prev_cell # Difference between current cell and previous cell 
            if diff < 0:
                result += '<' * abs(diff)
            else:
                result += '>' * diff
            diff = ord(sign) - memory[MEMORY_CELLS.NUMBERS] # Difference between memory value and ord of sign
            if diff < 0:
                result += '-' * abs(diff)
            else:
                result += '+' * diff
            memory[MEMORY_CELLS.NUMBERS] = ord(sign)
            prev_cell = MEMORY_CELLS.NUMBERS # Set previous memory cell to current
            result += '.' # Print sign from memory
        elif u.category(sign) in ['Ps', 'Pe']: # { or }
            diff = MEMORY_CELLS.SPECIALS - prev_cell # Difference between current cell and previous cell 
            if diff < 0:
                result += '<' * abs(diff)
            else:
                result += '>' * diff
            diff = ord(sign) - memory[MEMORY_CELLS.SPECIALS] # Difference between memory value and ord of sign
            if diff < 0:
                result += '-' * abs(diff)
            else:
                result += '+' * diff
            memory[MEMORY_CELLS.SPECIALS] = ord(sign)
            prev_cell = MEMORY_CELLS.SPECIALS # Set previous memory cell to current
            result += '.' # Print sign from memory
    return result

print(f"Flag: {encrypt(flag)}")
print(f"Writing challenge to: {file_name}")

email = \
f"""
From: {hacker_name}
To: You

Dear user

I hacked your bank account. 
If you want to get your money back, tell me what's hidden in this message or pay me 13,37 BTC.

Message:
{encrypt(flag)}


Greetings,
{hacker_name} {encrypt(hacker_name)}

"""

with open(file_name, 'w') as w:
    w.write(email)
    print(f"Challenge generated to: {file_name}")
