stuff={
    "pen":1.5,
    "book":5,
    "notebook":2.5,
    "calculator":30
}
global items
global total
def listitem(lis):
    for a,b in lis.items():
        print(f"{a}: ${b}")
def get_order(lis):

    total = 0
    items = {}
    y = True
    while y == True:
        user = input("What do you want to buy? ")
        if user in lis:
            #y=int(input("how many do you want to buy"))
            a= input("do you want to add to order? y/n: ")
            if a == "y":
                
                amt = int(input("how many? "))
                print(f"{amt} {user} added to order")
                items[user] = {"amt":amt,"cost":lis[user]}
                total = total+(amt*lis[user])
            else:
                print(f" not added to order.")
        elif user == "no more":
            break
        elif not user in lis:
            print("not in bookshop")
def summary():
    print("order summary")
    for a,b in items.items():
        print(f"{a}: {b['amt']} @ ${b['cost']:.2f} each = ${(b['amt'] * b['cost']):.2f}")

    print(f"total: ${total:.2f}")
def discount():
    d=total
    print(d)
    if d> 20:
        d=d*0.8
        print(f"discounted 20% total is ${d:.2f} discounted ${(d*0.25):.2f}")





listitem(stuff)
get_order(stuff)
summary()
discount()