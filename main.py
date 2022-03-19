import json
import os
import time
import tkinter
import sys
import textwrap
import random
from tkinter import ttk
import termcolor
from termcolor import colored

# useful info
# https://stackoverflow.com/questions/62564224/python-text-rpg-how-to-save-load

new = colored("New Game", "red")

screen_width = 100


def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


# def save_game(save_name):
# if not os.path.exists(save_name):
# os.makedirs(save_name)
# with open(save_name + "/" + save_name + ".json", 'w') as f:
# json.dump(place, f)
# with open(save_name + "/inventory.json", 'w') as f:
# json.dump(inventory, f)
# else:
# print("Exception: Save file name already exists!")


class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.stamina = 0
        self.status_effect = []
        self.location = ''


my_player = player()


def title_screen_selections():
    while True:
        option = input("\n> ").lower()
        if option == "start":
            start_game()  # placeholder
            break
        elif option == "help":
            help_menu()  # placeholder
            break
        elif option == "quit":
            exit(0)
            break
        else:
            print("Exception: Invalid command")
            continue


def title_screen():
    clear_screen()
    print('''
###################################
# Welcome to TeleGraphic,         #
# A text-based game about death,  #
# murder, and living in a future  #
# desensitised to gore and        #
# incomprehensible horror.        #
###################################

				
            - Play -
            - Help -
            - Quit -
	    Copyright 2022 LeiaFox
	''')
    title_screen_selections()


def help_menu():
    print('''
###################################
# Welcome to TeleGraphic,         #
# A text-based game about death,  #
# murder, and living in a future  #
# desensitised to gore and        #
# incomprehensible horror.        #
###################################


  - Type up, down, left or right 
    to move around the place
  - Type your commands to do them
  - Type "inspect" to inspect 
  	something around you
	
	''')


#### GAME FUNCTIONALITY ####
# def start_game():


#### MAP ####

"""
a1    a2   a3  a4
-----------------
¦   ¦   ¦   ¦   ¦ b1
-----------------
¦   ¦   ¦   ¦   ¦ b2
-----------------
¦   ¦   ¦   ¦   ¦ b3
-----------------
¦   ¦   ¦   ¦   ¦ b4
-----------------
"""

DESCRIPTION = 'description'
EXAMINATION = 'examination'
COMPLETE = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

while True:
    title_screen()
