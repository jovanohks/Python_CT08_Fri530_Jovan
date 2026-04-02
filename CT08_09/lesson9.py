import os
filepath=os.getcwd()
fullpath=os.path.join(filepath,"encrypted_note.txt")
d=""
new_lines =""
e=""
if not os.path.exists(fullpath):
    print(f"The encrypted note has vanished. Is someone trying to hide the truth?")
else:
    with open(fullpath,"r") as file:
        lines=file.read()
        print(f"Passage: {lines}")
    for i in lines:
        if i.isalpha() or i ==" ":
            new_lines +=i.lower()
    print(f"cleaned passage: \n\n{new_lines}")
    for i in range(len(new_lines)):
        if i==0:
            d+=new_lines[i]
        elif new_lines[i] ==" ":
            d+=new_lines[i+1]
    print(f"decrypted message is: {d}")
    print(f"encrypted: {d[::-1]}")
    with open("hidden_message.txt","w") as file:
        file.write(f"{d[::-1]}")