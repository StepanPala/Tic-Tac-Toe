"""This module contains functions relating to players and their moves."""

import random
from helper import DOUBLE_SEPARATOR

def ai_player(board: list) -> tuple[int, int]:
    """Determines the next move of the AI player using a simple random method."""
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))
    if not available_moves:
        return None
    return random.choice(available_moves)

def choose_opponent() -> str:
    """
    Gets player's choice of opponent, i.e. another player or AI.

    Returns:
        'P' for a human opponent, 'A' for an AI opponent.
    """
    while True:
        opponent = input(
            "Would you like to play against another\nplayer (P) or against AI (A)?: "
            ).upper()
        if opponent in ("P", "A"):
            return opponent
        print("Please enter \"P\" or \"A\".")

def handle_ai_move(board: list, player: str):
    """Handles AI move."""
    print("AI's move")
    row, col = ai_player(board)
    mark_choice(board, player, row, col)
    print(DOUBLE_SEPARATOR)

def player_input(board: list, player: str) -> int:
    """
    Gets user input for the move number and checks if it is valid.
    
    Args:
        board: 2D list representing the game board.
        player: The current player ("X" or "O").
        
    Returns:
        Player's chosen number.
    """
    while True:
        try:
            # Checks if it is a number
            choice = int(input(f"Player {player}, please enter your move (1-9): "))
            if 1 <= choice <= 9:
                row, col = (choice - 1) // 3, (choice - 1) % 3
                is_valid = valid_move(board, row, col)
                if is_valid:
                    return choice
                print("The spot is already taken. Please choose another spot.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a number.")

def handle_human_move(board: list, player: str):
    """Handles human move."""
    row, col = player_move(board, player)
    mark_choice(board, player, row, col)
    print(DOUBLE_SEPARATOR)

def valid_move(board, row, col) -> bool:
    """Checks if the move can be made."""
    if board[row][col] != " ":
        return False
    return True

def mark_choice(board: list, player: str, row: int, col: int):
    """Marks the player's choice on the board."""
    board[row][col] = player

def player_move(board: list, player: str) -> tuple[int, int]:
    """Returns valid coordinates."""
    while True:
        choice = player_input(board, player)
        row, col = (choice - 1) // 3, (choice - 1) % 3
        if valid_move(board, row, col):
            return row, col
        print("Please select an empty spot.")
