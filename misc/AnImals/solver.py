import re
from predictor import Predict

input_images = 'flag'
model_path = 'DogCat.h5'

def string_2_bin(string_text):
    return ''.join(format(ord(i), '08b') for i in string_text) 

def bin_2_dec(binary): 
    if len(binary) < 8:
        binary = binary.zfill(8)
    string = int(binary, 2) 
      
    return string

def convert_bin_to_str(binary):
    str_data =' '
    for i in range(0, len(binary), 8): 
        temp_data = binary[i:i + 8]
        decimal_data = bin_2_dec(temp_data) 
        str_data = str_data + chr(decimal_data)  
    
    return str_data

if __name__ == '__main__':
    pred = Predict(model_path)
    pred.load_model()

    result_flag = pred.get_the_flag(input_images)
    print(result_flag)
    converted_result = convert_bin_to_str(result_flag)
    print(f"Enconded string is: {converted_result}")

    x = re.findall(r'BtS-CTF{.*}', converted_result)

    if x:
        flag = x[0]
        print(f"The flag is: {flag}")
    else:
        print('Flag not found. :(')
