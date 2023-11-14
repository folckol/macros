import time

import pyautogui
import keyboard


keys = []
with open('results.txt', 'r') as file:
    for i in file:
        keys.append(i.strip('\n'))

# print(keys[3:-3])


print("Нажмите кнопку, чтобы начать воспроизведение макроса")

while True:

    key = keyboard.read_event()

    if key.name == 'space':
        print('Воспроизведение началось')
        break

keys = keys[3:-3]
ww = True
for key in keys:
    print(key)

    if 'DOWN' in key:
        if ww == True:
            keyboard.press(key.split(' ')[0])
            ww = False

        if ww == False:
            continue

    elif 'UP' in key:

        keyboard.release(key.split(' ')[0])
        ww = True

    else:
        time.sleep(float(key))


