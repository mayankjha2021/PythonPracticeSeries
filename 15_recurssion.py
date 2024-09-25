# factorial(1) =1
# factorial(2)=2*1
# factorial(3)=3*2*1

# similarly factorial(n) =n*factorial(n-1)

n=int(input('Enter the number you want to get as factorial: '))

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

k= factorial(n)
print(k)