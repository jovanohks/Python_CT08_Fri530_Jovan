"""
============================================================
Q1. Quiz Auto-Marker
============================================================
You are building an auto-marker system for a multiple-choice quiz.
The program must compare a student's answers with the answer key.
It should calculate the score, identify which questions were wrong, and assign a grade.

- Write 3 functions:
    1) score_quiz(key, ans)
    2) wrong_questions(key, ans)
    3) grade(score, total)
- Do not change the function names or parameters.
- After writing your functions, uncomment the test code at the bottom to test.

============================================================
"""

# ============================================================
# Step 1: Write function score_quiz(key, ans)
# ============================================================
# - key and ans are lists of equal length
# - Compare answers at the same position
# - Return total number of correct answers
# ============================================================
answer_key = ["B","D","C","A","C","B","C","A","B","A"]
student_ans = ["B","D","C","A","C","B","C","A","B","A"]
def score_quiz(key,ans):
    correct =0
    if not len(key) == len(ans):
        return False #if length of answer key and student answer is different, return fase
    for question in range(len(answer_key)):
        if key[question] == ans[question]: 
            correct +=1 
    return correct
print(score_quiz(answer_key,student_ans))

# ============================================================
# Step 2: Write function wrong_questions(key, ans)
# ============================================================
# - Return a list of question numbers (starting from 1) that are wrong
# - If all answers are correct, return an empty list
# ============================================================
def wrong_questions(key,ans):
    wrong=[]
    if not len(key) ==len(ans):
        return False
    for question in range(len(key)):
        if not ans[question]==key[question]:
            wrong.append(question+1) #append question number to list and add one since index start from 0
    return wrong
print(wrong_questions(answer_key,student_ans))
    


# ============================================================
# Step 3: Write function grade(score, total)
# ============================================================
# - Compute percentage = (score / total) * 100
# - Return:
#     "A" if percentage >= 80
#     "B" if percentage >= 70
#     "C" if percentage >= 60
#     "D" otherwise
# ============================================================
def grade(score,total):
    percentage=(score/total)*100
    if percentage>=80:
        return "A"
    elif percentage >=70 and percentage <80:
        return "B"
    elif percentage >=60 and percentage <70:
        return "C"
    else:
        return "D"


# ============================================================
# Step 4: Main Code Testing
# ============================================================
# Uncomment after writing your functions

score = score_quiz(answer_key, student_ans)
wrong = wrong_questions(answer_key, student_ans)
final_grade = grade(score, len(answer_key))

print("Score:", score)
print("Wrong Questions:", wrong)
print("Grade:", final_grade)