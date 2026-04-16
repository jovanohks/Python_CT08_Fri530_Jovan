import os
def ceasar_shift_character(char,key,mode):
    ascii_value=ord(char)-32
    #print(ascii_value)
    if mode.lower()=="encrypt":
        
        ascii_value +=key
        ascii_value =ascii_value %95
        ascii_value+=32
    elif mode.lower()=="decrypt":
        ascii_value-=key
        ascii_value =ascii_value %95
        ascii_value+=32
    char=chr(ascii_value)
    return char
def ceasar_shift_sentence(sentence,key,mode):
    encrypted_sentence=""
    for char in sentence:
        encrypted_sentence+=ceasar_shift_character(char,key,mode)
    return encrypted_sentence
def ceasar_shift_file(input_file,output_file,key,mode):
    with open(input_file,"r") as file:
        char=file.read()
        x=[]
        x+=ceasar_shift_sentence(char,key,mode)
    with open(output_file,"w") as file:
        file.writelines(x)
def brute_force_decrypt(input_file):
    with open(input_file,"r") as file:
        x=file.read()
        for i in range(0,95):
            print(f"key {i}")
            print(ceasar_shift_sentence(x))
input_file=os.path.join(os.getcwd(),"encrypted.txt")
output_file=os.path.join(os.getcwd(),"decrypted.txt")
ceasar_shift_file(input_file,output_file,20,"decrypt")