from bs4 import BeautifulSoup

def get_answers(answer_page_filename):
    with open(answer_page_filename) as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    
    answers = []
    for answer in soup.find_all("font", attrs={"color": ["green", "red"]}): # <font color="green or red" ... contain answers
        if answer["color"] == "green": # <font color="green" ... means answer is correct
            answers.append(answer.span.get_text())
        else: # color is red, answer is wrong
            answers.append("")
    
    return answers
