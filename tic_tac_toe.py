"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Štěpán Pala
e-mail: Palast@seznam.cz
"""

# Imports functions from functions.py
from board import empty_board, print_board
from players import choose_opponent, ai_player, player_move, mark_choice
from helper import game_over, score, play_again, double_separator

def play_game():
    """This is the main function that takes care of the gameplay."""

    # Win counter
    win_x = 0
    win_o = 0

    chosen_opponent = None

    # Gameplay loop
    while True:

        # Chooses either human or AI opponent and remembers the choice for further games
        if chosen_opponent == None:
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
            print(double_separator())

            # AI opponent
            if opponent == "A" and player == "O":
                print("AI's move")
                row, col = ai_player(board)
                mark_choice(board, player, row, col)
                print(double_separator())

            # Human player
            else:
                row, col = player_move(board, player)
                mark_choice(board, player, row, col)
                print(double_separator())

            # Checks if the player won
            result = game_over(board, player)
            if result == "win":
                print_board(board)
                print(double_separator())
                print(f"Congratulations, Player {player} WON!")
                win_x, win_o = score(player, win_x, win_o)
                break

            # Checks if there is a draw
            elif result == "draw":
                print_board(board)
                print(double_separator())
                print("It's a tie!")
                break # Jumps to play_again

            # Switches the player
            player = "O" if player == "X" else "X"

        # Prints the current score
        print(double_separator())
        print(f"Player X wins: {win_x} | Player O wins: {win_o}")
        print(double_separator())

        # Asks if the players want another game
        if not play_again():
            break

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

if __name__ == "__main__":
    play_game()
