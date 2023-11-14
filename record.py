import time
from pynput import keyboard

# Функция записи нажатия клавиш клавиатуры и интервалов между ними
def record_keystrokes():
    print("Запись началась. Нажмите Esc, чтобы завершить запись.")
    keystrokes = []
    last_time = time.time() # Инициализация переменной времени

    Status = False

    def on_press(key):

        if Status == True:
            pass
        else:
            if key == keyboard.Key.esc:
                listener.stop()

            nonlocal last_time
            nonlocal keystrokes
            try:
                # Добавляем нажатие клавиши в массив нажатий клавиш и интервал до нее
                current_time = time.time() - last_time
                keystrokes.append(current_time)
                keystrokes.append(str(key) + ' DOWN')
                last_time = time.time()
            except AttributeError:
                pass

    def on_release(key):
        nonlocal last_time
        nonlocal keystrokes
        try:
            # Добавляем отпускание клавиши в массив нажатий клавиш и интервал до нее
            current_time = time.time() - last_time
            keystrokes.append(current_time)
            keystrokes.append(str(key) + ' UP')
            last_time = time.time()
        except AttributeError:
            pass

    # Настраиваем отслеживание клавиш
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    return keystrokes

# Основной цикл программы
print("Нажмите TAB, чтобы начать запись.")


def on_press1(key):
    if key == keyboard.Key.tab:
        listener1.stop()

with keyboard.Listener(on_press=on_press1) as listener1:
    listener1.join()


keystrokes = record_keystrokes()

print(keystrokes)
# Здесь можно сохранить массив нажатий клавиш и временных интервалов в файл или обработать как-то иначе

