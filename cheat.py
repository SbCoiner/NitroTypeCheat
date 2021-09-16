import time
import keyboard
import random
import string
import pyperclip

f = open("config.txt", 'r').readlines()
wpm = float(f[0].replace(' ', '').replace('wpm=', ''))
accuracy = float(f[1].replace(' ', '').replace('accuracy=', ''))

while True:
    used_nitro = False
    made_up = 0.00
    prev_text = pyperclip.paste()

    while True:
        if pyperclip.paste() == prev_text:
            continue
        else:
            words = pyperclip.paste().split('\xa0')
            prev_text = pyperclip.paste()
            break
        
    for word in words:
        if (not used_nitro) and len(word) >= 10:
            keyboard.press_and_release('enter')
            continue

        rand = random.uniform(0.00, 100.00)
        if rand > accuracy:
            keyboard.write(random.choice(string.ascii_letters))
            made_up += 1
            time.sleep(1)

        keyboard.write(word + ' ')
        
        if made_up == 0.0:
            time.sleep(60/wpm)
        else:
            if made_up >= 0.3:
                time.sleep(60/wpm - 0.3)
                made_up -= 0.3
            else:
                time.sleep(60/wpm - made_up)
                made_up = 0.0
