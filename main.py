"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

from board import empty_board, print_board
from players import choose_opponent, handle_ai_move, handle_human_move
from helper import handle_win, handle_draw, game_over, play_again, DOUBLE_SEPARATOR, DASH_SEPARATOR

def play_game():
    """
    This function serves as the main loop of the game,
    managing gameplay until the user decides to stop it.

    The function calls other functions to:
        Manage the game board,
        Choose opponent (human or AI),
        Handle player moves,
        Check for win or draw,
        Record score
    """

    # Win counter
    win_x, win_o = 0, 0

    chosen_opponent = None

    # Gameplay loop
    while True:

        # Chooses either human or AI opponent and remembers the choice for further games
        if chosen_opponent is None:
            opponent = choose_opponent()
            chosen_opponent = opponent
        else:
            opponent = chosen_opponent

        # Sets the board and starting player
        board = empty_board()
        player = "X"

        # Game progress – one game
        while True:
            print_board(board)
            print(DOUBLE_SEPARATOR)

            # AI opponent
            if opponent == "A" and player == "O":
                handle_ai_move(board, player)

            # Human player
            else:
                handle_human_move(board, player)

            # Checks if the player won
            result = game_over(board, player)
            if result == "win":
                win_x, win_o = handle_win(board, player, win_x, win_o)
                break

            # Checks if there is a draw
            if result == "draw":
                handle_draw(board)
                break # Jumps to play_again

            # Switches the player
            player = "O" if player == "X" else "X"

        # Prints the current score
        print(DOUBLE_SEPARATOR)
        print(f"Player X wins: {win_x} | Player O wins: {win_o}")
        print(DOUBLE_SEPARATOR)

        # Asks if the players want another game
        if not play_again():
            break

# Introduction and game rules
print(f"""
Welcome to Tic Tac Toe
{DOUBLE_SEPARATOR}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{DOUBLE_SEPARATOR}
Let's start the game
{DASH_SEPARATOR}"""
)

if __name__ == "__main__":
    play_game()
