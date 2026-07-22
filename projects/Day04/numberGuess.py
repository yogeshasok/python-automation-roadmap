import random

def number_guess():
    print("-" * 45)
    print("************Number Guess*****************")
    print("-" * 45)
    
    random_number = random.randint(1, 100)
    print(f"Random number is {random_number}")
    print("I am thinking of a number between 1 and 100. Guess it within 5 attempts.")
    
    attempts = 5
    
    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        user_number = input("Enter your guess: ")
        
        if not user_number.isdigit():
            print("Enter only digits!")
            attempts -= 1
            continue  # Skips the rest of the loop to prevent int() conversion error
            
        user_guess = int(user_number)
        
        # Check for out-of-bounds numbers first
        if user_guess < 1 or user_guess > 100:
            print("Enter a number between 1 and 100 only!")
            attempts -= 1
            continue

        match user_guess:
            case _ if user_guess == random_number:
                print(f"Congratulations! You successfully guessed the number {random_number}!")
                return  # Exits the function since the game is won
            case _ if user_guess < random_number:
                print("Too Low! Try a higher number.")
                attempts -= 1
            case _ if user_guess > random_number:
                print("Too High! Try a lower number.")
                attempts -= 1

    print(f"\nGame Over! You ran out of attempts. The number was {random_number}.")

number_guess()
