
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <emscripten/emscripten.h>

char* EMSCRIPTEN_KEEPALIVE __wasm_get_12vyatwd76(char* secret_key) {
    int CORRECT_CODE[] = { 0x32,0x34,0x35,0x38,0x35,0x38,0x37,0x39,0x30,0x36,0x38,0x33,0x33,0x35,0x31,0x36,0x32,0x39,0x35,0x32,0x30,0x33,0x35,0x31,0x32,0x35,0x34,0x37,0x37,0x38,0x34,0x32,0x38,0x30,0x31,0x30,0x31,0x32,0x32,0x34,0x33,0x36,0x32,0x36,0x31,0x37,0x31,0x30,0x37 };
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

    int jio98941Adm12[] = { 0x42,0x74,0x53,0x2d,0x43,0x54,0x46,0x7b,0x56,0x47,0x56,0x73,0x62,0x43,0x42,0x74,0x5a,0x53,0x42,0x6f,0x62,0x33,0x63,0x67,0x65,0x57,0x39,0x31,0x49,0x47,0x64,0x76,0x64,0x43,0x42,0x70,0x64,0x43,0x34,0x67,0x52,0x47,0x6c,0x6b,0x49,0x48,0x6c,0x76,0x64,0x53,0x42,0x6b,0x5a,0x57,0x4a,0x31,0x5a,0x79,0x42,0x70,0x64,0x43,0x42,0x76,0x63,0x69,0x42,0x6b,0x61,0x57,0x51,0x67,0x65,0x57,0x39,0x31,0x49,0x47,0x70,0x31,0x63,0x33,0x51,0x67,0x63,0x6d,0x56,0x68,0x5a,0x43,0x42,0x30,0x61,0x47,0x55,0x67,0x5a,0x6d,0x78,0x68,0x5a,0x79,0x42,0x6d,0x63,0x6d,0x39,0x74,0x49,0x48,0x64,0x68,0x63,0x32,0x30,0x67,0x5a,0x6d,0x6c,0x73,0x5a,0x54,0x38,0x67,0x53,0x53,0x42,0x68,0x62,0x53,0x42,0x72,0x61,0x57,0x35,0x6b,0x59,0x53,0x42,0x6a,0x64,0x58,0x4a,0x70,0x62,0x33,0x56,0x7a,0x4c,0x69,0x41,0x76,0x51,0x58,0x4a,0x78,0x63,0x33,0x6f,0x75,0x7d };
    int ad78y2eyfuadyta_len = sizeof(jio98941Adm12)/sizeof(jio98941Adm12[0]);
    char ad78y2eyfuadyta[ad78y2eyfuadyta_len+1];
    char* ret;
    for(int i=0; i<ad78y2eyfuadyta_len; i++){
        ad78y2eyfuadyta[i] = (char)jio98941Adm12[i];
    }
    ret = ad78y2eyfuadyta;
    return ret;
}
