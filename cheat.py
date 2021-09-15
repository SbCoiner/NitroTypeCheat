import time
import keyboard
import random
import string

f = open("config.txt", 'r').readlines()
wpm = float(f[0].replace(' ', '').replace('wpm=', ''))
accuracy = float(f[1].replace(' ', '').replace('accuracy=', ''))

while True:
    text = input("Enter what u want to type: ")
    words = text.split(' ')
    used_nitro = False
    print("Press shift to start")
    keyboard.wait('shift')
    time.sleep(0.2)

    for word in words:
        if used_nitro == False and len(word) >= 10:
            keyboard.press_and_release('enter')
            continue

        rand = random.uniform(0.00, 100.00)
        if rand > accuracy:
            keyboard.write(random.choice(string.ascii_letters))
            time.sleep(0.5)

        keyboard.write(word + ' ')
        time.sleep(60/wpm)
