s={
    "pen":1.5,
    "book":5,
    "notebook":2.5,
    "calculator":30
}
def x(m):
    for a,b in m.items():
        print(f"{a}: ${b}")
def z(m):
    global z
    global t
    t=0
    z={}
    y=True
    while y==True:
        x=input("What do you want to buy?")
        if x in m:
            #y=int(input("how many do you want to buy"))
            a=input("do you want to add to order? y/n: ")
            if a =="y":
                print(f"added to order")
                q=int(input("how many?"))
                z[x]={"q":q,"c":m[x]}
                t=t+(q*m[x])
            else:
                print(f" not added to order.")
        elif x =="no more":
            break
        elif not x in m:
            print("not in bookshop")
def y():
    print("order summary")
    for a,b in z.items():
        print(f"{a}: {b['q']} @ ${b['c']:.2f} each = ${(b['q'] * b['c']):.2f}")
    print(f"total: ${t:.2f}")
# def d():
#     if t >=20:
#         t=0.9*t
#         print(f"20% discount applied, total with discount is ${t:.2f}")




x(s)
z(s)
y()
d()