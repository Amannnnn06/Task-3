import random

def roll_dice():
    die1 = random.randint(1, 6)  
    die2 = random.randint(1, 6) 
    return die1, die2

def main():
    print("Welcome to the Dice Roller!")
    
    while True:
        input("Press Enter to roll the dice...")
        die1, die2 = roll_dice()
        print(f"You rolled a {die1} and a {die2}.")
        
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
