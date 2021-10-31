from bs4 import BeautifulSoup

def get_answers(answer_page_filename):
    with open(answer_page_filename) as f:
        contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    
    answers = []
    question_number = 1
    for question in soup.find_all("li"): # li elements contain answers
        if question.div.font["color"] == "green": # <div><font color="green" ... means answer is correct
            answers.append(question.div.font.span.get_text())
        else: # color is red
            answers.append("")
        question_number += 1
    
    return answers
