"""This module contains miscellaneous functions for smooth gameplay."""

def double_separator():
    """Returns a string of 42 equal signs."""
    return '=' * 42

def check_win(board, player) -> bool:
    """Checks if any of the players won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def game_over(board, player):
    """
    Checks if the game is over.

    Returns:
        "win": If the player has won.
        "draw": If the gmae neded with a tie.
        "continue": If the game isn't over yet.
    """
    if check_win(board, player):
        return "win"
    elif all(all(square != " " for square in row) for row in board):
        return "draw"
    else:
        return "continue"

def score(player, win_x, win_o) -> tuple:
    """
    Updates the win count for the current player.
    
    Args:
        player: The current player who won the game ("X" or "O").
        win_x: Win count for Player X.
        win_o: Win count for Player O.
    
    Returns:
        A tuple containing updated win counts.
    """
    if player == "X":
       win_x += 1
    else:
        win_o += 1
    return win_x, win_o

def play_again() -> bool:
    """Asks if the players want another game."""
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Please enter \"yes\" or \"no\".")
