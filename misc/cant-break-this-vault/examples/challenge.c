
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <emscripten/emscripten.h>

char* EMSCRIPTEN_KEEPALIVE __wasm_get_12vyatwd76(char* secret_key) {
    int CORRECT_CODE[] = { 0x33,0x39,0x32,0x34 };
    int correct_code_len = sizeof(CORRECT_CODE)/sizeof(CORRECT_CODE[0]);
    char correct_code_chr[correct_code_len+1];
    for(int i=0; i<correct_code_len; i++){
        correct_code_chr[i] = (char)CORRECT_CODE[i];
    }
    correct_code_chr[correct_code_len]='\0';

    int len_sk = strlen(secret_key);
    int len_cc = strlen(correct_code_chr);
    if(len_sk != len_cc){
        return "0";
    }

    for(short i=0; i<strlen(correct_code_chr); i++) {
        if( secret_key[i] != correct_code_chr[i] ) {
            return "0";
        }
    }

    int jio98941Adm12[] = { 0x62,0x74,0x73,0x7b,0x65,0x78,0x61,0x6d,0x70,0x6c,0x65,0x7d };
    int ad78y2eyfuadyta_len = sizeof(jio98941Adm12)/sizeof(jio98941Adm12[0]);
    char ad78y2eyfuadyta[ad78y2eyfuadyta_len+1];
    char* ret;
    for(int i=0; i<ad78y2eyfuadyta_len; i++){
        ad78y2eyfuadyta[i] = (char)jio98941Adm12[i];
    }
    ret = ad78y2eyfuadyta;
    return ret;
}
