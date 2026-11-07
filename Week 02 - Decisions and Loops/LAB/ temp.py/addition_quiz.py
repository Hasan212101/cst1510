# addition_quiz
'''import random

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    answer = int(input(f"What is {num1} + {num2}? "))

    if answer == num1 + num2:
        print("Correct, well done!")
        break
    else:
        print(f"Incorrect. The answer is {num1 + num2}.")'''

import random
while True:
    number1 = random.randint(1,10)
    number2 = random.randint(1,20)
    answer = int(input(f"what is {number1} - {number2}? "))
    if answer == number1 - number2:
        print("Correct, well done")
        break
else:
    print("incorrect, Try again")