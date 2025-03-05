import pyautogui
import time

def type_sentence():
    """
    Takes a user-inputted sentence and types it out automatically.
    """
    sentence = input("Enter a sentence to type: ")  # Get user input
    time.sleep(3)  # Gives time to switch to a text field

    pyautogui.typewrite(sentence, interval=0.001)  # Type the sentence
    pyautogui.press("enter")  # Press Enter after typing

# Run the function
type_sentence()