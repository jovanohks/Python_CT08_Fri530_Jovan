import random
char=[]
for i in range(33,48):
    char.append(chr(i))
for i in range(58,65):
    char.append(chr(i))
for i in range(91,97):
    char.append(chr(i))
for i in range(123,127):
    char.append(chr(i))
for i in range(65,91):
    char.append(chr(i))
for i in range(97,123):
    char.append(chr(i))
for i in range(48,58):
    char.append(chr(i))
def generate_password(length):
    pw=""
    for i in range(0,length):
        pw+=random.choice(char)
    return pw
print(generate_password(1000000))