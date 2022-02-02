import random
class Dice:
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
    
    def roll(self):
        return random.randint(1,6)
class Bank:
    def __init__(self, balance, owner_name):
        self.balance = balance
        self.owner_name = owner_name
    
    def withdraw(self, my_money):
        self.balance -= my_money

    def deposit(self, new_money):
        self.balance += new_money

def greet():
    print("====================================")
    print("Welcome to this dice roll simulator!")
    print("====================================\n")

def main():

    # Initialize variables and die
    my_bank_account = Bank(1000, "Max Chai")
    sum_of_outcomes = 0
    die = Dice()

    greet()
    
    # User input + simulator
    desired_number_of_rolls = int(input("How many times would you like to roll the die? "))
    
    for i in range(desired_number_of_rolls):
        outcome = die.roll()
        sum_of_outcomes += die.roll()
        my_bank_account.withdraw(3.6)
        my_bank_account.deposit(outcome)


    # Results
    average = round(sum_of_outcomes / desired_number_of_rolls, 1)
    my_bank_account_balance = my_bank_account.balance
    net_proceeds = my_bank_account_balance - 1000
    print("The average number was: {}".format(str(average)))
    print()
    print("The average won/lost is: {}".format(round(net_proceeds / desired_number_of_rolls, 2)))

    

main()