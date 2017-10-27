#Erik Hansen
#10/4/2017
#multiply.py - ask addition problems until user gets 5

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is ' + str(num1) + 'x' + str(num2) + '? '
    answer = int(input(question))
    if num1*num2 == answer:
        print('Correct')
        numCorrect += 1
    else:
        print('WRONG YOU DUMB IMBECILE! The real answer was', num1+num2)
complement()

def complement():
    n = randint(1,4)
    if n == 1:
        print('Great Job!')
    elif n == 2:
        print('Good job!')
    elif n == 3:
        print("You aren't a complete disappointment")
    else:
        print("You don't suck at math")
    numcorrect = 0
