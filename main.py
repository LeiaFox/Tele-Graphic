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

def load_game():
    print("What is the name of your save file?")
    while True:
        save_file = input("> ")
        sure = input("Are you sure? (y/n)\n> ")
        if sure == "y":
            break
        elif sure == "n":
            break
        else:
            continue
    char = open(save_file + "/char.json")
    load_char = json.loads(char.read())
    my_player.name = load_char["name"]
    my_player.xp = load_char["xp"]
    my_player.lv = load_char["lv"]
    my_player.hp = load_char["hp"]
    my_player.stamina = load_char["stamina"]
    my_player.job = load_char["job"]
    my_player.status_effect = load_char["status_effect"]
    my_player.location = load_char["location"]
    my_player.game_over = load_char["game_over"]
    my_player.inventory = load_char["inventory"]

    zonem = open(save_file + "/zone_map.json")
    zone_map = json.loads(zonem.read())
    global zone_map

    completep = open(save_file + "/complete_places.json")
    complete_places = json.loads(completep.read())
    global complete_places

    print("Welcome back.")
    time.sleep(2.0)
    main_game_loop()


def save_game():
    print("What would you like to name your save file?")
    while True:
        save_file = input("> ")
        sure = input("Are you sure? (y/n)\n> ")
        if sure == "y":
            if not os.path.exists(save_file):
                break
            else:
                print("Exception: Save file name already exists!")
                while True:
                    print("Would you like to overwrite this save? (y/n)")
                    save_over = input("> ")
                    if save_over == "y":
                        break
                    elif save_over == "n":
                        break
                if save_over == "y":
                    break
                elif save_over == "n":
                    continue
        elif sure == "n":
            break
        else:
            continue

    char_json = {
        "name": my_player.name,
        "xp": {
            "xp": my_player.xp["xp"],
            "maxxp": 500
        },
        "lv": {
            "lv": my_player.lv["lv"],
            "maxlv": 20
        },
        "hp": {
            "hp": my_player.hp["hp"],
            "maxhp": my_player.hp["maxhp"]
        },
        "stamina": {
            "stamina": my_player.stamina["stamina"],
            "maxstamina": 10
        },
        "job": my_player.job,
        "status_effect": my_player.status_effect,
        "location": my_player.location,
        "game_over": my_player.game_over,
        "inventory": my_player.inventory
    }

    os.mkdir("./" + save_file)

    with open(save_file + "/char.json", 'w') as f:
        json.dump(char_json, f)
    with open(save_file + "/zone_map.json", 'w') as f:
        json.dump(zone_map, f)
    with open(save_file + "/complete_places.json", 'w') as f:
        json.dump(complete_places, f)


class player:
    def __init__(self):
        self.name = ''
        self.xp = {"xp": 0, "maxxp": 500}
        self.lv = {"lv": 0, "maxlv": 20}
        self.hp = {"hp": 0, "maxhp": 0}
        self.stamina = {"stamina": 0, "maxstamina": 10}
        self.job = ''
        self.status_effect = []
        self.location = 'b3'
        self.game_over = "False"
        self.inventory = []


my_player = player()


def title_screen_selections():
    while True:
        option = input("\n> ").lower()
        if option == "play":
            while True:
                neworload = input("Would you like to load a game or start a new one? (new, load)\n> ")
                if neworload == "new":
                    break
                elif neworload == "load":
                    break
                else:
                    continue
            if neworload == "new":
                setup_game()
            elif neworload == "load":
                load_game()
        elif option == "help":
            help_menu()
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
    clear_screen()
    print('''
  - Type up, down, left or right 
    to move around the place
  - Type your commands to do them
  - Type "inspect" to inspect 
  	something around you
	''')
    title_screen_selections()


#### GAME FUNCTIONALITY ####
def main_game_loop():
    while my_player.game_over == "False":
        prompt()


def setup_game():
    clear_screen()
    question = "\nWhat would be your name?\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    my_player.name = player_name

    question = "\nWhat class would you like to be?\n"
    question2 = "\nClasses: Technician, Arms Handler, Swordsman\n"
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    valid_jobs = ["technician", "arms handler", "swordsman"]
    player_job = ""
    while player_job not in valid_jobs:
        player_job = input("> ").lower()
        if player_job not in valid_jobs:
            print("Class must be valid. Enter again.")
            continue
        else:
            break
    my_player.job = player_job
    print(f"You are now a {player_job}")

    my_player.job = player_job

    if my_player.job == "technician":
        my_player.xp = {"xp": 0, "maxxp": 500}
        my_player.lv = {"lv": 1, "maxlv": 20}
        my_player.hp = {"hp": 7, "maxhp": 7}
        my_player.inventory.append("light_gun")

    elif my_player.job == "arms handler":
        my_player.xp = {"xp": 0, "maxxp": 500}
        my_player.lv = {"lv": 1, "maxlv": 20}
        my_player.hp = {"hp": 10, "maxhp": 10}

    elif my_player.job == "swordsman":
        my_player.xp = {"xp": 0, "maxxp": 500}
        my_player.lv = {"lv": 1, "maxlv": 20}
        my_player.hp = {"hp": 15, "maxhp": 15}

    time.sleep(1.0)

    print("You crawl out of bed to a new day. You apartment is a mess.")

    time.sleep(2.0)

    main_game_loop()


#### GAME INTERACTIVITY ####
def print_location():

    print(zone_map[my_player.location][ZONENAME])
    print()
    print(zone_map[my_player.location][DESCRIPTION])


