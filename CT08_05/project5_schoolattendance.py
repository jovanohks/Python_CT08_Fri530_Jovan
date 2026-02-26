def take_attendance(listt):

    for someone,b in listt.items():

        while 1==1:
            x=input(f"Is {someone} in school? y/n")
            if x=="y":
                b.append(True)
                break
            elif x=="n":
                b.append(False)
                break
            else:
                print(f"only accept y or n,try again.")
    return listt
def check_attendance(listt,name):
    if name in listt.items():
        days_present=0
        for a in listt[name]:
            if a==True:
                
                days_present+=1
        attendance_percentage=days_present/len(listt)
        return attendance_percentage
    else:
        print(f"not in list")
        attendance_percentage=False
        return attendance_percentage
def notify_low_attendance(listt,threshold):
    for i in something:
        if check_attendance(listt,i) < threshold:
            print(f"student {i} has low attendance")
something={
    "John":[],
    "Johnny":[],
    "Tom":[],
    "Alice":[],
    "Bob":[],
    "Alex":[],
 

take_attendance(something)
notify_low_attendance(something,50)
   "Joshua":[]
}
#     e True:
#     take_attendance(something)
    notify_low_attendance(something,50)
