# Password Manager

A simple graphical desktop application to generate strong passwords and securely store your credentials locally in a CSV file. Built using Python and Tkinter.

## Features

* **Graphical User Interface:** Clean and simple UI built with Python's built-in `tkinter` library.
* **Password Generator:** Automatically generates strong, random passwords containing a mix of letters (8-10), numbers (2-4), and symbols (2-4).
* **Local Storage:** Saves all your websites, emails, and passwords locally in a `data.csv` file.
* **Input Validation:** Ensures no fields are left blank before attempting to save.
* **Confirmation Dialogs:** Displays pop-up dialogs to confirm credential details before saving to prevent mistakes.

## Prerequisites

* Python 3.x installed on your system.
* A `logo.png` file in the same directory as the script (required for the app's UI canvas).
* *Note: All standard libraries used (`tkinter`, `csv`, `random`) come pre-installed with Python.*

## How to Use

1.  **Clone or Download** the project to your local machine.
2.  Ensure you have a file named `logo.png` (a 200x200 pixel image works best) in the same directory as `main.py`.
3.  Run the application from your terminal or command prompt:
    ```bash
    python main.py
    ```
4.  Enter the **Website** name.
5.  Enter your **Email/Username** (defaults to `example@gmail.com`).
6.  Either type your own password or click **Generate Password** to let the app create a highly secure one for you.
7.  Click **Add**. Verify the details in the pop-up and click **OK**.
8.  Your credentials are now saved in `data.csv`, and the input fields will automatically clear for your next entry.

## Project Structure

* `main.py`: The main Python application script containing the UI and logic.
* `logo.png`: The image file used in the UI (must be added by the user).
* `data.csv`: Auto-generated file created upon the first saved entry to store your credentials.