n1 =90
guesses=1
print("You have only 9 chances for guess ")
while(guesses<=9):
    number=int(input("Enter your number\n"))
    if number<90:
        print("You have entered lesser number")
    elif number>90:
        print("You have entered a greater number")  
    else:
        print("Congratulations you have won")
        break
    print(guesses,"no.of guesses you have taken")
    guesses=guesses+1

    if guesses>9:
        print("Game Over")

