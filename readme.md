# Road Hazard 🚗💨

**Road Hazard** is a fun and challenging road-crossing game built using Python and the Pygame library. Can you navigate through 10 lanes of heavy traffic and reach the safe zone?

![Road Hazard Gameplay](screenshot.png)

---

## 🎮 How to Play
The goal is to reach the **Top Grass Row** without getting hit by moving cars.

### Controls:
*   **Move:** Use the **Arrow Keys** (Up, Down, Left, Right) or **WASD**.
*   **Start Game:** Press **SPACE** on the menu screen.
*   **Restart:** Press **R** on the Game Over screen.

### Scoring:
*   **+10 points** for every lane you cross successfully.
*   **+500 points** bonus for reaching the safe zone (Top row).

---

## ✨ Features
*   **Dual Controls:** Supports both Arrow keys and WASD.
*   **Hit Detection:** Pixel-accurate collisions with a 1-second invincibility "blinking" window.
*   **Lives System:** You start with 3 lives. Don't lose them all!
*   **Dynamic Backgrounds:** Custom environment using tiled grass and road assets.
*   **Dynamic Difficulty:** Car spawn rates increase as your score goes higher.
*   **Audio:** Immersive background music and sound effects for jumps and crashes.

---

## 🛠️ Installation & Setup
To run this game, you will need **Python (3.11 or 3.12 recommended)**.

1.  **Install Pygame**:
    Open your terminal/command prompt and run:
    ```bash
    pip install pygame
    ```
    *(Note: If you have multiple Python versions, use `py -3.11 -m pip install pygame`)*

2.  **Run the Game**:
    ```bash
    python Script.py
    ```
    *(Note: If you have multiple Python versions, use `py -3.11 Script.py`)*

---

## 📂 File Structure
*   `Script.py`: Main game logic and code.
*   `Backgrounds/`: Tiles for grass, roads, and bushes.
*   `Cars/`: 48 unique car sprites.
*   `Characters/`: Player and death animation sprites.
*   `Sounds/`: Music and sound effect files.
