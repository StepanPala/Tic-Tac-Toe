# Piškvorky

*Note: English follows*

Jednoduchá implementace klasické hry Piškvorky napsaná v Pythonu

## Popis

Hra umožňuje souboj dvou lidských hráčů nebo hru jednoho hráče proti jednoduché umělé inteligenci (AI), která provádí náhodné tahy.
Hra probíhá na standardní mřížce 3x3 podle pravidel klasických piškvorek.

Jednotlivé funkce:
*   hra dvou lidských hráčů
*   hra proti počítači (jednoduché náhodné tahy)
*   přehledné zobrazení herní desky v konzoli
*   validace uživatelských vstupů (kontrola číselného vstupu, rozsahu 1-9 a obsazenosti políčka)
*   detekce výherních stavů (řádky, sloupce, diagonály)
*   detekce remízy (plná deska bez vítěze)
*   sledování skóre mezi jednotlivými hrami v rámci jedné herní relace
*   možnost opakovat hru po jejím skončení
*   přehledná struktura kódu rozdělená do modulů (`main.py`, `board.py`, `players.py`, `helper.py`)

## Použité knihovny a verze Pythonu

Tento program vyžaduje **Python 3.9** a novější.

Nejsou vyžadování žádné externí knihovny.

## Používání programu

Program spustíte přímo z příkazového řádku příkazem `python main.py`.
Všechny ostatní vstupy se zadávají v příkazovém řádku a potvrzují se klávesou Enter.
Uživatel postupuje podle instrukcí v konzoli. Zvolí si soupeře a zadává čísla políček pro své tahy.

## Příklad fungování

Spuštění:

`python main.py`

Ukázka:

```
Let's start the game
------------------------------------------
Would you like to play against another player (P) or against AI (A)?: a
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
Player X, please enter your move (1-9): 2 
==========================================
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
AI's move
==========================================
+---+---+---+
|   | X |   |
+---+---+---+
| O |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
```

## Struktura projektu

*   `main.py`: Hlavní modul, který obsahuje úvodní text, hlavní herní smyčku a volání funkcí z ostatních modulů.
*   `board.py`: Obsahuje funkce k vytvoření prázdné herní desky a její vykreslení do konzole.
*   `players.py`: Zpracovává akce hráčů – výběr soupeře, získání a validace tahu lidského hráče, generování tahu AI, označení tahu na desce.
*   `helper.py`: Obsahuje pomocné funkce – kontrola výhry, kontrola remízy, zpracování konce hry (výhra/remíza), aktualizace skóre, dotaz na opakování hry a definice oddělovačů pro výpis.

## Autor
Štěpán Pala


# Tic-Tac-Toe

A simple implementation of the classic game Tic-Tac-Toe in Python

## Description

The game allows two human players to duel or a single player game against a simple AI that makes random moves.
The game is played on a standard 3x3 grid according to the standard Tic-Tac-Toe rules.

Functions:
*   a game between two human players
*   a game against an AI (simple random moves)
*   clearly displayed game board in the console
*   validation of user inputs (checking numeric input, range 1-9 and empty spots)
*   detection of win conditions (rows, columns, diagonals)
*   tie detection (full board with no winner)
*   tracking scores between games within a single game session
*   option to replay the game after it is over
*   clearly structured code divided into modules (`main.py`, `board.py`, `players.py`, `helper.py`)

## Dependencies

This program requires **Python 3.9** or newer.

No external libraries required.

## Usage

Execute the script directly from your terminal/command line using `python main.py`.
All other inputs are typed in the command line and confirmed with the Enter key.
Follow the instructions in the command line. Choose an opponent and enter the square numbers to make a move.

## Example

Initiation:

`python main.py`

Example:

```
Let's start the game
------------------------------------------
Would you like to play against another player (P) or against AI (A)?: a
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
Player X, please enter your move (1-9): 2 
==========================================
+---+---+---+
|   | X |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
AI's move
==========================================
+---+---+---+
|   | X |   |
+---+---+---+
| O |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
==========================================
```

## Project structure

*   `main.py`: The main module, which contains the introductory text, the main game loop and function calls from other modules.
*   `board.py`: Contains functions to create a blank game board and render it to the console.
*   `players.py`: Handles player actions – opponent selection, human player turn and validation, AI turn generation, board move indication.
*   `helper.py`: Contains helper functions – win check, draw check, end of game (win/loss), score update, replay query and separators.

## Author
Štěpán Pala
