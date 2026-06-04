import random

def play_game():
    print("🎮 Welcome to Number Guessing Game")
    print("Choose Difficulty Level:")
    print("1. Easy (1 to 20)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    choice = input("Enter level (1/2/3): ")

    if choice == "1":
        max_num = 20
        attempts = 8
    elif choice == "2":
        max_num = 50
        attempts = 6
    elif choice == "3":
        max_num = 100
        attempts = 5
    else:
        print("Invalid choice! Default = Easy")
        max_num = 20
        attempts = 8

    secret_number = random.randint(1, max_num)

    print(f"\nI picked a number between 1 and {max_num}")
    print(f"You have {attempts} attempts\n")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("🎉 Correct! You won!")
            break
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        attempts -= 1
        print(f"Attempts left: {attempts}")

        # Hint system
        if attempts > 0:
            if abs(secret_number - guess) <= 5:
                print("🔥 Very close!")
            else:
                print("❄️ Far away!")

    if attempts == 0:
        print(f"\n😢 Game Over! The number was {secret_number}")

play_game()