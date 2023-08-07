from decimal import *

#Specify the calculation precision as 500 digits
getcontext().prec = 500 

def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)

e = Decimal(0)
n = 0

while True:
    term = Decimal(1) / Decimal(fact(n))
    if term < Decimal(10) ** -500:
        break
    e += term
    n += 1

print(e)