def prompt():
    print("\n" + "=================================")
    print("What will you do?")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine",
                          "inspect", "interact", "look", "help", "inventory",
                          "items", "stuff", "save", "equip", ]
    action = ""
    while action not in acceptable_actions:
        action = input("> ").lower()
    if action == "quit":
        clear_screen()
        print("Shutting Subject Down.")
        time.sleep(1.0)
        clear_screen()
        print("Shutting Subject Down..")
        time.sleep(1.0)
        clear_screen()
        print("Shutting Subject Down...")
        time.sleep(1.0)
        exit(0)
    elif action in ["move", "go", "travel", "walk"]:
        player_move(action)
    elif action in ["examine", "inspect", "interact", "look"]:
        player_examine(action)
    elif action in ["inventory", "items", "stuff"]:
        print(f"Here are your current stored items: \n{my_player.inventory}")
    elif action in "help":
        print(f"Acceptable commands:\n{acceptable_actions}")
    elif action in "save":
        save_game()


def player_move(my_action):
    ask = "where will you head to?\n> "
    destination = input(ask)
    if destination in ["up", "north"] and (zone_map[my_player.location][UP] != ""):
        destination = zone_map[my_player.location][UP]
        movement_handler(destination)
    elif destination in ["down", "south"] and (zone_map[my_player.location][DOWN] != ""):
        destination = zone_map[my_player.location][DOWN]
        movement_handler(destination)
    elif destination in ["left", "west"] and (zone_map[my_player.location][LEFT] != ""):
        destination = zone_map[my_player.location][LEFT]
        movement_handler(destination)
    elif destination in ["right", "east"] and (zone_map[my_player.location][RIGHT] != ""):
        destination = zone_map[my_player.location][RIGHT]
        movement_handler(destination)
    else:
        print("Invalid movement, probably out of bounds or you wrote something wrong.")


def movement_handler(destination):
    print(f"\nYou have moved to '{destination}.'")
    my_player.location = destination
    print_location()


def player_examine(action):
    if zone_map[my_player.location][COMPLETE]:
        print("You have already completed anything important to do here.")
    else:
        print(zone_map[my_player.location][EXAMINATION])


#### MAP ####
"""
 a1   a2  a3  a4
-----------------
¦ B ¦ B ¦ B ¦ B ¦ a4
-----------------
¦   ¦ W ¦ H ¦   ¦ b4
-----------------
¦   ¦ W ¦   ¦   ¦ c4
-----------------
¦   ¦ W ¦   ¦   ¦ d4
-----------------

B - black market
H - home
W - thin walkway
"""

ZONENAME = 'ZONENAME'
DESCRIPTION = 'DESCRIPTION'
EXAMINATION = 'EXAMINATION'
COMPLETE = "COMPLETE"
CLEANED = "CLEANED"
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

complete_places = {
    "a1": False, "a2": False, "a3": False, "a4": False,
    "b1": False, "b2": False, "b3": False, "b4": False,
    "c1": False, "c2": False, "c3": False, "c4": False,
    "d1": False, "d2": False, "d3": False, "d4": False,
}

zone_map = {
    "a1": {
        ZONENAME: "West Black Market Stall",
        DESCRIPTION: "This stall sells various hazardous and experimental drugs. These have been outlawed for a reason",
        EXAMINATION: "The man running the stall is covered in cybernetic implants,\nwhich at a first glance have obviously been stolen from various SCP/D droids you recognise.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b1",
        LEFT: "",
        RIGHT: "a2"
    },
    "a2": {
        ZONENAME: "Black Market Entrance",
        DESCRIPTION: "The entrance to the black market.\nYou wonder why such an obviously illegal area has not been raided or taken down by SCP/D law \nenforcement.",
        EXAMINATION: "Many intense and drudged looking people are entering and leaving the Black Market,\nsome of them look glance at you and,\nlikely under the assumption that you yourself are some sort of law enforcement,\nscoff at your existence.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b2",
        LEFT: "a1",
        RIGHT: "a3"
    },
    "a3": {
        ZONENAME: "Center Black Market Stall",
        DESCRIPTION: "description",
        EXAMINATION: "examination",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b3",
        LEFT: "a2",
        RIGHT: "a4"
    },
    "a4": {
        ZONENAME: "South Black Market Stall",
        DESCRIPTION: "description",
        EXAMINATION: "examination",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "b4",
        LEFT: "a3",
        RIGHT: ""
    },
    "b1": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "b2": {
        ZONENAME: "Thin Walkway",
        DESCRIPTION: "A thin walkway filled with signs and conglomerate advertisements",
        EXAMINATION: "Many advertisements are showcasing the new Better Than Life Virtual Environment Simulation.\nThis only appeals to the lower class and people living in horrid situations.\nClassic.",
        COMPLETE: False,
        CLEANED: False,
        UP: "a2",
        DOWN: "",
        LEFT: "",
        RIGHT: "b3"
    },
    "b3": {
        ZONENAME: "Apartment",
        DESCRIPTION: "This is your apartment. It's filled with trash. You haven't decided to clean it yet.",
        EXAMINATION: "Nothing has changed about your apartment. Except you remember you should clean it someday.",
        COMPLETE: False,
        CLEANED: False,
        UP: "",
        DOWN: "",
        LEFT: "b2",
        RIGHT: ""
    },
    "b4": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c1": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c2": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c3": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
    "c4": {
        ZONENAME: "",
        DESCRIPTION: "",
        EXAMINATION: "",
        COMPLETE: False,
        CLEANED: False,
        UP: ["up", "north"],
        DOWN: ["down", "south"],
        LEFT: ["left", "west"],
        RIGHT: ["right", "east"]
    },
}

title_screen()
