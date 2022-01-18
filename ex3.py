  # exercise 2- Faulty calculator

print("Enter your first number")
n1=int(input())
print("Enter Your Second Number")
n2=int(input())
print("Enter the arithmatic operator symbol which you want to do")
opt=(input())
if opt== "+":
    if n1==45 and n2==3:
        print("Your answer is 555")
    else:
        print("Your Answer Is", n1 + n2)
if opt=="*":
    if n1==56 and n2==45:
        print("Your answer is 6447")
    else:
        print("Your Answer Is", n1 * n2)
if opt=="-":
    if n1==87 and n2==34:
        print("Your answer is 233")
    else:
        print("Your Answer Is", n1 - n2)
if opt=="/":
    if n1==98 and n2==28:
        print("Your answer is 46")
    else:
        print("Your Answer Is", n1 / n2)                       
