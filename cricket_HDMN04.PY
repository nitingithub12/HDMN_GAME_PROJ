import random

def toss():
    """Function to simulate a coin toss"""
    return random.choice(["Heads", "Tails"])

def batting():
    """Function to simulate batting"""
    runs = 0
    while True:
        bowl = random.randint(0, 6)
        guess = int(input("Enter your guess (0-6): "))
        if guess < 0 or guess > 6:
            print("Invalid input! Please enter a number between 0 and 6.")
            continue
        print("You guessed:", guess)
        print("Bowler bowled:", bowl)
        if guess == bowl:
            print("Out! Your total runs:", runs)
            break
        else:
            runs += bowl
            print("You scored", bowl, "runs in this ball.")
            print("Your total runs:", runs)

def bowling():
    """Function to simulate bowling"""
    runs = 0
    while True:
        bowl = random.randint(0, 6)
        guess = int(input("Enter your guess (0-6): "))
        if guess < 0 or guess > 6:
            print("Invalid input! Please enter a number between 0 and 6.")
            continue
        print("You guessed:", guess)
        print("Batsman played:", bowl)
        if guess == bowl:
            print("Out! Batsman's total runs:", runs)
            break
        else:
            runs += bowl
            print("Batsman scored", bowl, "runs in this ball.")
            print("Batsman's total runs:", runs)

def main():
    print("Welcome to the Cricket Game!")
    choice = input("Enter '1' to bat or '2' to bowl: ")
    if choice == '1':
        print("You won the toss and chose to bat.")
        toss_result = toss()
        print("Toss result:", toss_result)
        if toss_result == "Heads":
            print("You won the toss!")
            print("Start batting!")
            batting()
        else:
            print("You lost the toss!")
            print("Start bowling!")
            bowling()
    elif choice == '2':
        print("You won the toss and chose to bowl.")
        toss_result = toss()
        print("Toss result:", toss_result)
        if toss_result == "Heads":
            print("You won the toss!")
            print("Start bowling!")
            bowling()
        else:
            print("You lost the toss!")
            print("Start batting!")
            batting()
    else:
        print("Invalid choice! Please enter '1' to bat or '2' to bowl.")

if __name__ == "__main__":
    main()
