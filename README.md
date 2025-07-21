# SpeedUP Maze

A fast-paced arcade game inspired by "Tomb of the Mask," built with Python and the Raylib library.

## Features

- **Main Menu:** A simple main menu to start the game.
- **Level Selection:** A screen to select from 10 levels, with the first level unlocked.
- **"Tomb of the Mask"-style Gameplay:** A single level with the core dashing and collision mechanics.
- **Quit Confirmation:** A confirmation dialog to prevent accidental closing of the game.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install the dependencies:**
    ```bash
    pip3 install raylib==5.5.0.2 --break-system-packages
    ```

## How to Play

1.  Run the game:
    ```bash
    python3 game.py
    ```
2.  Use the arrow keys to navigate the menus and select a level.
3.  Press "Enter" to start the selected level.
4.  In the game, use the arrow keys to dash in the desired direction.

## Controls

### Main Menu

- **Enter/Space:** Start the game and go to the level selection screen.
- **Escape:** Open the quit confirmation dialog.

### Level Selection

- **Arrow Keys:** Navigate between the levels.
- **Enter:** Start the selected level.
- **Escape:** Go back to the main menu.
- **Mouse Click on "Back" button:** Go back to the main menu.

### In-Game

- **Arrow Keys:** Dash in the chosen direction.
- **Escape:** Quit the game.

### Quit Confirmation

- **Arrow Keys:** Switch between "Yes" and "No".
- **Enter:** Confirm the selection.
- **Escape:** Cancel and return to the previous screen.
- **Mouse Click on "Yes" or "No" button:** Confirm the selection.

## File Structure

````

.SpeedUP_Maze/
├── game.py
├── resources/
│ ├── color/
│ │ └── colors.py
│ └── images/
│ └── meme.jpeg
└── states/
├── main_menu.py
├── level_selection.py
├── quit_confirmation.py
└── game_level.py

```

````
