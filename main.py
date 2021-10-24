import time
import os
from get_answers import get_answers
from put_answers import put_answers

if os.name == "nt":
    answer_page_filename = os.path.expandvars(
        "C:\\Users\\$USERNAME\\Downloads\\quia_answer_page.html"
    )
else:
    answer_page_filename = os.path.expanduser("~") + \
        "/Downloads/quia_answer_page.html"
answers = get_answers(answer_page_filename)
time.sleep(3)
put_answers(answers)
