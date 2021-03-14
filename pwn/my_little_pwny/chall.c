#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    char tab[32];
    printf("Hey, what's your name?\n");
    fflush(stdout);
    fflush(stdin);
    scanf("%s", &tab);
    printf("Hi %s!\n", tab);
    return 0;
}
