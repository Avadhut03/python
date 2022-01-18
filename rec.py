"""def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac=fac*(i+1)
    return fac
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)    
     
n=int(input("Enter a number:\n"))    
print(factorial_iterative(n))       
print("recursive method",factorial_recursive(n))  """


# Quiz
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))        
   
num=int(input("Enter a number:\n"))
for i in range(num):
    print(fib (i+1), end="")

