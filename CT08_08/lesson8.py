import os
fullpath=os.getcwd()
filepath=os.path.join(fullpath,"sherlock.txt")
print(filepath)

if not os.path.exists(filepath):
    print("file does not exist")

with open(filepath,"r") as file:
    lines=file.read()
print(f"{len(lines)} characters")
a=0
e=0
i=0
o=0
u=0
for l in lines:
    if l=="a" or l=="A":
        a+=1
    elif l=="e" or l=="E":
        e+=1
    elif l=="i" or l=="I":
        i+=1
    elif l=="o" or l=="O":
        o+=1
    elif l=="u" or l=="U":
        u+=1

print(f"A:{a}, E:{e}, I:{i}, O:{o},U:{u},total {a+e+i+o+u}")
print(f"total percentage of vowels: {(((a+e+i+o+u)/len(lines))*100):.2f}%")
with open("results.txt","w") as file:
    file.write(f"Text analysis\n")
    file.write(f"Total number of characters: {len(lines)}\n")
    file.write(f"Total vowels: {a+e+i+o+u}\n\nVowel frequency:\n")
    file.write(f"A:{a}\nE:{e}\nI:{i}\nO:{o}\nU:{u}\n")
    file.write(f"Total percentage of vowels in text: {(((a+e+i+o+u)/len(lines))*100):.2f}%\n")
print(f"Results have been written to results.txt")