number = 7

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == "n":
        break

    user_numer = int(input("Guess our number: "))
    if user_numer == number:
        print("You guesses correctly!")
    elif abs(number - user_numer) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

