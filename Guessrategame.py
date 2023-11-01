import random

def interest_game():
    principal = random.randint(1000, 10000)
    rate = random.uniform(1, 10)
    time = random.randint(1, 10)

    correct_interest = principal * (1 + rate/100) ** time

    print(f"Welcome to the Interest Rate Guessing Game!")
    print(f"You have $ {principal} and invest it at {rate}% interest rate for {time} years.")
    print(f"Can you guess the final amount after {time} years?")

    guess = float(input("Enter your guess: "))

    if guess == correct_interest:
        print(f"Congratulations! You guessed it right. The correct answer is {correct_interest:.2f}")
    else:
        print(f"Sorry, your guess is incorrect. The correct answer is {correct_interest:.2f}")

if __name__ == "__main__":
    interest_game()


