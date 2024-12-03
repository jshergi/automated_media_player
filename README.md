# Automated Media Player with Hand Gesture Control
## Overview

This Automated Media Player uses hand gestures to control media playback and interact with the system. 
By leveraging MediaPipe, OpenCV, and PyAutoGUI, it interprets hand movements and finger counts as specific commands to control media playback on platforms like YouTube.

## Features
Gesture Controls:

    1 Finger: Forward video by 5 seconds.
    2 Fingers: Reverse video by 5 seconds.
    3 Fingers: Toggle between fullscreen and normal screen.
    4 Fingers: Mute or unmute the video.
    5 Fingers & Thumb (Fist): Pause or resume playback.
    Fist (0 fingers): Toggle captions on or off.

User-Friendly Visual Interface:

    Displays a graphical options menu using Pygame.
    Offers intuitive on-screen instructions for using gestures.

Gesture Recognition:

    Utilizes MediaPipe Hands for detecting and analyzing hand landmarks.
    Processes hand key points to count fingers and associate counts with commands.

## How It Works

    Gesture Detection:
        Captures live video feed using OpenCV.
        Identifies and tracks hand landmarks in real-time with MediaPipe.

    Command Execution:
        Maps the number of extended fingers to specific media player commands using PyAutoGUI.
        Sends keyboard shortcuts to the media player, enabling gesture-based control.

    YouTube Integration:
        Automatically opens a YouTube video upon launch.

    Debugging Interface:
        Shows the live video feed with hand landmarks drawn for debugging.
        Includes an escape mechanism to quit the application (ESC key).

## Installation
Prerequisites:

    Python 3.7+
    Install the following libraries:

    pip install opencv-python mediapipe pyautogui pygame

Setup:

    Save the script in a .py file.
    Connect a webcam for live video feed.
    Ensure YouTube is accessible in your default browser.

Usage

    Run the script:

    python automated_media_player.py

    Perform gestures as described in the Features section.
    Observe the media player's response to your gestures.
    Press the ESC key to exit the application.

## Notes

    The gesture recognition is designed for a single hand.
    Requires a well-lit environment for accurate hand tracking.
    Exiting the program also releases the webcam and closes all OpenCV windows.

## Limitations and Future Improvements

    Limitations:
        Requires continuous visibility of the hand for consistent operation.
        Gestures might be less accurate in low-light conditions or with complex backgrounds.

    Future Improvements:
        Add support for multiple hands.
        Extend gesture commands for more complex media control.
        Incorporate audio feedback for gesture actions.
        Improve UI elements in Pygame for enhanced user experience.
