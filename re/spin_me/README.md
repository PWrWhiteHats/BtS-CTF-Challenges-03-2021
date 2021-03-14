# Spin me

Crack me plz

## Flag

```
BtS-CTF{y0u_sP1n_m3_R16h7_r0UnD_848Y}
```

## How to run

Run prepare_flag with number of encryption rounds and a flag as parameters, to create encrypted flag. Then place result in `flg` variable in chall.c and chosen number of rounds in `cipher_rounds` variable. Then compile chall.c using `g++ chall.c -o chall` and provide this binary to players.

## Solution

So it's typical crack me. You have to reverse engineer the program and understand the algorithm behind it. In this case it's a variation of Ceasar's cipher - only over space of ASCII characters between 33 and 126, and with different shift. 