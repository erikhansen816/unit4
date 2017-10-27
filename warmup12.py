#Erik Hansen
#10/27/2017
#warmup12.py greatest common factor

def GCF(num1,num2):
    n = min(num1,num2)
    for i in range(n,0,-1):
        if num1%i == 0 and num2%i == 0:
            return i

print(GCF(14,14))
