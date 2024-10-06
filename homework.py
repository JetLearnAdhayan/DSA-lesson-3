def multiply(base, power):
    
    if power == 0:
        return 1
    
    else:
        return base * multiply(base, power - 1)


result = multiply(5, 3)
print(result)  