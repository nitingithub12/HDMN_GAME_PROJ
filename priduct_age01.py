def predict_age():
    print("Welcome to the Age Prediction Game!")
    print("Answer a few questions, and I'll try to guess your age.")

    # Ask the user some questions to predict their age
    question1 = input("What is the remainder when you divide your age by 3? ")
    question2 = input("What is the remainder when you divide your age by 5? ")
    question3 = input("What is the remainder when you divide your age by 7? ")

    # Convert answers to integers
    try:
        remainder1 = int(question1)
        remainder2 = int(question2)
        remainder3 = int(question3)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Calculate the predicted age
    predicted_age = (remainder1 * 70 + remainder2 * 21 + remainder3 * 15) % 105

    print(f"Based on your answers, I predict that you are approximately {predicted_age} years old!")

if __name__ == "__main__":
    predict_age()
