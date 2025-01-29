"""This module contains functions relating to players and their moves."""

import random

def ai_player(board):
    """Determines the next move of the AI player using a simple random method."""
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))
    return random.choice(available_moves) if available_moves else None

def choose_opponent():
    """
    Gets player's choice of opponent, i.e. another player or AI.

    Returns:
        'P' for a human opponent, 'A' for an AI opponent.
    """
    while True:
        opponent = input("Would you like to play against another\nplayer (P) or against AI (A)?: ").upper()
        if opponent in ("P", "A"):
            return opponent
        else:
            print("Please enter \"P\" or \"A\".")

def player_input(board, player) -> int:
    """
    Gets user input for the move number and checks if it is valid.
    
    Args:
        board: 2D list representing the game board.
        player: The current player ("X" or "O").
        
    Returns:
        Player's chosen number.
    """
    while True:
        try: # Checks if it is a number
            choice = int(input(f"Player {player} | Please enter your move number: "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a number.")

def valid_move(board, row, col) -> bool:
    """Checks if the move can be made."""
    if board[row][col] != " ":
        return False
    return True

def mark_choice(board, player, row, col):
    """Marks the player's choice on the board."""
    board[row][col] = player

def player_move(board, player) -> tuple[int, int]:
    """Returns valid coordinates."""
    while True:
        choice = player_input(board, player)
        row, col = (choice - 1) // 3, (choice - 1) % 3
        if valid_move(board, row, col):
            return row, col
        else:
            print("Please select an empty spot.")
