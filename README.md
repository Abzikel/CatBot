
# Cat Bot - Automated Message Sender

**Cat Bot** is a Python-based application that automatically sends the word "cat" to any specified input field, with configurable time intervals for message sending and waiting. It features a graphical user interface (GUI) built using PyQt5, allowing users to define minimum and maximum time intervals for both the message sending frequency and the waiting period between consecutive messages.

The program runs efficiently in the background and provides real-time control with start and stop functionality. It ensures user input validation, verifying that time intervals are valid numbers and that the minimum values are less than or equal to the maximum values. Additionally, the program can be compiled into a standalone executable using PyInstaller, making it easy to share with others who may not have Python installed.

## Features:
- Automated "cat" message sender with configurable intervals.
- User-friendly GUI built with PyQt5.
- Input validation to ensure valid time values.
- Start/stop button to control message sending.
- Can be compiled into an executable for easy distribution.

## Requirements

To run the script or generate the executable, you will need:

- **Python 3.x** installed.
- The following Python libraries:
  - `PyQt5`
  - `pyautogui`

You can install these dependencies by running:

```bash
pip install PyQt5 pyautogui
```

## Running the Program

If you are running the script directly, execute:

```bash
python catbot.py
```

## Creating the Executable

To create a standalone executable that you can share with others, you can use **PyInstaller**. First, install PyInstaller if you don’t have it:

```bash
pip install pyinstaller
```

Then, navigate to the directory where your script is located and run the following command:

```bash
pyinstaller --onefile --windowed tu_script.py
```

- `--onefile`: Packages everything into a single executable.
- `--windowed`: Ensures the program runs without showing a console window.

The executable will be generated in the `dist` folder.
