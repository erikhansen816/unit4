#Erik Hansen
#10/26/17
#recursionFibonacci.py - A recursive version of the fibonacci function

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
