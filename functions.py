"""This file contains defined functions and any necessary libraries."""

import random

def double_separator():
    return '=' * 42

def create_grid(board):
    """Creates 3x3 playing board."""
    print("+---+---+---+")
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("+---+---+---+")

def check_win(board, player):
    """Checks if any of the players won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def play_again():
    """Asks if the players want another game."""
    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Please enter \"yes\" or \"no\".")

def ai_player(board):
    """Defines a simple AI player using random library."""
    available_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                available_moves.append((row, col))
    return random.choice(available_moves) if available_moves else None

def play_game():
    """This is the main function that takes care of the gameplay."""

    # Win counter
    win_x = 0
    win_o = 0

    # Gameplay loop
    while True:

        # Asks if you want to play against AI or against another player
        opponent = input("Would you like to play against another\nplayer (P) or against AI (A)?: ").upper()
        if opponent not in ("P", "A"):
            print("Please enter \"P\" or \"A\".")
            continue

        # Sets the board and starting player
        board = [[" " for _ in range (3)] for _ in range(3)]
        player = "X" # Starting player

        # Game progress – one game
        while True:
            create_grid(board)
            print(double_separator())

            # AI opponent
            if opponent == "A" and player == "O":
                print("AI's move")
                ai_row, ai_col = ai_player(board)
                board[ai_row][ai_col] = player
                print(double_separator())

            # Human player
            else:
                try: # Checks if the input is a number
                    choice = int(input(f"Player {player} | Please enter your move number: "))
                    print(double_separator())
                except ValueError:
                    print("You must enter a number.")
                    continue

                # Checks if the input is a number from 1 to 9
                if not 1 <= choice <= 9:
                    print("You have entered an invalid number.")
                    continue

                row = (choice - 1) // 3
                col = (choice - 1) % 3

                # Checks if the chosen spot is empty
                if board[row][col] != " ":
                    print("You must select an empty spot.")
                    continue

                # Marks the player's choice
                board[row][col] = player

            # Checks if the player won
            if check_win(board, player):
                create_grid(board)
                print(double_separator())
                print(f"Congratulations, Player {player} WON!")

                # Adds +1 to score and jumps to play_again
                if player == "X":
                    win_x += 1
                else:
                    win_o += 1
                break

            # Cheks if there is a draw
            if all(all(square != " " for square in row) for row in board):
                create_grid(board)
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

if __name__ == "__main__":
    play_game()
