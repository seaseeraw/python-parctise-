import random

# Step 1: Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

# Step 2: Keep asking until the player guesses right
while True:
    guess = input("Enter your guess: ")
    attempts += 1

    # Step 3: Make sure input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    # Step 4: Give hints
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}. You guessed it in {attempts} tries.")
        break
