import time
import os
from get_answers import get_answers
from put_answers import put_answers

if os.name == "nt":
    answer_page_filename = input("\033[1m" + "What is the full file path (relative to the home directory) of the saved answer page? " + "\033[0m")
else:
    answer_page_filename = os.path.expanduser("~") + "/Downloads/" + input("\033[1m" + "What is the name of the file you put in the ~/Downloads directory? " + "\033[0m")

print("Extracting answers from the answer page...")
answers = get_answers(answer_page_filename)
print("Answers have been extracted.")

print("\033[1m" + "You have 3 seconds to go to the new quiz page and click on the first answer box. Do not press or click anything until you see the bot enter the last answer." + "\033[0m")
time.sleep(3)

print("Entering in answers...")
put_answers(answers)
print("Answers have been entered in.")
