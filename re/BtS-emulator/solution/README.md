# Solution

## Solution I
Decompile emulator, write disassembler/debugger for architecture, and find correct password.

## Solution II
Easier way(unintended solution) copy opcodes from executable
```
xxd -c 6 opcodes
```
then read password from bottom to top
