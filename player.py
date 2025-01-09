import random
from board import Board

class Player: 
    # Player Name: 
    name = "Bob"

    # Cash value: 
    cash = 1500

    # Board location index: 
    location = 0

    # Property List: 
    property = []

    # Roll List to check if you rolled double: 
    roll_list = []

    roll = 0

    # Turn boolean: 
    is_turn = False 

    # In jail boolean: 
    in_jail = True

    # Number of turns in jail: 
    turns_in_jail = 0

    # Constructor: 
    def __init__(self, name):
        self.name = name 

    # Roll the dice: 
    def DieRoll(self):
        self.roll_list = [random.randint(1, 6), random.randint(1, 6)]
        # self.roll_list = [1,1] # Used to test doubles functionality.
        self.roll = self.roll_list[0] + self.roll_list[1]
        print(f"You rolled a {self.roll}: ({self.roll_list[1]}, {self.roll_list[0]})")

    #Check if you rolled doubles: 
    def IsDouble(self): 
        if self.roll_list[1] == self.roll_list[0]:
            return True
        else: 
            return False
    
    # Advance board spaces: 
    def AdvancePos(self):
        for i in range(self.roll):
            self.location += 1 
            if self.location > 39: 
                self.location = 0
                print("You passed GO! Collect $200!")
                self.cash += 200
        self.DisplayLocation()
        if self.location in Board.property_index:
            purchase = input("Buy property? (y/n) ")
            if purchase == "y":
                # Add property to list: 
                self.property.append(Board.spaces[self.location])
                # Remove property from property index:
                Board.property_index.pop(Board.property_index.index(self.location))

    def DisplayLocation(self):
        print(f"You landed on {Board.spaces[self.location]}.")

        
    def DisplayAttributes(self):
        print(f"\nYou have ${self.cash}.")
        print("You currently own:")
        for i in self.property: 
            print(i)

    