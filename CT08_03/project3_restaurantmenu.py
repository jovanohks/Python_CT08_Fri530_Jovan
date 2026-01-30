# d=True
# food={"hamburger":5.7,"fries":4.6,"coke":3.2,"ice cream":3,"nuggets":6}
# new_dict={}
# print("welcome to restraunt heres our bad menu")
# for a,b in food.items():
#     print(f"{a}: ${b:.2f}")
# while d==True:
#     x=input("what do u want to order ")
#     if x in food:
#         print(f"it costs ${food[x]:.2f}")
#         yn = input("add 2 order? (y/n) ")
#         if yn == "y":
#             print("added to order")
#             new_dict[x]=food[x]
#         else:
#             print("not added 2 order")
            
#     elif x =="no more":
#         print("thank you")
#         break
#     else:
#         print("not in menu")
# print(new_dict)
# x = 0
# for i in new_dict:
#     x+=new_dict[i]
# print("---------order summary-------")
# for a,b in new_dict.items():
#     print(f"{a}: ${b:.2f}")
# print(f"total bill: ${x:.2f}") 
d=True
food={"hamburger":5.7,"fries":4.6,"coke":3.2,"ice cream":3,"nuggets":6}
new_dict={}
w=int(input("how much do u have in ur wallet?"))
print("welcome to restraunt heres our bad menu")
for a,b in food.items():
    print(f"{a}: ${b:.2f}")
while d==True:
    x=input("what do u want to order ")

    if x[0:6] =="delete":
        y=x[7:]
        if y in new_dict:
            w+=new_dict[y]
            del new_dict[y]
            print(w)
            
    elif x in food:
        print(f"it costs ${food[x]:.2f},wallet left {w:.2f}")
        yn = input("add 2 order? (y/n) ")
        if yn == "y":
            if food[x] > w:
                print("not enough money, food not added to order")
            elif food[x] <= w :
                
                print("added to order")
                new_dict[x]=food[x]
                w-=food[x]
        else:
            print("not added 2 order")     
    elif x =="no more":
        print("thank you")
        break
    else:
        print("not in menu")

x = 0
for i in new_dict:
    x+=new_dict[i]
print("---------order summary-------")
for a,b in new_dict.items():
    print(f"{a}: ${b:.2f}")
print(f"total bill: ${x:.2f}") 
print(f"wallet left ${w:.2f}")