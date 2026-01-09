# r=1 
# b=2
# g=3
# print(f"ur sushi cost ${3*r+b*5+g*4}.")
# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))



score = int(input("what is students grade? "))
if score >= 75:
    grade = "A"
elif score < 75 and score >= 60:
    grade ="B"
elif score > 50 and score <= 59:
    grade="C"
elif score < 50:
    grade="F"
print(f"grade is {grade}")