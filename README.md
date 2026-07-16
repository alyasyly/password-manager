# Password Manager

A simple graphical desktop application to generate strong passwords, securely store your credentials locally in a JSON file, and retrieve them easily. Built using Python and Tkinter.

## Features

* **Graphical User Interface:** Clean and simple UI built with Python's built-in `tkinter` library.
* **Search Functionality:** Quickly retrieve your saved email and password for a specific website.
* **Password Generator:** Automatically generates strong, random passwords containing a mix of letters (8-10), numbers (2-4), and symbols (2-4).
* **Local Storage:** Saves all your websites, emails, and passwords locally in a `data.json` file.
* **Input Validation:** Ensures no fields are left blank before attempting to save.
* **Confirmation Dialogs:** Displays pop-up dialogs to confirm credential details before saving to prevent mistakes.
* **Error Handling:** Safely handles missing or empty data files to prevent application crashes.

## Prerequisites

* Python 3.x installed on your system.
* A `logo.png` file in the same directory as the script (required for the app's UI canvas).
* *Note: All standard libraries used (`tkinter`, `json`, `random`, `messagebox`) come pre-installed with Python.*

## How to Use

1. **Clone or Download** the project to your local machine.
2. Ensure you have a file named `logo.png` (a 200x200 pixel image works best) in the same directory as `main.py`.
3. Run the application from your terminal or command prompt:
   ```bash
   python main.py