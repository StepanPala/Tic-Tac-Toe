"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

# Imports functions from functions.py
from functions import double_separator, play_game

# Introduction and game rules
print(
    f"Welcome to Tic Tac Toe\n"
    f"{double_separator()}\n"
    f"GAME RULES:\n"
    f"Each player can place one mark (or stone)\n"
    f"per turn on the 3x3 grid. The WINNER is\n"
    f"who succeeds in placing three of their\n"
    f"marks in a:\n"
    f"* horizontal,\n"
    f"* vertical or\n"
    f"* diagonal row\n"
    f"{double_separator()}\n"
    f"Let's start the game\n"
    f"{'-' * 42}"
    )

# Main game
play_game()
