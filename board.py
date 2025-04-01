"""
This module contains functions for creating and managing the game board
for Tic-Tac-Toe. 
"""


def print_board(board):
    """
    Prints the current game board.
    
    Args:
        board: 2D list representing the game board."""
    print("+---+---+---+")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")


def empty_board() -> list[list[str]]:
    """Creates and returns an empty 3x3 game board.

    Returns:
        2D list with an empty game board with each element being
        an empty string (" ").
    """
    return [[" " for _ in range (3)] for _ in range(3)]
