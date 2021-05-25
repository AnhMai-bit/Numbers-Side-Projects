def fibo_eq(n):
    
    if n <0:
        print('Please pick number larger than 0')
    
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    
    # Second Fibonacci number is 1 
    elif n == 1:
        return 1
    
    # The rest follows the formula
    else:
        return fibo_eq(n-1) + fibo_eq(n-2)
        # not (n-1) + (n-2)

fibo_eq(9)
