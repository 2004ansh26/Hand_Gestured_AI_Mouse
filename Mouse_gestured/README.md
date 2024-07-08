# Hand Gesture Controlled Mouse

This project uses OpenCV, MediaPipe, and PyAutoGUI to create a hand gesture-controlled mouse. The application detects hand gestures from a webcam feed and performs mouse movements and actions based on the gestures.

## Features

- Hand tracking using MediaPipe
- Control mouse movements with index finger
- Click with index and middle fingers
- Scroll with index, middle fingers, and thumb

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## Installation

1. Clone the repository:

```sh
git clone https://github.com/2004ansh26/Hand_Gestured_AI_Mouse.git
cd Hand_Gestured_AI_Mouse
```

2. Install the required packages:

```sh
pip install opencv-python mediapipe pyautogui numpy
```

3. Run the application:

```sh
python MouseGestured.py
```

# User Manual

-  Up index finger - move the cursor 
-  up index & middle finger - cursor will stop moving
-  up index & middle finger and both finger tips are joint - left click
-  up index & up thumb - scroll the screen 
