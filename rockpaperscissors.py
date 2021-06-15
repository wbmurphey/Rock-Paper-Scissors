#!/usr/bin/env python3

import random

while True:
    quit_input = input("Enter q to quit or hit enter to continue: ")
    if quit_input.lower() == 'q':
        exit()
    else:
        choice = ["rock", "paper", "scissors"]
        usr_throw = input("Enter rock paper or scissors: ")
        usr_throw = usr_throw.lower()
        usr_throw_idx = 69

        while usr_throw_idx > 2:
            if usr_throw == "rock":
                usr_throw_idx = 0
            elif usr_throw == "paper":
                usr_throw_idx = 1
            elif usr_throw == "scissors":
                usr_throw_idx = 2
            else:
                usr_throw = input("Try again pal: ")

        usr_choice = choice[usr_throw_idx]
        comp_choice = choice[random.randint(0, 2)]

        print(f"User chose {usr_choice}.")
        print(f"Computer chose {comp_choice}.")


        if usr_choice == comp_choice:
            print("it's a tie")
        elif usr_choice == "rock" and comp_choice == "paper":
            print("computer wins")
        elif usr_choice == "rock" and comp_choice == "scissors":
            print("user wins")
        elif usr_choice == "paper" and comp_choice == "rock":
            print("user wins")
        elif usr_choice == "paper" and comp_choice == "scissors":
            print("computer wins")
        elif usr_choice == "scissors" and comp_choice == "rock":
            print("computer wins")
        elif usr_choice == "scissors" and comp_choice == "paper":
            print("user wins")
