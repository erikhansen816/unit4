#Erik Hansen
#10/26/17
#recursionFactorial.py - A recursive version of the factorial function

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1))
    
print(factorial(4))

