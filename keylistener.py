from pynput import keyboard


def on_press(key):
    try:
        if key.char == "s":
            print("Start program")
        elif key.char == "m":
            print("Go to main")
        elif key.char == "p":
            print("Pause program")
        else:
            print("  key {0} pressed".format(key.char))
    except AttributeError:
        if key != keyboard.Key.esc:
            print("  special key {0} pressed".format(key))
        else:
            print("Exit program")
            return False


# Collect events until released
print("automated investing")
with keyboard.Listener(on_release=on_press) as listener:
    listener.join()
