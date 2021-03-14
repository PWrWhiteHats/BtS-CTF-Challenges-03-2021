import random as ran

try:
    with open('flag.txt', 'r') as r:
        FLAG = r.read().strip()
except FileNotFoundError:
    FLAG = "bts{temp_flag}"
CODE = ran.getrandbits(len(FLAG))
CHALL_FILE = "challenge/challenge.c"
CHALL_FUNC_NAME = "__wasm_get_12vyatwd76"
HELPERS_JS_TEMPLATE = "challenge/base_files/helpers.js.template"
HELPERS_JS = "challenge/static/js/helpers.js"
chall = \
"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <emscripten/emscripten.h>

char* EMSCRIPTEN_KEEPALIVE {WASM_FUNC_NAME}(char* secret_key) {
    int CORRECT_CODE[] = {CODE_TEMPLATE};
    int correct_code_len = sizeof(CORRECT_CODE)/sizeof(CORRECT_CODE[0]);
    char correct_code_chr[correct_code_len+1];
    for(int i=0; i<correct_code_len; i++){
        correct_code_chr[i] = (char)CORRECT_CODE[i];
    }
    correct_code_chr[correct_code_len]='\\0';

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

    int jio98941Adm12[] = {FLAG_TEMPLATE};
    int ad78y2eyfuadyta_len = sizeof(jio98941Adm12)/sizeof(jio98941Adm12[0]);
    char ad78y2eyfuadyta[ad78y2eyfuadyta_len+1];
    char* ret;
    for(int i=0; i<ad78y2eyfuadyta_len; i++){
        ad78y2eyfuadyta[i] = (char)jio98941Adm12[i];
    }
    ret = ad78y2eyfuadyta;
    return ret;
}
"""

flag_arr = [hex(ord(c)) for c in FLAG]
code_str = [hex(ord(c)) for c in str(CODE)]

CH_FLG = [f"{c}" for c in flag_arr]
FLAG_TEMPLATE = '{ ' + ','.join(CH_FLG) + ' }'
CH_CODE = [f"{c}" for c in code_str]
CODE_TEMPLATE = '{ ' + ','.join(CH_CODE) + ' }'

chall = chall.replace("{FLAG_TEMPLATE}", FLAG_TEMPLATE).replace("{CODE_TEMPLATE}", CODE_TEMPLATE).replace("{WASM_FUNC_NAME}", CHALL_FUNC_NAME)
with open(CHALL_FILE, 'w') as w:
    w.write(chall)

with open(HELPERS_JS_TEMPLATE, 'r') as f:
    content = f.read()
    content = content.replace('WASM_FUNCTION', CHALL_FUNC_NAME)
    with open(HELPERS_JS, 'w') as f:
        f.write(content)

info = \
f"""
Your challenge is ready!
Flag: {FLAG}
Solve code: {CODE}
Challenge file: {CHALL_FILE}
Execute following command to prepare files:

emcc {CHALL_FILE} -s WASM=1 -o challenge/static/js/module.js  -s NO_EXIT_RUNTIME=1  -s EXPORTED_FUNCTIONS="['_{CHALL_FUNC_NAME}']" -s "EXTRA_EXPORTED_RUNTIME_METHODS=['cwrap']"
"""
print(info)
