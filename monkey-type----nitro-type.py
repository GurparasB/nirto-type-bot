import pytesseract
from PIL import Image
import pyautogui
import time

def capture_read_and_type(region=None, save_image=False):
    print("Waiting 5 seconds before capturing screenshot...")
    time.sleep(5) 

    screenshot = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()

    screenshot = screenshot.convert("L")

    if save_image:
        screenshot.save("screenshot.png")
        print("Screenshot saved as 'screenshot.png'")

    text = pytesseract.image_to_string(screenshot)

    print("\nExtracted Text:")
    print(text if text.strip() else "No text detected.")

    lines = text.strip().split("\n")  
    for line in lines:
        pyautogui.typewrite(line)
        pyautogui.press("space")   

# Format: (x, y, width, height)

#monkey type 
capture_read_and_type(region=(100, 450, 1800, 400), save_image=True)

#nitro type 
#capture_read_and_type(region=(500, 750, 600, 200), save_image=True)
