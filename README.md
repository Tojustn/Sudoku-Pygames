# Sudoku-Pygames

This is a Sudoku game that uses the same logic as my other suduoku program but implemented using the Pygame library. It features a graphical interface where users can interact with the Sudoku board by selecting cells and entering numbers. The game enforces Sudoku rules, ensuring that each number is valid within the board's constraints.

## Features
- **One solution**: Uses backtracking in order to check how many solutions the board has 
- **Graphical Interface**: Uses Pygame to render the Sudoku grid and numbers.
- **Interactive Gameplay**: Allows users to select squares and input numbers using the keyboard.
- **Valid Move Enforcement**: Ensures that user inputs follow Sudoku rules.
- **Highlighting**: Highlights selected squares to enhance the user experience.

## How to Play

1. **Select a Square**: Click on a square in the grid to select it. The selected square will be highlighted.
2. **Enter a Number**: Press a number key (1-9) to input a number into the selected square. The game will check if the move is valid.
3. **Quit**: Close the game window or press the escape key to exit.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tojustn/sudoku-pygames.git
   cd sudoku-pygames