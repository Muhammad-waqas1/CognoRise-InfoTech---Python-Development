import random

def roll_dice():
    try:
        sides = int(input("Enter the number of sides on the dice: "))
        rolls = int(input("Enter the number of rolls: "))
        
        if sides < 2 or rolls < 1:
            raise ValueError("Number of sides should be at least 2 and number of rolls should be at least 1.")
        
        results = [random.randint(1, sides) for _ in range(rolls)]
        print(f"Dice roll results: {results}")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    roll_dice()