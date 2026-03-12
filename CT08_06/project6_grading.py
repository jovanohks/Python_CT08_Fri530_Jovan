# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}
def grade_all_students(key,ans):
    quiz_scores ={}

    for x,y in ans.items():
        score=0
        for i in range(len(key)):
            if key[i] == y[i]:
                score +=1
        quiz_scores[x] = score
    return quiz_scores
def calculate_average_score(score):
    t=0
    for y in score.values():
        t+=y
    avg_score =t/len(score)
    return avg_score
def find_highest_scorer(score):
    h = 0
    hs=[]
    for x in score.values():
        if x > h:
            h=x
    for x,y in score.items():
        if y==h:
            hs.append(x)
    return hs
def display_all_results(score):
    for x,y in score.items():
        print(f"{x.capitalize()}: {y}")
def menu_system():
    while True:
        print(f"menu system")
        print(f"1. grade all students")
        print(f"2. find class average")
        print(f"3. find highest scorer(s)")
        print(f"4. display all scores")
        print(f"5. exit")
        x=input("input number from 1-5: ")
        print(f"")
        a=["1","2","3","4","5"]
        if not x in a:
            print("not accepted input type again")
        elif x =="1":
            print(grade_all_students(answer_key,student_answers))
        elif x =="2":
            print(calculate_average_score(grade_all_students(answer_key,student_answers)))
        elif x =="3":
            print(find_highest_scorer(grade_all_students(answer_key,student_answers)))
        elif x =="4":
            display_all_results(grade_all_students(answer_key,student_answers))
        else:
            break
# x=grade_all_students(answer_key,student_answers)
# print(grade_all_students(answer_key,student_answers))
# print(calculate_average_score(x))
# print(find_highest_scorer(x))
# display_all_results(x)
menu_system()