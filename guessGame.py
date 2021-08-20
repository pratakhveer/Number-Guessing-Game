import random
print("Number Guessing Game ")
print("guess a number between 1-9")
count = 0
while count != 5:
    guess = input("Enter your guess:-")
    count = count+1
    randomNumber = random.randint(1, 9)
    if (guess == randomNumber):
        print("Congratulations Your Guess Is Correct")
    if (int(guess) > randomNumber):
        print("your guess was too big, guess a number smaller than", guess)
    if (int(guess) < randomNumber):
        print("Your guess was too low, guess a bigger number than", guess)

    if(count == 5):
        print("You have ran out of guesses :(")

        break
