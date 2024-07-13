# Calendar_using_python_tkinter
# Calendar Application

This is a simple calendar application built using Python's Tkinter library. The application displays the calendar for a specified year when the user inputs a year and clicks the "Show Calendar" button.

## Prerequisites

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- calendar module (standard Python module)

## Installation

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. Install Tkinter if it is not already installed. Tkinter usually comes pre-installed with Python. If you need to install it, you can do so using pip:
   ```bash
   pip install tk
   ```

## Usage

1. Save the script into a Python file, e.g., `calendar_app.py`.

2. Make sure you have an image file named `cal.png` in the same directory as the script. This image will be displayed in the application's GUI.

3. Run the script using the following command:
   ```bash
   python calendar_app.py
   ```

## Code Explanation

- **Import Statements:**
  ```python
  from tkinter import *
  import calendar
  ```
  The necessary modules are imported. Tkinter is used for creating the GUI, and the calendar module is used to fetch the calendar of the specified year.

- **showCal Function:**
  ```python
  def showCal():
  ```
  This function is responsible for creating a new GUI window that displays the calendar for the input year.

- **Main GUI Window:**
  ```python
  root = Tk()
  ```
  This creates the main GUI window where users can enter the year and click the button to show the calendar.

- **Widgets:**
  - `Label` widgets are used to display text and images.
  - `Entry` widget is used to take the year input from the user.
  - `Button` widgets are used for showing the calendar and exiting the application.

- **Widget Placement:**
  The `place` method is used to set the position of the widgets on the GUI window.

- **Event Handling:**
  The `showCal` function is bound to the "Show Calendar" button to display the calendar when clicked.

## Running the Application

1. When the application starts, it displays a window with a title "CALENDAR".
2. The user is prompted to enter a year in the input field.
3. Upon clicking the "Show Calendar" button, a new window will appear showing the calendar for the entered year.
4. The "Exit" button closes the application.

## Screenshot
![Screenshot 2024-07-13 093819](https://github.com/user-attachments/assets/8fe6f23f-64c2-46c7-9630-199db374d16e) ![Screenshot 2024-07-13 093829](https://github.com/user-attachments/assets/b6f02474-4b52-48f5-9695-c73611380147)

