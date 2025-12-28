🏗️ Program Structure
The game is built using a Class-Based Architecture (class PONG), which ensures organized state management and easy function reuse.

Key Components:
The Constructor (__init__): Automatically initializes the game state, prompts for player input, sets the difficulty, and builds the game world.

AI Logic: The computer paddle uses a tracking algorithm to follow the ball's Y-coordinate. The speed of this tracking is dictated by the selected difficulty:

Easy: 0.08 speed

Medium: 0.15 speed

Hard: 0.25 speed

Collision Engine: Detects when the ball hits the top/bottom walls or the paddles, reversing trajectory and triggering sound effects.

Menu Logic: A dual-turtle system (one for shape, one for text) creates a clickable UI that pauses the game loop until a selection is made.

🎮 How to Play
Controls
W Key: Move Player Paddle Up

S Key: Move Player Paddle Down

Rules
Enter your name and select a difficulty (1, 2, or 3).

Prevent the ball from passing your paddle.

Score more points than the AI before the 60-second timer expires.

If you need a break, click the MENU button at the bottom of the screen.

📂 Installation & Execution
Prerequisites: Ensure you have Python installed (designed for Windows due to winsound).

Run the Game:

Bash

python pong_game.py
📝 Code Logic Overview
Movement: The ball movement is handled by updating its coordinates by ball_dx and ball_dy in a continuous while loop.

State Management: A boolean flag is used to monitor if the game is "Paused" or "Running," which controls whether the game logic executes inside the loop.

Winner Declaration: When the timer reaches zero, the game clears the screen and compares the player's score against the computer's to announce the winner.
