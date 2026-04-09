import random
# char=[]
# for i in range(33,48):
#     char.append(chr(i))
# for i in range(58,65):
#     char.append(chr(i))
# for i in range(91,97):
#     char.append(chr(i))
# for i in range(123,127):
#     char.append(chr(i))
# for i in range(65,91):
#     char.append(chr(i))
# for i in range(97,123):
#     char.append(chr(i))
# for i in range(48,58):
#     char.append(chr(i))
def generate_password(length):
    has_upper=False
    has_lower=False
    has_symbol=False
    has_digit=False
    valid=False
    while not valid:
        pw=""
        for i in range(0,length):
            char_type=["lower","upper","digit","symbol"]
            choice =random.choice(char_type)
            if choice =="upper":
                pw+=chr(random.randint(65,90))
            elif choice =="lower":
                pw+=chr(random.randint(97,122))
            elif choice=="digit":
                pw+=chr(random.randint(48,57))
            elif choice=="symbol":
                pw+=chr(random.randint(33,47))
        for i in pw:
            if i==chr(range(65,90)):
                has_upper==True
            elif i==chr(range(97,122)):
                has_lower==True
            elif i==chr(range(48,57)):
                has_digit==True
            elif i==chr(range(33,47)):
                has_symbol==True
        if has_upper == True and has_lower ==True and has_digit ==True and has_symbol == True:
            valid=True
    return pw
def create_new_user(user_db) :
    username = input("enter a username")
    password=generate_password(12)
    print(f"password is {password}")
    user_db[username] = password
def login(user_db):
    auth_status=False
    username = input("enter your username")
    password=input("enter your password")
    if username in user_db:
        if user_db[username] == password:
            auth_status=True
            print("login successful")
        else:
            print("login unseccessful.")
    else:
        print(f"user {username} doesnt exist")
    return auth_status
def view_data(user_db):
    print(user_db)
user_db={}
def view_menu():
    print("1:create a new user")
    print("2:login")
    print("3:view data")
    print("4:exit program")
    x=input("what choice do u want")
    if x==1:
        create_new_user()
    elif x==2:
        login(user_db)
    elif x==3:
        view_data(user_db)
    elif x ==4:
        break
    
print(generate_password(12))
while True:
    logged_in=login(user_db)
    if not logged_in:
        print(" login fail")

