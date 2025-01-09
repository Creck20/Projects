""" 
The following is a monopoly simulator using the command line as an interface.
"""
import random
import csv

from board import Board
from player import Player

print("Welcome to Monopoly!\n")

# Instantiate Class Objects: 
board = Board()
player1 = Player("Bob")
player2 = Player("Sarah")

# Main Game Loop: 
done = False
odd_even = 0

while not done: 
    # Switching turns mechanic
    if odd_even % 2 == 0: 
        player1.is_turn = True
        player2.is_turn = False
    else: 
        player1.is_turn = False
        player2.is_turn = True
    odd_even += 1 

    if player1.is_turn: 
        # If the player is in jail: Roll the dice ... 
        if player1.in_jail: 
            print(f"\nIt's {player1.name}'s turn")
            player1.turns_in_jail += 1
            print(f"You are in jail...({player1.turns_in_jail} turn(s))")
            player1.DieRoll()
            #The player can leave free if they role doubles ...
            if player1.IsDouble():
                print("You rolled doubles! Get out of jail!")
                player1.in_jail = False
                player1.turns_in_jail = 0
                player1.AdvancePos()
                
             # The player can choose to pay $50 on a turn. 
            if (player1.turns_in_jail != 3) and (not player1.IsDouble()):
                pay = input("Pay $50? (y/n)")
                if pay == "y":
                    player1.cash -= 50
                    player1.in_jail = False
                    player1.turns_in_jail = 0
                    player1.AdvancePos()
                    
            # After three turns, the player must pay $50 ...
            if (player1.turns_in_jail == 3) and (not player1.IsDouble()):
                print("You must pay $50")
                player1.in_jail = False
                player1.turns_in_jail = 0
                player1.cash -= 50
                player1.AdvancePos()
                
        
        # If player not in jail: 
        else: 
            # Player can roll doubles three times before going to jail: 
            print(f"\nIt's {player1.name}'s turn")
            player1.DieRoll()
            player1.AdvancePos()
            player1.DisplayAttributes()
            
            if player1.IsDouble():
                print("\nYou rolled doubles!")
                player1.DieRoll()
                player1.AdvancePos()
                player1.DisplayAttributes()
                
                if player1.IsDouble():
                    print("\nYou rolled doubles! (2)")
                    player1.DieRoll()
                    player1.AdvancePos()
                    player1.DisplayAttributes()
                    
                    if player1.IsDouble():
                        print("\nYou rolled doubles! (3) ...Go to jail")
                        player1.location = 10
                        player1.in_jail = True
                        print(board.spaces[player1.location])
            

    elif player2.is_turn:
        # If the player is in jail: Roll the dice ... 
        if player2.in_jail: 
            print(f"\nIt's {player2.name}'s turn")
            player2.turns_in_jail += 1
            print(f"You are in jail...({player2.turns_in_jail} turn(s))")
            player2.DieRoll()
            #The player can leave free if they role doubles ...
            if player2.IsDouble():
                print("You rolled doubles! Get out of jail!")
                player2.in_jail = False
                player2.turns_in_jail = 0
                player2.AdvancePos()
                
            # The player can choose to pay $50 on a turn. 
            if (player2.turns_in_jail != 3) and (not player2.IsDouble()):
                pay = input("Pay $50? (y/n)")
                if pay == "y":
                    player2.cash -= 50
                    player2.in_jail = False
                    player2.turns_in_jail = 0
                    player2.AdvancePos()
                    
            # After three turns, the player must pay $50 ...
            if (player2.turns_in_jail == 3) and (not player2.IsDouble()):
                print("You must pay $50")
                player2.in_jail = False
                player2.turns_in_jail = 0
                player2.cash -= 50
                player2.AdvancePos()
                
            

        # If player is not in jail:         
        else: 
            # Player can roll doubles 3 times before going to jail.
            print(f"\nIt's {player2.name}'s turn")
            player2.DieRoll()
            player2.AdvancePos()
            player2.DisplayAttributes()
            
            if player2.IsDouble():
                print("\nYou rolled doubles! (1)")
                player2.DieRoll()
                player2.AdvancePos()
                player2.DisplayAttributes()
                
                if player2.IsDouble():
                    print("\nYou rolled doubles! (2)")
                    player2.DieRoll()
                    player2.AdvancePos()
                    player2.DisplayAttributes()
                    
                    if player2.IsDouble():
                        print("\nYou rolled doubles! (3) ...Go to jail")
                        player2.location = 10
                        player2.in_jail = True
                        print(board.spaces[player2.location])
                

    complete = input("\nGame over? (y/n) ")
    if complete == "y":
        done = True



