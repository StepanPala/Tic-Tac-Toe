"""This module contains functions managing the game board."""

def print_board(board):
    """
    Creates empty 3x3 game board.
    
    Args:
        board: 2D list representing the game board."""
    print("+---+---+---+")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")

def empty_board() -> list[list[str]]:
    """Sets the board for game.

    Returns:
        New game board ready for the game.
    """
    return [[" " for _ in range (3)] for _ in range(3)]
