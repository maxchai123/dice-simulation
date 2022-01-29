import random
class Dice:
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
    
    def roll(self):
        return random.randint(1,6)

def greet():
    print("====================================")
    print("Welcome to this dice roll simulator!")
    print("====================================\n")

def main():

    # Initialize variables and die
    sum_of_outcomes = 0
    die = Dice()

    greet()
    
    # User input + simulator
    desired_number_of_rolls = int(input("How many times would you like to roll the die? "))
    
    for i in range(desired_number_of_rolls):
        sum_of_outcomes += die.roll()

    # Results
    average = round(sum_of_outcomes / desired_number_of_rolls, 1)
    print("The average number was: {}".format(str(average)))
    

main()