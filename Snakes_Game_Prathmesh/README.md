# Snake Game v1.0 & v1.1

## Introduction
This repository contains a classic Snake game built using **Pygame**. The game begins with a welcome screen where players can control the snake's movement to collect apples, grow in length, and avoid collisions. The game tracks the player's score and saves the highest score as a high score.

### Game Versions:
- **v1.0**: A basic version of the game with snake movement, collision detection, scoring, and apple collection.
- **v1.1**: Refactored with an object-oriented approach to handle the snake's body, eyes, and movement logic more efficiently.

## Features
- **Snake Movement**: Control the snake using the arrow keys (`UP`, `DOWN`, `LEFT`, `RIGHT`).
- **Apple Collection**: Increase the snake's length and score by eating apples.
- **Collision Detection**: The game ends if the snake collides with the boundary or itself.
- **High Score Tracking**: The highest score is saved and displayed at the end of the game.
- **Welcome Screen**: Start the game by pressing the `SPACE` bar.
- **Smooth Gameplay**: Efficient game rendering and event handling using Pygame.
- **Sound Effects**: Collision sound and background music for an engaging experience.

## Requirements
- **Python 3.x**
- **Pygame**

Install Pygame:
```bash
pip install pygame
```

## Installation and Usage

### Step 1: Fork the Repository
Fork this repository to your GitHub account by clicking the "Fork" button at the top of this page.

### Step 2: Clone the Forked Repository
After forking, clone the repository from **your account** to your local machine:
```bash
git clone https://github.com/<your-username>/ACM-GitQuest-HacktoberFest-2024.git
cd ACM-GitQuest-HacktoberFest-2024
git checkout classic-snakes-game
```

### Step 2: Install Dependencies
Navigate to the project directory and install the required dependencies using:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Game
To start the game, run the following command based on the version you want to play:
- For **v1.0**:
  ```bash
  python Snake_Game_v1.0.py
  ```
- For **v1.1**:
  ```bash
  python Snake_Game_v1.1.py
  ```

## Controls
- **UP Arrow**: Move the snake up.
- **DOWN Arrow**: Move the snake down.
- **LEFT Arrow**: Move the snake left.
- **RIGHT Arrow**: Move the snake right.
- **TAB**: Slow down the snake (v1.0 only).

## Project Structure
```plaintext
├── .gitignore           # Ignored files/folders for version control
├── LICENSE              # MIT License
├── Highscore.txt        # Stores the highest score achieved in the game
├── Hit.mp3              # Sound played when the snake hits a boundary or itself
├── Nagin.mp3            # Background music during gameplay
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
├── Snake_Game_IMG.jpg   # Background image for the game
├── Snake_Game_v1.0.py   # Version 1.0 of the Snake Game
├── Snake_Game_v1.1.py   # Refactored Version 1.1 with OOP
```

## Code Walkthrough

### Snake_Game_v1.0.py
- **Game Window**: The game runs at a resolution of 610x610 pixels with a custom background image.
- **Snake Movement & Apple Collection**: The snake grows in length upon eating apples, and its movement is controlled using the arrow keys.
- **Collision Detection**: The game ends if the snake collides with the boundaries or its own body.

### Snake_Game_v1.1.py
- **Object-Oriented Refactor**: The game has been refactored using an OOP approach with a `Snake` class to manage the snake's body, eyes, and movement.
- **Improved Modularity**: Snake movement, apple collection, and collision detection have been encapsulated within the `Snake` class for better code organization.

## Future Improvements
- **v2.0**:
  - Add levels or difficulty modes.
  - Implement a pause menu.
  - Include power-ups or special apples for bonus points.

## License
This project is licensed under the MIT License.

---