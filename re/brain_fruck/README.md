# Don't you F**k with my Brain

I recently got this strange email. I'm worried about my money. I think that someone is trying to f**k with my brain. Can you tell me what does it mean?

## Flag

```
bts{tempflag}
```

## How to run

To generate files for this challenge you need to:

1. Write correct flag to `generate.py`:
```python
flag = "your_flag"
```
Remember that flag can only contain lower, upper letters, numbers and '{' '}'

2. Execute following command:
```
python3 generate.py
```

Your challenge file (default name is `email.txt`) will be created in the same directory.

## Solution

This challenge is based on esoteric programming language called [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck). What you have to do is to find out how is memory allocated.
Basing on example (hacker's signature in both English and Brainfuck) you can assume that upper letters are stored in second cell, all lower letters are operating on third cell and numbers on fourth. What you are missing are special characters like `{` and `}`.

Character `.` in Brainfuck allows you to print out memory value. Now we can assume that `.` is located after each sign. Basing on this knowledge and the fact that format of flag is specified we can find where `{` and `}` begin in message. This allows us to figure out that specials are stored in fifth memory cell.

What we do not know are starting values of memory. Basing on amount of `+` and `-` of first signs from each type and their ASCII decimal values we can assume that memory starts like this:
```
[0, 60, 90, 50, 120]
```

Using online tools like [this](https://fatiherikli.github.io/brainfuck-visualizer/) we can visualize it and solve this challenge.

Final memory filling function looks like this:

```Brainfuck
+++++ +++++         
[                       
     > +++++ +              
     > +++++ ++++            
     > +++++                
     > +++++ +++++ ++       
<<<< -              
]
```