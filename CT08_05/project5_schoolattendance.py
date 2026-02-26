def take_attendance(listt):

    for someone,b in listt.items():

        while True:
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
    if name in listt:
        days_present=0
        for a in listt[name]:
            if a==True:
                days_present+=1
        attendance_percentage=(days_present/len(listt[name]))*100
        
        return attendance_percentage
    else:
        print(f"not in list")
        attendance_percentage=False
        return attendance_percentage
def notify_low_attendance(listt,threshold):
    for i in listt:
        if check_attendance(listt,i) < threshold:
            print(f"student {i} has low attendance")
def view_attendance(dictionary_name):
    for a,b in dictionary_name.items():
        present=0
        for x in range(0,len(b)):
            if b[x] == True:
                present+=1
        print(f"{a}'s precentage: {(((present)/len(b))*100)}%")



something={
    "John":[],
    "Johnny":[],
    "Tom":[],
    "Alice":[],
    "Bob":[],
    "Alex":[],
   "Joshua":[]
}
while True:
    print(f"1.Take attendance")
    print(f"2:Caculate Attendance percentage")
    print(f"3:Notify low attendance")
    print(f"4:view attendance")
    print(f"5:exit program")
    x=input("enter a choice(1,2,3,4,5):")
    if x == "1":
        take_attendance(something)
    elif x== "2":
        name=input("enter student name: ")
        if name in something:
            print(f"{name} attendence percentage is {check_attendance(something,name):.0f}%.")
    elif x=="3":
        y=int(input("threshold for low attendance "))
        notify_low_attendance(something,y)
    elif x=="4":
        view_attendance(something)
    elif x=="5":
        break
    else:
        print("Invalid input")

# Build an interactive menu to access the
# attendance system's features.​
# Display a menu with the following
# options:​
# 1: Take Attendance​
# 2: Calculate Attendance Percentage for a Student​
# 3: Notify Low Attendance​
# 4: Exit Program​

# Based on the user’s choice:​
# Call the respective function with the necessary inputs.​
# Display the results of the chosen action.​

# Challenge:​
# Add a view_attendance() function. ​
# Params:​
# attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​
# Return: none