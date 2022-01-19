# Quia Re-enter Answer Bot

Bot that copies correct answers from a submitted instance of a [Quia quiz](https://www.quia.com/quicktour.html#:~:text=Complete%20online%20testing%20tools%20that%20allow%20you%20to%20create%20quizzes%2C%20grade%20them%20with%20computer%20assistance%2C%20and%20receive%20detailed%20reports%20on%20student%20performance.) to a new instance of the same Quia quiz.

## Dependencies

The programming language this uses is Python **version 3.x**; check your version by running `python --version`. If your version isn't version 3 or it tells you `python` isn't a command, install Python 3 [here](https://www.python.org/downloads/).

There are also external Python libraries you will have to install:
* [bs4 (Beautiful Soup 4)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
* [pyautogui](https://pyautogui.readthedocs.io/en/latest/) 

You can install both of these by running `pip install -r requirements.txt` 

## Usage

1. Go to the Quia [Student Zone Page](https://www.quia.com/studentZone). Sign in if it asks you.
2. Click on the "view results" button on the left of your chosen submitted quiz (to the left of the quiz name) in the table.  It will open a new window with a page containing the answers you submitted.
3. For Chrome: Save the page in the new window by using the keyboard shortcut <kbd>Ctrl</kbd>+<kbd>S</kbd> on Linux and Windows, and <kbd>Cmd</kbd>+<kbd>S</kbd> on Mac. Make sure you save it in the Downloads directory, and that it's named `quia_answer_page.html`. A directory might be created with the name `quia_answer_page_files`. The program will automatically delete this directory at the end.
4. Open and start a new instance of the same Quia quiz.
5. Run the program. On Mac, you can open Finder, go to the directory where you stored the `main.py` file, right click on it, click on Open With, and then click on Python Launcher. On Windows, you can open File Explorer, go to the directory where you stored the `main.py` file, and double click it. Linux users probably know how to run `main.py` via command line, so I won't give instructions for Linux on this step.
6. Go back to the page with the new instance of the Quia quiz, and click on the first answer box. The program will give you 3 seconds to do this. 
7. The program will automatically type in answers in the answer boxes. Do not press anything or click anywhere in the time that the program is still typing in the answers.
8. The `quia_answer_page.html` file and `quia_answer_page_files` directory will be deleted by the program.

## Code Structure

* `get_answers.py` contains the `get_answers` function that takes a filename as an argument (you'll have to install the answer page) and uses [web scraping](https://en.wikipedia.org/wiki/Web_scraping) to extract the correct answers from the quiz.
* `put_answers.py` contains the `put_answers` function that takes a list with the correct answers as an argument and uses GUI automation (using a program to simulate key presses and clicks) to put in answers in quia quiz input boxes.
* `main.py` adds user friendliness and is the main file (the file you run).

## TODO

- [ ] Decrease time of following "Usage" steps
  - [x]  Make it possible to run `main.py` from file explorer (remove input and provide instructions)
- [ ] Make a way for non-coders to fully understand all instructions (including installing `git`, using `git clone`, opening terminal, etc.)
- [ ] Make code error-proof (using try-except)
- [ ] Add comments
