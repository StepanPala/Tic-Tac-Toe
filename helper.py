"""This module contains miscellaneous functions for smooth gameplay."""

from board import print_board

def check_win(board: list, player: str) -> bool:
    """Checks if any of the players won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def game_over(board: list, player: str) -> str:
    """
    Checks if the game is over.

    Returns:
        "win": If the player has won.
        "draw": If the game ended with a tie.
        "continue": If the game isn't over yet.
    """
    if check_win(board, player):
        return "win"
    if all(all(square != " " for square in row) for row in board):
        return "draw"
    return "continue"

def handle_win(board: list, player: str, win_x: int, win_o: int) -> tuple[int, int]:
    """Handles win scenario."""
    print_board(board)
    print(DOUBLE_SEPARATOR)
    print(f"Congratulations, Player {player} WON!")
    win_x, win_o = score(player, win_x, win_o)
    return win_x, win_o

def handle_draw(board: list):
    """Handles draw scenario."""
    print_board(board)
    print(DOUBLE_SEPARATOR)
    print("It's a tie!")

def score(player: str, win_x: int, win_o: int) -> tuple[int, int]:
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
        if again == "no":
            return False
        print("Please enter \"yes\" or \"no\".")

# Separators
DOUBLE_SEPARATOR = '=' * 42
DASH_SEPARATOR = '-' * 42
