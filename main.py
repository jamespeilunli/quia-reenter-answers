import sys
import time
import os
import shutil
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
if len(sys.argv) == 1:
    time.sleep(3)
else:
    time.sleep(int(sys.argv[1]))
put_answers(answers)

os.remove(answer_page_filename)
if os.path.isdir(answer_page_filename[:-5] + "_files"):
    shutil.rmtree(answer_page_filename[:-5] + "_files")

