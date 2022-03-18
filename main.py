import json
import os
import time
import tkinter
import sys
from tkinter import ttk
import termcolor
from termcolor import colored

#useful info
#https://stackoverflow.com/questions/62564224/python-text-rpg-how-to-save-load

new = colored("New Game","red")

def clear_screen():
  if sys.platform == 'win32':
    os.system('cls')
  else:
    os.system('clear')

def savegame(save_name):
	if not os.path.exists(save_name):
		os.makedirs(save_name)
		with open(save_name+"/"+save_name+".json", 'w') as f:
			json.dump(place, f)
		with open(save_name+"/inventory.json", 'w') as f:
			json.dump(inventory, f)
	else:
		print("Exception: Save file name already exists!")

#first thing people see
print("Welcome to TeleGraphic, A text-based game about death, murder, and living in a future desensitised to gore and incomprehensible horror.")
while True:
	newgame = input(f"\n\n\nWould you like to start a {new}? ")