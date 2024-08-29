# Sudoku-Pygames

This is a Sudoku game that uses the same logic as my other suduoku program but implemented using the Pygame library. It features a graphical interface where users can interact with the Sudoku board by selecting cells and entering numbers. The game enforces Sudoku rules, ensuring that each number is valid within the board's constraints. Pressing space will automatically solve the board

## Features
- **One solution**: Uses backtracking in order to check how many solutions the board has 
- **Graphical Interface**: Uses Pygame to render the Sudoku grid and numbers.
- **Interactive Gameplay**: Allows users to select squares and input numbers using the keyboard.
- **Valid Move Enforcement**: Ensures that user inputs follow Sudoku rules.
- **Highlighting**: Highlights selected squares to enhance the user experience.
- **Solver**: Space will automatically solve the puzzle
- **Win Checker**: Checks if the player wins and displays message

## How to Play

1. **Running the Game**:
    - Make sure you have Python and Pygame installed on your system.
    - Run the script `sudoku_board.py` to start the game.
  
2. **Controls**:
    - **Mouse**: Click on cells to select them.
    - **Keyboard**: Press numbers (1-9) to input them into the selected cell.
    - **Spacebar**: Automatically solve the puzzle.
    - **Esc/Close**: Exit the game.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tojustn/sudoku-pygames.git
   cd sudoku-pygames