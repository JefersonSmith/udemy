number = 7
user_input = input("Enter 'y' if you wold like to play: ")

if user_input in ("Y", "y"):
    user_numer = int(input("Guess our number: "))
    if user_numer == number:
        print("You guesses correctly!")
    elif abs(number - user_numer) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")