s={
    "pen":1.5,
    "book":5,
    "notebook":2.5,
    "calculator":30
}
for a,b in s.items():
    print(f"{a}: ${b}")
x=True
while x==True:
    x=input("What do you want to buy?")
    if x in s:
        y=int(input("how many do you want to buy"))
    elif not x in s:
        print("not in bookshop")
    elif x =="no more":
        break