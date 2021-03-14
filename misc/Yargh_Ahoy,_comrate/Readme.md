# Yargh! Ahoy, comrate!

Ahoy! let's play a game. I will ask ye three questions an' ye need to answer correctly. Talk to me by usin' YARghA... ekhm jara. 
 ye need to find a secret phrase to start talk to me! this is where i want to come from!

I really want to Sing and Dance!  yo-ho-ho

# Flag

```
BtS-CTF{-a-merry-life-and--a-short-one--shall-be-my-motto-}
```

# Setup

You need to download hosted .tar.gz file and extract it. Then download YARA and use it (or cheat :D).
[YARA docs](https://yara.readthedocs.io/en/stable/gettingstarted.html)
[Yara newest version](https://github.com/virustotal/yara/releases/tag/v4.0.2)
or use grep :)

# Solution

Firstly, to find out the key, you need to communicate with pirate via YARA - description gives a hint. 
First secret key, obtained thankfully from last sentence (```I really want to Sing and Dance!  yo-ho-ho``` and ```this is where i want to come from!``` ) is "**Penzance**":

Because of:
*The Pirate Song (I Want to Sing and Dance), Ray Stevens*
>"I want to be a pirate in the Pirates of **Penzance**"

So, you need to develop YARA rule with secret key:

```
rule talk_to_me
{
    strings:
        $key = "Penzance"

    condition:
        $key
}
```

Then use created yara rule and search for file:
```
yara -r talk_to_me Adventure/
```

You will see the output below:
```
talk_to_me Adventure//LZePKhCrJ6WqskbOTxWniPa0ulEpSVtJ/file023.txt
```

Open pointed file by using text editing or reading command like cat, nano, etc.
Find a note.

In the files pirate starts to asking a questions - if you think your answer is correct - you need to conduct search again with that phrase.
Each good answer provides you a clue about a flag. When you answer for all questions you need to match clues.

## Question #1

```
Ye nailed it! arggh 

when I waitin' fer ye I found first clue, but I need yer answer... Sailor!

who makes it, 'as no need o' it.
who buys it, 'as no use fer it.
who uses it can neither see nor feel it.
what be it?

or ye will feed the fishes!
```
**Answer:** coffin

**Yara** 
```
rule first_question
{
    strings:
        $answer = "coffin"

    condition:
        $answer
}
```
```
yara -r first_question Adventure/
first_question Adventure//GdoS7GkGS3Y9KGALnlFgjbY15UpYwtvr/file067.txt
```

## Question #2

```
Shiver me timbers! so as I promised - take it: 
2d 73 68 61 6c 6c 2d 62 65 2d 6d 79 2d 6d 6f 74 74 6f 2d

when ye diggin' yer own grave in 'opeless state o' mind I invented new kind o' puzzle - make the equation true! 
savvy? harharr answer me rookie! 

   BARN
 BEACON
+   BEN
-------
 BAMBOO

```
**Obtained part of flag:** 2d 73 68 61 6c 6c 2d 62 65 2d 6d 79 2d 6d 6f 74 74 6f 2d

**Answer:** 584566

>**Alphametic puzzles** are arithmetic problems which involve words where each letter stands for unique digit *that makes the arithmetic equation true*. 

```
   BARN
 BEACON
+   BEN
-------
 BAMBOO
has 1 solution in base 10.

It is:

   5832    A=8 B=5 C=1 E=7 M=4 N=2 O=6 R=3 
 578162
+   572
-------
 584566

```
**Yara** 
```
rule second_question
{
    strings:
        $answer = "584566"

    condition:
        $answer
}
```
```
yara -r second_question Adventure/
second_question Adventure//C35A4TY4XD8e4C2OUe4IlhhMvSdW6Sht/file016.txt
```


## Question #3


```
Arrrrrr, arr, matey 'ave yer next part!
2d 61 2d 6d 65 72 72 79 2d 6c 69 66 65 2d 61 6e 64 2d

allright seadog, last one an' I give to the sky...
 ye see I really like oranges an' I 'ave a lack o' it.
 other gentleman o' fortune left me a note where I can sail to buy more.
 Somewhere to battista della porta to scurvy dog named giovanii... 
 'elp me! note says:

lvvrqrihkfaxtjyvgiyewsdzfvcryfqtkschmjoonquarslcnufqslcnhjnhwtjpfgnulwitrmspvivaoq
```

**Obtained part of flag:** 2d 61 2d 6d 65 72 72 79 2d 6c 69 66 65 2d 61 6e 64 2d

**Answer:** sailacrosstheseatoitalymyfriendandyouwillhavemoreandmoreorangesinthenaplescampania

> **Giovanii Battista della Porta** was a known Italian scholar, which investigated various topics related to  occult philosophy, astrology, alchemy, mathematics, meteorology, and natural philosophy.

For us is this important, because he developed a cipher called [Porta Chiper](http://practicalcryptography.com/ciphers/classical-era/porta/). 
Key word used by gentleman o' fortune was **oranges**.

**Yara** 
```
rule third_question
{
    strings:
        $answer = "sailacrosstheseatoitalymyfriendandyouwillhavemoreandmoreorangesinthenaplescampania"

    condition:
        $answer
}
```
```
yara -r third_question Adventure/
third_question Adventure//fYY686W9dnL4dmsH6wg1g0DSrQTIvIG7/file084.txt
```

## Final clues matching

After run yara with decrypted message, captain proves last part of flag, which you need to match:

```
Swashbuckler, 'ow dare ye!
arrrggghhhh, take it an' enjoy yer victory!
2d 61 2d 73 68 6f 72 74 2d 6f 6e 65 2d
```
**Obtained part of flag:** 2d 61 2d 73 68 6f 72 74 2d 6f 6e 65 2d

You need to decode hex to ASCII and match phrase in good order. 
Decoded parts:
 - **First part:** -shall-be-my-motto-
 - **Second part:** -a-merry-life-and-
 - **Third part:** -a-short-one-

Matched in good order: **-a-merry-life-and--a-short-one--shall-be-my-motto-**

>“In an honest service there is thin commons, low wages, and hard labour. In this, plenty and satiety, pleasure and ease, liberty and power; and who would not balance creditor on this side, when all the hazard that is run for it, at worst is only a sour look or two at choking? No, **a merry life and a short one shall be my motto**.”
>*-A General History of the Robberies and Murders of the most notorious Pyrates (1724).*
>*[Bartholomew Roberts “Black Bart”](https://en.wikipedia.org/wiki/Bartholomew_Roberts) - pirate *
 

