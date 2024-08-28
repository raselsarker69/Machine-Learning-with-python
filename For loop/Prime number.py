def FindPrimeNumber(n):
    if n <= 1:
        return 'not prime' 
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'not prime'  
    return 'Prime' 

num = int(input('Enter a number: '))
result = FindPrimeNumber(num)
print(result)

    