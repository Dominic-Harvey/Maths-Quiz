import random
import sys
import mathsquizSQLite

operators = ["/","+","*","-"]
#Dictionary of functions used to calculate the answer to the randomly generated question
operator_functions = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b, 
    '/': lambda a, b: a / b,
}

#generates the random intergers and opperators to use in the question
def question_gen():
    first_number = random.randint(2, 10)
    second_number = random.randint(2, 10)
    picked_operator = random.choice (operators)

    #If the question uses dividing this generates a multiple of the first variable number to use in the question so the answer is always integer
    if picked_operator == "/":
        multiples_range = first_number * 10
        start_range = random.randrange(multiples_range)
        end_range = start_range + first_number   
        multiple_var = [n for n in range(start_range, end_range) if n % (first_number) == 0]
        print (f"{multiple_var[0]}{picked_operator}{first_number}")
        correct_answer = operator_functions[picked_operator]( multiple_var[0], first_number)
    else:
        print (f"{first_number}{picked_operator}{second_number}")
        correct_answer = operator_functions[picked_operator](first_number, second_number)
    return correct_answer    

#Asks for answer with error handling
def ask_question():
    valid_answer = False
    while not valid_answer:
            try:
                answer = int(input("What is the answer? " ))
                if isinstance(answer,(int)) == True:
                    valid_answer = True
                    return answer
            except:
                valid_answer = False
                print ("Please enter a int")

#checks if the users input is equal to the answer
def update_score(correct_answer, answer):
    if answer == correct_answer:
        print ("CORRECT")
        correct_score = 1
    else:
        print("INCORRECT")
        correct_score = 0
    return correct_score

print("Welcome to my maths quiz")
name = input("What is your name? ")
number_of_questions = int(input("How many questions would you like to answer?"))
current_score = 0

for _ in range(number_of_questions):
    correct_answer = question_gen()
    answer = ask_question()
    score_to_add = update_score(correct_answer, answer)
    current_score = current_score + score_to_add
    print (f"You current score is: {current_score}")

'''
try:
    mathsquizSQLite.database(name, current_score)
    print (f"Your final score of {current_score}/{number_of_questions} and Name have been saved in the database")
except:
    e = sys.exc_info()[0]
    print ("Error adding entry in database", e)
'''
