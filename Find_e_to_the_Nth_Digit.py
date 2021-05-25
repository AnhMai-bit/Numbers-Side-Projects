from math import e

def e_equation(n):
    if n<= 0:
        return 'Please pick number larger than 0'
    else:
        return round(e,n) 

e_equation(4)
