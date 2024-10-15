# Snake Game v1.0 & v1.1

## Overview

This project is a classic Snake game built using **Pygame**. The game starts with a welcome screen, and players can control the snake's movement to collect apples and grow in length while avoiding collisions. The game tracks the player's score and saves the highest score as a high score.

### Game Versions:
- **v1.0**: A basic version of the game with snake movement, collision detection, scoring, and apple collection.
- **v1.1**: Refactored with an object-oriented approach to handle the snake's body, eyes, and movement logic more efficiently.

## Features

- **Snake Movement**: Control the snake using arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`).
- **Apple Collection**: Increase the snake's length and score by eating apples.
- **Collision Detection**: The game ends if the snake collides with the boundary or itself.
- **High Score Tracking**: The highest score is saved and displayed upon game over.
- **Welcome Screen**: A start screen invites the player to begin by pressing the `SPACE` bar.
- **Smooth Gameplay**: Utilizes the Pygame library for efficient game rendering and event handling.
- **Sounds**: Hit sound on collision and background music for an engaging experience.

## How to Run

### Requirements:
- **Python 3.x**
- **Pygame**

Install Pygame:
```bash
pip install pygame
```

### Run the Game:

1. Clone the repository.
2. Navigate to the game directory.
3. Run the game using Python:
   - For v1.0:
     ```bash
     python Snake_Game_v1.0.py
     ```
   - For v1.1:
     ```bash
     python Snake_Game_v1.1.py
     ```

## Controls

- **UP Arrow**: Move the snake up.
- **DOWN Arrow**: Move the snake down.
- **LEFT Arrow**: Move the snake left.
- **RIGHT Arrow**: Move the snake right.
- **TAB**: Slow down the snake (v1.0 only).

---

## Code Walkthrough

### Snake_Game_v1.0.py

- **Modules Imported**:
  - `pygame`: For game rendering and controls.
  - `random`: For random apple placement.
  - `os`: To handle high score saving.
  - `sys.exit`: To exit the game cleanly.

- **Game Window**:
  - Dimensions: 610x610 pixels.
  - Background: An image is used for the game background, scaled to fit the window.

- **Colors**:
  - `white`, `red`, `green`, `navy`, `blue`, `black`: Defined for drawing objects and text.

- **Game Functions**:
  - `showText()`: Displays text on the screen at specified coordinates.
  - `plotSnake()`: Draws the snake's body using a list of coordinates.
  - `plotEyesR()` & `plotEyesL()`: Draws the snake's right and left eyes for better visualization.
  - `wlcScreen()`: Displays the welcome screen and waits for the player to start the game.
  - `gameLoop()`: The main game loop where snake movement, collisions, and scoring are handled.

### Snake_Game_v1.1.py

- **Refactored with Object-Oriented Programming**:
  - A `Snake` class was introduced to manage the snake's body, eyes, and movement. This encapsulates the snake's properties and logic, making the code cleaner and easier to extend.

- **Key Changes**:
  - Snake movement, eye positions, and apple collection are handled within the `Snake` class.
  - `move()` function manages user inputs and updates the snake's direction and speed.
  - Game boundaries, snake length, and collision detection logic are similar to version 1.0 but more modular and efficient.

---

## File Structure

```plaintext
├── .gitignore           # Ignored files/folders for version control
├── Highscore.txt        # Stores the highest score achieved in the game
├── Hit.mp3              # Sound played when the snake hits a boundary or itself
├── Nagin.mp3            # Background music during gameplay
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
├── Snake_Game_IMG.jpg   # Background image for the game
├── Snake_Game_v1.0.py   # Version 1.0 of the Snake Game
├── Snake_Game_v1.1.py   # Refactored Version 1.1 with OOP
```

---

## Future Improvements

- **v2.0**:
  - Add levels or difficulty modes.
  - Implement a pause menu.
  - Include power-ups or special apples for bonus points.
  - Refactor the game further for multiplayer functionality.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---