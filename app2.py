import random

def hand_cricket():
    print("Welcome to Hand Cricket!")
    user_score, computer_score = 0, 0

    # Toss to decide who bats first
    toss = input("Choose heads or tails: ").lower()
    toss_result = random.choice(["heads", "tails"])
    if toss == toss_result:
        choice = input("You won the toss! Choose to bat or bowl: ").lower()
        user_batting = choice == "bat"
    else:
        print("Computer won the toss and will choose to bat or bowl.")
        user_batting = random.choice([True, False])

    def play_inning(is_user_batting):
        score = 0
        while True:
            user_input = int(input("Enter your run (1-6): "))
            computer_input = random.randint(1, 6)
            print(f"Computer chose: {computer_input}")
            
            if user_input == computer_input:
                print("Out!")
                break
            else:
                score += user_input if is_user_batting else computer_input
                print(f"Score: {score}")

        return score

    # First inning
    if user_batting:
        print("\nYou are batting first.")
        user_score = play_inning(is_user_batting=True)
        print(f"Your inning ends with a score of {user_score}")
        print("\nComputer is now batting.")
        computer_score = play_inning(is_user_batting=False)
    else:
        print("\nComputer is batting first.")
        computer_score = play_inning(is_user_batting=False)
        print(f"Computer's inning ends with a score of {computer_score}")
        print("\nYou are now batting.")
        user_score = play_inning(is_user_batting=True)

    # Decide the winner
    print(f"\nFinal Scores: You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the match!")
    elif user_score < computer_score:
        print("Computer wins the match. Better luck next time!")
    else:
        print("It's a tie!")

# Run the game
hand_cricket()
