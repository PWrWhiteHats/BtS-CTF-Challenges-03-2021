#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* flg = "]1nH^oa86K2z0kL+z*NzmLQ%Rz/Kp+_zSOSt:";
int cipher_rounds=27;

void printMessage() {
    printf("Give me the flag!\n");
}

char* getInput() {
    char* buffer;
    size_t bufsize = 32;
    buffer = (char *)malloc(bufsize * sizeof(char));
    if( buffer == NULL)
    {
        perror("Unable to allocate buffer");
        exit(1);
    }
    getline(&buffer,&bufsize,stdin);
    return buffer;
}

char* encryptInput(char* input) {
    size_t length = strlen(input);
    for(int i=0; i<cipher_rounds; i++) {
        for(int j=0; j<length; j++) {
            input[j]++;
            if(input[j] > 126)
                input[j] -= 94;
        }

    }
    return input;
}

bool checkIfInputIsOK(char* encryptedInput) {
    size_t length = strlen(encryptedInput);
    size_t flg_length = strlen(flg);
    int result = 0;
    if(flg_length < length)
        length = flg_length;
    for(int i=0; i<length; i++) {
        if(encryptedInput[i] == flg[i])
            result++;
    }
    if(result == flg_length)
        return true;
    return false;
}

int main() {
    printMessage();
    char* input = getInput();
    char* encryptedInput = encryptInput(input);
    if(checkIfInputIsOK(encryptedInput))
        printf("Congratulations!");
    else
        printf("Nope");
}