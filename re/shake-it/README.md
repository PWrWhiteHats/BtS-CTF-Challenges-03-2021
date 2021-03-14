# Shake-It

*Author: __Hck__*

## Description 

We have acquired hash of the flag in a database leak.  
We've heard that you are a cryptoanalyst,  
so better crack this flag or we'll be  
forced to force a wrench UYB

Hash: `4a3ad948eb3eceb425b74609f480951c3d5503a3a9f4bef9d713dae9dc14d71e1e155192`  
Sauce: [shake-it.rb](./shake-it.rb)

## Flag

Current flag is: `BtS-CTF{L1ke_m3rs3nne_Tw15ter_19937}`

You can use `./flaggen` to generate other flag if you want to, just change the variable and run the script.

## How to use

This is an offline challenge, just host the 'shake-it.rb' file, and allow it's download.

## Write-up

Upper 3 bits of hash are left untouched, you can use them to find next 3 bits of original data and so on. If you don't feel like bitfidling hero, you can do it in-place, bit-by-bit with ofset of 3 bits. See `solution.rb`.