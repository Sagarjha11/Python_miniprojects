import random
num = 1
print("Welcome to the number guessing game. We have a number that need to be guessed. You have 10 chances")
print("The secret number is between 1 to 50")
no_of_attempt = int(input("How many attempts you want ? "))
secret_number = random.randint(1,50)
attempt = no_of_attempt
is_guess_correct = False
while num <= no_of_attempt:
    print(f"you have {attempt} attempt remaining.")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number :
        print("Congrats, Your guess is correct!!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong, Try {higher_or_lower} number")

    num += 1
    attempt -= 1 
    
if is_guess_correct == False :
    print("Bad luck !! You exhausted all your attempt, You couldn't guess the Number ")
print(f"The secret number was {secret_number}. Game end!!")


