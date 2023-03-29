number = 7
user_input = input("Enter 'y' if you wold like to play: ")

if user_input == "y":
    user_numer = int(input("Guess our number: "))
    if user_numer == number:
        print("You guesses correctly!")
    else:
        print("Sorry, it's wrong!")