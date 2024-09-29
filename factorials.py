def factorial(n):
    #base case or stop value
    if n == 1 or n == 0:
        return 1 
    #recursive case 
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number : "))

print("Factorial of ",n,"is",factorial(n))