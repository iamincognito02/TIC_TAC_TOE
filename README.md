# Tic Tac Toe with AI (Minimax Algorithm)

A simple **Tic Tac Toe** game implemented in Python using **Tkinter** for the GUI, where you can play against an AI that uses the **Minimax algorithm** to make its moves.

## Features
- Play Tic Tac Toe against an AI.
- The AI uses the Minimax algorithm for optimal moves.
- Scores are tracked for both the player and the AI.
- The game announces a winner after a player or AI wins 5 rounds.
- Automatic reset of the board after each round.
- Visual and responsive GUI with simple buttons and labels.

## Game Rules
- The player uses **X**, and the AI uses **O**.
- To win the game, align three of your marks (either **X** or **O**) in a row, column, or diagonal.
- The first player to reach 5 wins is declared the overall winner.

## How to Play
1. The player starts the game by clicking any of the available spots on the 3x3 grid.
2. The AI will automatically make its move.
3. The game continues until someone wins or the board is full.
4. The first player to win 5 rounds is the ultimate winner.

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## Installation
1. Clone the repository or download the code:
    ```bash
    git clone https://github.com/yourusername/tic-tac-toe-ai.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tic-tac-toe-ai
    ```
3. Run the game:
    ```bash
    python tic_tac_toe.py
    ```

## How it Works
- The AI makes decisions using the **Minimax algorithm**, which ensures it always chooses the best possible move.
- The algorithm evaluates the board state recursively, simulating possible future moves and their outcomes.
- The game updates after each move, and the GUI displays the updated board state along with the result.

## Minimax Algorithm
The Minimax algorithm is a recursive function that evaluates the possible moves and selects the optimal move for the AI. It works by:
- Maximizing the AI's chances of winning.
- Minimizing the player's chances of winning.
- Returning a score based on the game outcome.

## Sample Output
![image](https://github.com/user-attachments/assets/75ac0387-aeb5-47ef-b462-7739247b4dcb)
![image](https://github.com/user-attachments/assets/eca3c07c-cf9c-4e04-b684-44ea0276c76d)
![image](https://github.com/user-attachments/assets/e61fe34a-ae7b-40ff-9721-653f805e39d7)

