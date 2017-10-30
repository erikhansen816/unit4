#Erik Hansen
#10/30/2017
#quiz4.py

def csia():
    for i in range(1,6):
        print('computer science is awesome')
    
def average(num1,num2,num3):
    return ((num1+num2+num3)/3)

def lastLetter(word):
    total = 0
    for ch in word:
        total = total + 1
    if total == len(word):
        print(ch)
    
def same(x,y):
    if x == y:
        return True
    else:
        return False
csia()
print(average(2,4,6))
lastLetter('Lit')
print(same(2*3,7-1))
