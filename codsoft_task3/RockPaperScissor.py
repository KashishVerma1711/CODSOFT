import random
def getUserChoice():
    while True:
        userChoice = input("Choose rock, paper, or scissors: ").strip().lower()
        if userChoice in ['rock', 'paper', 'scissors']:
            return userChoice
        else:
            print("Invalid choice!!! Please enter a valid choice.")

def getComputerChoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'scissors' and computerChoice == 'paper') or \
         (userChoice == 'paper' and computerChoice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def print_choices(userChoice, computerChoice):
    print(f"You chose: {userChoice}")
    print(f"Computer chose: {computerChoice}")

def rockPapperScissor():
    userScore = 0
    computerScore = 0
    while True:
        print("\nRock, Paper, Scissors - Game Start!")
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print_choices(userChoice, computerChoice)
        result = winner(userChoice, computerChoice)
        print(result)
        
        if 'win' in result:
            userScore += 1
        elif 'lose' in result:
            computerScore += 1
        
        print(f"\nScore - You: {userScore}, Computer: {computerScore}")
        
        playAgain = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if playAgain != 'yes':
            print("Thanks for playing!")
            break
rockPapperScissor()
