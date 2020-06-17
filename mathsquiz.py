import random
import sqlite3

operators = ["/","+","*","-"]
#Dictionary of functions used to calculate the answer to the randomly generated question
operator_functions = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b, 
    '/': lambda a, b: a / b,
}

print("Welcome to my maths quiz")
name = input("What is your name? ")


def question():
    #checks if the users input is equal to the answer
    def check_answer(answer, score):
        if answer == correct_answer:
            print ("CORRECT")
            score = score + 1
        else:
            print("INCORRECT")
        return score

    score = 0
    #generates the random intergers and opperators to use in the question
    var1 = random.randint(2, 10)
    var2 = random.randint(2, 10)
    picked_operator = random.choice (operators)

    #If the question uses dividing this generates a multiple of the first variable number to use in the question so the answer is always integer
    if picked_operator == "/":
        multiples_range = var1 * 10
        start_range = random.randrange(multiples_range)
        end_range = start_range + var1   
        multiple_var = [n for n in range(start_range, end_range) if n % (var1) == 0]
        print (f"{multiple_var[0]}{picked_operator}{var1}")
        correct_answer = operator_functions[picked_operator]( multiple_var[0], var1)
    else:
        print (f"{var1}{picked_operator}{var2}")
        correct_answer = operator_functions[picked_operator](var1, var2)   
        

    #Asks for answer with error handling
    valid_answer = False
    while not valid_answer:
            try:
                answer = int(input("What is the answer? " ))
                if isinstance(answer,(int)) == True:
                    valid_answer = True
            except:
                valid_answer = False
                print ("Please enter a int")
                      
    
    
    #Edits users score
    score = check_answer(answer, score)
    print (f"You current score is: {score}")   
            
                
     

question()
