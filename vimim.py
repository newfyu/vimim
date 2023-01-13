import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
import subprocess

last_esc_press_time = None
ctl = Controller()

def is_abc():
    output = subprocess.Popen(["sh", "is_abc"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output_str,error_str = output.communicate()
    return output_str.decode("utf-8")


def on_press(key):
    global last_esc_press_time
    if key == keyboard.Key.esc and not is_abc():
        current_time = time.time()
        if last_esc_press_time is not None and current_time - last_esc_press_time < 0.5:
            ctl.press(Key.ctrl)
            ctl.press(Key.space)
            time.sleep(0.1)
            ctl.release(Key.ctrl)
            ctl.release(Key.space)
            print('快速按下esc键')
        last_esc_press_time = current_time

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
