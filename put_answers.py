import pyautogui

def put_answers(answers):
    for answer in answers:
        pyautogui.typewrite(answer)
        pyautogui.press("Tab")
