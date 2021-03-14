//-std=c++2a
#include <vector>
#include <iostream>
#include <algorithm>
#include <ranges>
#include <string>
#include <unistd.h>
#include <cstdint>
#include <stdio.h>
uint8_t r1=0;
uint8_t r2=0;
uint8_t r3=0;
uint8_t sp=0;
uint8_t ip=0;
uint8_t ef=0;
std::vector<uint8_t> stack;

const uint8_t opcode[255]={0xf2,0x72,0x45,0x8a,0x72,0xf2,0x72,0x6e,0x8a,0x72,0xf2,0x72,0x74,0x8a,0x72,0xf2,0x72,0x65,0x8a,0x72,0xf2,0x72,0x72,0x8a,0x72,0xf2,0x72,0x20,0x8a,0x72,0xf2,0x72,0x70,0x8a,0x72,0xf2,0x72,0x61,0x8a,0x72,0xf2,0x72,0x73,0x8a,0x72,0xf2,0x72,0x73,0x8a,0x72,0xf2,0x72,0x77,0x8a,0x72,0xf2,0x72,0x6f,0x8a,0x72,0xf2,0x72,0x72,0x8a,0x72,0xf2,0x72,0x64,0x8a,0x72,0xf2,0x72,0x0a,0x8a,0x72,0xf2,0x5f,0x01,0xf2,0x72,0x0f,0xe5,0x01,0xf2,0x5f,0x00,0xf2,0x72,0x19,0xe5,0x00,0xf2,0x5f,0x33,0xbf,0x33,0x06,0xf2,0x5f,0x6c,0xbf,0x33,0x06,0xf2,0x5f,0x70,0xbf,0x33,0x06,0xf2,0x5f,0x40,0xbf,0x33,0x06,0xf2,0x5f,0x74,0xbf,0x33,0x06,0xf2,0x5f,0x24,0xbf,0x33,0x06,0xf2,0x5f,0x79,0xbf,0x33,0x06,0xf2,0x5f,0x72,0xbf,0x33,0x06,0xf2,0x5f,0x33,0xbf,0x33,0x06,0xf2,0x5f,0x74,0xbf,0x33,0x06,0xf2,0x5f,0x74,0xbf,0x33,0x06,0xf2,0x5f,0x40,0xbf,0x33,0x06,0xf2,0x5f,0x38,0xbf,0x33,0x06,0xf2,0x5f,0x33,0xbf,0x33,0x06,0xf2,0x5f,0x24,0xbf,0x33,0x06,0xf2,0x5f,0x72,0xbf,0x33,0x06,0xf2,0x5f,0x30,0xbf,0x33,0x06,0xf2,0x5f,0x68,0xbf,0x33,0x06,0xf2,0x5f,0x74,0xbf,0x33,0x06,0xf2,0x5f,0x63,0xbf,0x33,0x06,0xf2,0x5f,0x33,0xbf,0x33,0x06,0xf2,0x5f,0x72,0xbf,0x33,0x06,0xf2,0x5f,0x72,0xbf,0x33,0x06,0xf2,0x5f,0x30,0xbf,0x33,0x06,0xf2,0x5f,0x63,0xbf,0x33,0x06,0x8c,0xf8,0xf2,0x5f,0x01,0xe5,0x3c,0xf2,0x5f,0x00,0xe5,0x3c};
void interpreter_switch(const std::vector<uint8_t> &code);
void psh(const uint8_t reg1);
void pop(const uint8_t reg1);
void cmp();
void jmpif(const uint8_t value);
void movimm(const uint8_t reg1, const uint8_t value);
void sys(const uint8_t syscall_number);
void write_register(uint8_t reg,uint8_t value);
uint8_t read_register(const uint8_t reg,const uint8_t value);

int main()
{
    std::cout<<"This executable emulates custom architecture. Figure out how emulator works and take the flag. Good luck :)"<<std::endl;
    std::vector<uint8_t> code(std::ranges::begin(opcode),std::ranges::end(opcode));
    interpreter_switch(code);
    exit(0);
}


void interpreter_switch(const std::vector<uint8_t> &code)
{
    uint8_t instr;
    while(true)
    {
        instr=code.at(ip);
        switch (instr)
        {
            [[likely]]case 0x8a:
                psh(code.at(ip+1));
                break;
            [[likely]]case 0xbf:
                pop(code.at(ip+1));
                break;
            [[likely]]case 0x06:
                cmp();
                break;
            [[likely]]case 0x8c:
                jmpif(code.at(ip+1));
                break;
            [[likely]]case 0xf2:
                movimm(code.at(ip+1),code.at(ip+2));
                break;
            [[likely]]case 0xe5:
                sys(code.at(ip+1));
                break;
            [[unlikely]]default:
                std::cout<<"VM crashed(unknown instruction), existing...";
                exit(1);
                break;
        }
    }
}
void write_register(uint8_t reg, uint8_t value)
{
    switch(reg)
    {
        case 0x5f:
            r1=value;
            break;
        case 0x33:
            r2=value;
            break;
        case 0x72:
            r3=value;
            break;
        case 0xc3:
            sp=value;
            break;
        case 0x46:
            ip=value;
            break;
        case 0xfa:
            ef=value;
            break;
        [[unlikely]]default:
            std::cout<<"VM crashed(write unknown register), exiting...";
            exit(1);
            break;
    }
}
uint8_t read_register(const uint8_t reg)
{
    switch(reg)
    {
        case 0x5f:
            return r1;
            break;
        case 0x33:
            return r2;
            break;
        case 0x72:
            return r3;
            break;
        case 0xc3:
            return sp;
            break;
        case 0x46:
            return ip;
            break;
        case 0xfa:
            return ef;
            break;
        [[unlikely]]default:
            std::cout<<"VM crashed(read unknown register"<<reg<<"), exiting...";
            exit(1);
            break;
    }
}

void psh(const uint8_t reg1)
{
    uint8_t value=read_register(reg1);
    stack.push_back(value);
    sp=stack.size();
    write_register(0x46,ip+2);
}
void pop(const uint8_t reg1)
{
    uint8_t top_stack=stack.back();
    stack.pop_back();
    write_register(reg1,top_stack);
    write_register(0x46,ip+2);
}
void cmp()
{
    uint8_t diff;
    diff=r1-r2;
    uint8_t equals=!(diff==0);
    write_register(0xfa,ef+equals);
    write_register(0x46,ip+1);
}
void jmpif(const uint8_t value)
{
    if(ef==0)
    write_register(0x46,value);
    else
    write_register(0x46,ip+2);
}
void movimm(const uint8_t reg1, uint8_t value)
{
    write_register(reg1,value);
    write_register(0x46,ip+3);
}
void sys(const uint8_t syscall_number)
{
    switch (syscall_number)
    {
        case 0x00:
        {
            uint8_t stack_size=stack.size();
            if(stack_size<r2+r3)
            stack.resize(r2+r3);

            read(r1,(uint8_t *)(&stack[r2]),r3);
            write_register(0x46,ip+2);
            break;
        }
        case 0x01:
            write(r1,(uint8_t *)(&stack[r2]),r3);
            write_register(0x46,ip+2);
            break;
        case 0x3c:
            if(r1==0)
            std::cout<<"Correct Password\nConnect to server to grab the flag\n";
            else
            std::cout<<"Wrong Password\nTry again\n";
            
            exit(r1);
            break;
        [[unlikely]]default:
            std::cout<<"VM_crashed(Unknown syscall), exiting...\n";
            exit(1);
            break;
    }
}
