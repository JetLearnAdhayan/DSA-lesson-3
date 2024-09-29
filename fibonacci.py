def fb(n):
    #base case
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    else:
        return fb(n-1) + fb(n-2)
    

n = int(input("Enter a number : "))  
print("Fibonacci of" , n, "is",) 
for i in range (0,n):
    print(fb(i), end = "  ")
      
    