n1= 100
guess=1
print("You have only 9 guess left")
while guess<=9:
    number=int(input("Enter your number\n"))
    if number>100:
        print("You have entered a greater number")
    elif number<100:
        print("You have entered a lesser number ") 
    else:
        print("Congratulation yuo have won")
        break
    print(guess,"Chances you have taken to guess the number")   
    guess=guess+1

    if guess>9:
        print("The game is over ")    