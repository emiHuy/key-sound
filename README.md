# KeySound

## Description
A program that plays sounds when keys are pressed. It contains various sound themes and sounds for different keys.

## ⚠️ Disclaimer: 
This project uses `pynput`'s keyboard listener to detect keystrokes in real time for sound generation. It does not record, store, or transmit keystroke data. This project is intended only for educational, creative, and non-malicious purposes.

## Project Metadata
**Author:** Emily  
**Date Created:** June 13, 2025  
**Last Updated:** June 14, 2025  

## Features
- Play different sounds for different keys/groups of keys
- Has different sound themes to choose from (ie. Minecraft, Super Mario Bros., Animal Crossing)
- Volume adjustment

## Requirements
- Python 3.12.5
- Install the necessary dependancies using the `requirements.txt` file

## File Information
- `.gitignore`: specifies untracked files to ignore in Git
- `key_sound_controller.py`: event handling and user interaction
- `key_sound_player.py`: business logic, detects the keys pressed and plays the sounds
- `key_sound_window.py`: GUI (with PySide6)
- `main.py`: entry point
- `README.md`: project overeview and documentation
- `requirements.txt`: necessary packages and dependencies
- `utils.py`: contains helper function for handling file paths

### /assets/
- `images/`: contains images and icons used for the combo box component in the GUI
- `sounds/`: contains sound files that are grouped by themes. These sounds are played in response to keys pressed