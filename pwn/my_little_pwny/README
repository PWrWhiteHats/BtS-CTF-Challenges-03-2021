# My little pwny

_Author: [xxzxcuzx-me](https://github.com/xxzxcuzx-me)


Hey, do you see what I see? It's buffer overflow snow! Go grab your nop sled and slide right into EIP! Last at the shell is a $cr1p7 k1dd13!

## Flag

BtS-CTF{4ll_y0ur_sh3ll_4r3_b3l0ng_to_us}

## How to run

To compile it just run command: 
gcc filename -o chall -m32 -fno-stack-protector -z execstack
On the serverside just disable ASLR with 
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'
and run command
tcpserver -t 50 -RHl0 0.0.0.0 4444 ./chall

If you don't have tcpserver, it is in ucspi-tcp package.
Reference: [https://anee.me/how-to-host-a-ctf-b644a1f15618]

## Solution

Check in [solution folder](./solution/README.md)
