#Python quiz game
import time
questions=("1. What is the maximum possible length of an identifier? :",
           "2. Which of the following is invalid?",
           "3. Which of the following is an invalid variable?",
           "4. Which of the following cannot be a variable?",
           "5. Which is the invalid datatype in python")
options=(("A. 31 characters","B. 310 characters","C. 255 characters","D.No limit, recommend  79 characters "),
         ("A. _a=1","B. __a = 1","C. A_a = 1","D. 1 = _a "),
         ("A. My_string_1","B. 1st_string","C. Foo","D. _a"),
         ("A. __init__","B. on ","C. in","D. it"),
         ("A. double","B. int","C. float","D. decimal.Decimal"))
answers=("D","D","B","C","A")
explanations=(("The question asks for the maximum possible length of an identifier,\nNo limit, recommend  79 characters in python ."),
              ("The given statement 1 = _a is invalid because in Python, variable names cannot start with a number.\n They must start with a letter or an underscore.\n Therefore, 1 = _a violates this rule and is not a valid assignment statement."),
              ("The variable 1st_string is invalid because it starts with a number,\n which is not allowed in variable names. \nVariable names in most programming languages must start with a letter or an underscore."),
              ("The word in cannot be a variable because it is a reserved keyword in many programming languages, including Python.\n Reserved keywords are predefined and have special meanings in the language,\n so they cannot be used as variable names."),
              ("Double is not a valid data type"))
guesses=[]
score=0
question_num=0
ex="Explanation below :"
print("-----------------------------------------------------")
print(" Welcome to quiz ")
for question in questions:
    print("***********************************************")
    print(question)
    for option in options[question_num]: 
        print(option)
    guess=input(f"Enter answer (A,B,C,D) for the question : ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score +=1
        print("Correct !")
        print(ex,explanations[question_num])
    else: 
        print("Incorrect !")
        print(f"Correct answer is: {answers[question_num]}")
        print(ex, explanations[question_num])
    question_num+=1
    time.sleep(5)
print("-----------------------")
print("       RESULTS         ")
print("-----------------------")
print("Correct answers")
for a in answers:
    print(a, end=" ")
print()
print("Your Guesses")
for g in guesses:
    print(g, end=" ")
print()
score=int((score/len(questions))*100)
print("*****************************")
print(f" Your score is :{score}")
print("*****************************")
