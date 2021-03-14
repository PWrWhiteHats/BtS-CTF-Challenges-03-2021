#include <stdio.h>
#include <stdlib.h>

void win() 
{
    printf("Congratulations!\n");
    printf("Grab your flag!\n");
    printf("BtS-CTF{smash_da_stack_for_fun_and_flags}\n");
    exit(0);
}

int main(int argc, char *argv[])
{
    char tab[32];
    printf("Hey, what's your name?\n");
    fflush(stdout);
    fflush(stdin);
    scanf("%s", &tab);
    printf("Hi %s!\n", tab);
    return 0;
}
