## ret FTW

_Author: [xxzxcuzx-me](https://github.com/xxzxcuzx-me)

Who would even check array boundaries? It's too much hassle. Nah, I'm just gonna copy everything, what can go possibly wrong?

## Flag

BtS-CTF{smash_da_stack_for_fun_and_flags}

## How to run

This chall comes with two files. One is for the player, and the second should be run on the server. The one for the player includes censored flag. Please make sure that flag in user's file is the same length as in server file.
To compile it just run command: 
gcc filename -o chall -no-pie -fno-stack-protector -z execstack
On the serverside just disable ASLR with 
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'
and run command
tcpserver -t 50 -RHl0 0.0.0.0 4444 ./chall

If you don't have tcpserver, it is in ucspi-tcp package.
Reference: [https://anee.me/how-to-host-a-ctf-b644a1f15618]

## Solution

Check in [solution folder](./solution/README.md)
