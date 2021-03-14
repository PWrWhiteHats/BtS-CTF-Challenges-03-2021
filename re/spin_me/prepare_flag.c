#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cipher_rounds=27;

char* encryptInput(char* input) {
    size_t length = strlen(input);
    int cipher_rounds = 27;
    for(int i=0; i<cipher_rounds; i++) {
        for(int j=0; j<length; j++) {
            input[j]++;
            if(input[j] > 126)
                input[j] -= 94;
        }

    }
    return input;
}

int main(int argc, char *argv[]) {
    if(argc < 3) {
        printf("Usage: %s number_of_rounds flag\n", argv[0]);
        exit(0);
    }
    cipher_rounds = atoi(argv[1]);
    char* flag = (char*)malloc(strlen(argv[2]) + 1); 
    strcpy(flag, argv[2]);
    char* encryptedInput = encryptInput(argv[2]);
    printf("Flag %s encrypted with %d rounds:\n%s\n", flag, cipher_rounds, encryptedInput);
}