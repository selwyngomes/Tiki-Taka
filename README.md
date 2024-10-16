
# Tiki-Taka: The Game

Tiki-Taka is a modern take on a classic 90s game inspired by retro Pong but enhanced with hand-tracking technology. Using OpenCV for hand detection, the game allows players to control paddles with their hands, providing a unique and immersive gameplay experience without the need for physical controllers.

# Project Overview


This project demonstrates the use of computer vision techniques to create a fully functional game where the player can interact with on-screen elements via a camera. The game utilizes OpenCV, CVZone, and MediaPipe for real-time hand detection and motion tracking. The objective is simple: defend your corner and score points by bouncing the ball back to your opponent.



## Features

- Hand Tracking: Control paddles by moving your hands in front of the camera.

- Dynamic Gameplay: The ball increases in speed with each successful hit, making the game more challenging.

- Multiplayer Support: Two hands can be tracked simultaneously, allowing for two-player mode.

- User-Friendly Interface: Easy-to-use start, stop, and reset controls.

## Requirements

- Python 3.x

- OpenCV

- cvzone

- numpy





## Deployment

Install the necessary dependencies using pip:

```bash
  pip install opencv-python cvzone numpy
```
# How to Play

- Clone the Repository

```bash
  git clone https://github.com/yourusername/TikiTaka.git
```
- Navigate to the project directory

```bash
  git clone cd TikiTaka
```
- Navigate to the project directory

```bash
  git clone cd TikiTaka
```
- Run the game

```bash
  python tikitaka.py
```
- Ensure that your webcam is active, as it is used for hand tracking.
## Directory Structure

```bash
TikiTaka/
│
├── Resources/               # Contains game assets (images)
│   ├── Background.png
│   ├── Ball.png
│   ├── bat1.png
│   ├── bat2.png
│   ├── gameStart.png
│   ├── gameStart1.png
│   └── gameOver.png
│
├── tikitaka.py              # Main Python script
└── README.md                # Project documentation
```
## Controls

- Left Paddle: Controlled by your left hand.
- Right Paddle: Controlled by your right hand.
- Restart: Press 'R' on the keyboard to restart the game.
## Game Modules

# 1. UI/UX
The user interface is straightforward, offering clear Start and Stop screens, along with a Game Over display. The paddles (disks) move along the Y-axis, and the ball registers scores upon hitting the surfaces.

# 2. Hand Tracker:
The hand tracker module uses OpenCV and MediaPipe to detect and track up to two hands at a time, allowing for accurate paddle movements.

# 3. Ball Physics
The ball responds dynamically to player interaction. It starts with a speed of 15 ppi, which increases with every successful hit. When the ball hits the paddles, it changes direction and velocity.

# 4. Known Limitations
Engine Instability: Python's speed and performance may not match modern game engines like Unreal Engine, affecting frame rates and speed dynamics.
Palm Detection Errors: Occasionally, the system fails to re-detect hands if they go out of frame.

## Future Enhancements

- Migrate to a more powerful game engine for better performance and scalability.
- Implement dynamic level progression and player rewards.
- Add more visual effects and improve graphics with 3D transitions.
- Introduce multiplayer mode with AI-driven opponents.
## Contributing

- Contributions are always welcome!

- If you have suggestions for improving the script, feel free to create a pull request or open an issue on GitHub.


## Acknowledgements

This project was guided by **Dr. Sunitha Joshi**, and I express gratitude to everyone who contributed, directly or indirectly, to the completion of this project.


## License

This project is licensed under the MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

