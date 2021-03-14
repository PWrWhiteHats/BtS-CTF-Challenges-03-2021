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
std::string read_name(const uint8_t reg);

int main()
{
    std::cout<<"This executable emulates custom architecture. Figure out how emulator works and take the flag. Good luck :)"<<std::endl;
    std::vector<uint8_t> code(std::ranges::begin(opcode),std::ranges::end(opcode));
    interpreter_switch(code);
    exit(0);
}


void interpreter_switch(const std::vector<uint8_t> &code)
{
    printf("r1:%2X r2:%2X r3:%2X sp:%2X ip:%2X ef:%2X\n",r1,r2,r3,sp,ip,ef);
    printf("stack size:%2X stack:",stack.size());
    std::ranges::for_each(stack,[](uint8_t value){printf("%2X ",value);});
    printf("\n");
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
                std::cout<<"VM crashed(unknown instruction"<<code.at(ip)<<"), existing...";
                exit(1);
                break;
        }
    printf("r1:%2X r2:%2X r3:%2X sp:%2X ip:%2X ef:%2X\n",r1,r2,r3,sp,ip,ef);
    printf("stack size:%2X stack:",stack.size());
    std::ranges::for_each(stack,[](uint8_t value){printf("%2X ",value);});
    printf("\n");
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
            std::cout<<"VM crashed(write unknown register"<<reg<<"), exiting...";
            printf("%2X ",reg);
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

std::string read_name(const uint8_t reg)
{
    if(reg==0x5f)
    {
        return "r1";
    }
    else if(reg==0x33)
    {
        return "r2";
    }
    else if(reg==0x72)
    {
        return "r3";
    }
    else if(reg==0xc3)
    {
        return "r3";
    }
    else if(reg==0x46)
    {
        return "ip";
    }
    else if(reg==0xfa)
    {
        return "ef";
    }
    else
    {
        std::cout<<"VM crashed(name unknown register), exiting...";
        exit(1);
    }
}

void psh(const uint8_t reg1)
{
    uint8_t value=read_register(reg1);
    stack.push_back(value);
    sp=stack.size();
    write_register(0x46,ip+2);

    printf("psh %s\n",read_name(reg1).c_str());
}
void pop(const uint8_t reg1)
{
    uint8_t top_stack=stack.back();
    stack.pop_back();
    write_register(reg1,top_stack);
    write_register(0x46,ip+2);

    printf("pop %s\n",read_name(reg1).c_str());
}
void cmp()
{
    uint8_t diff;
    diff=r1-r2;
    uint8_t equals=!(diff==0);
    write_register(0xfa,ef+equals);
    write_register(0x46,ip+1);

    printf("cmp r1,r2\n");
}
void jmpif(const uint8_t value)
{
    if(ef==0)
    write_register(0x46,value);
    else
    write_register(0x46,ip+2);
    
    printf("jmp if %2X == 0 to ip %2X\n",ef,value);
}
void movimm(const uint8_t reg1, uint8_t value)
{
    write_register(reg1,value);
    write_register(0x46,ip+3);

    printf("movimm %s,%2X\n",read_name(reg1).c_str(),value);
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

            printf("sys_read (%2X,%2X,%2X)\n",r1,r2,r3);
            break;
        }
        case 0x01:
        {
            write(r1,(uint8_t *)(&stack[r2]),r3);
            write_register(0x46,ip+2);

            printf("sys_write (%2X,%2X,%2X)\n",r1,r2,r3);
            break;
        }
        case 0x3c:
        {
            if(r1==0)
            std::cout<<"Correct Password\nConnect to server to grab the flag\n";
            else
            std::cout<<"Wrong Password\nTry again\n";

            printf("sys_exit (%2X)",r1);
            exit(r1);
            break;
        }
        [[unlikely]]default:
            std::cout<<"VM_crashed(Unknown syscall), exiting...\n";
            exit(1);
            break;
    }
}
