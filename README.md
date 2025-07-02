# Carrox: Interactive Carrot Game

## Overview

Carrox is an interactive carrot-pulling game built with Python and Pygame controlled by a hardware Arduino carrot controller. 
Carrots can be shaken and pulled into a basket, use your carrot controller in reality to match the carrot movement on the screen!

---

## Setup

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```
or import  Pygame, PySerial

---

## Running the Game

To use with Arduino hardware:

1. Set the mode at the top of `main.py`:
   ```python
   USE_ARDUINO = True
   ```
2. Make sure your Arduino is connected and the serial port in `main.py` is correct (e.g., `/dev/cu.usbserial-110`).
3. Run the game with:
  ```
  python main.py
  ```
## Credits
Made by Dingning Cao and Karla Sahin for Mingming Li and Jiaji Li :D

