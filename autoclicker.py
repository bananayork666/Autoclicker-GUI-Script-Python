import customtkinter as ctk
import pyautogui
import threading
import time
from pynput import keyboard

status = False
clicker_thread = None

app = ctk.CTk()
app.geometry('300x400')
app._set_appearance_mode('dark')
app.resizable(False, False)
app.title("Autoclicker v2.0")


def autoclicker():
    global status
    status = True
    print(f'Autoclicker ATIVADO. Pressione f2 para parar.')

    while status:
        pyautogui.click()
        try:
            interval = speed_slider.get()
            time.sleep(interval)
        except Exception as e:
            print(f"Error in thread (UI closed?): {e}")
            status = False


def start_clicker():
    global status, clicker_thread
    
    if clicker_thread is None or not clicker_thread.is_alive():
        clicker_thread = threading.Thread(target=autoclicker, daemon=True)
        clicker_thread.start()
        print('Autoclicker thread started.')
    else:
        print('Autoclicker is already running.')


def stop_clicker():
    global status
    if status:
        status = False
        print('Autoclicker DEACTIVATED.')
    else:
        print('Autoclicker was already stopped.')


def exit_soft():
    print("Closing application...")
    stop_clicker()
    app.destroy()


# Hotkey (pynput) listener setup

def on_press(key):
    try:
        if key == keyboard.Key.f1:
            start_clicker()
        elif key == keyboard.Key.f2:
            stop_clicker()
    except Exception as e:
        print(f"Error in hotkey handler: {e}")


def start_key_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    print("Keyboard listener finished.")



info_label = ctk.CTkLabel(app, text='Autoclicker Script', font=('Times New Roman', 16, 'bold'))
info_label.pack(pady=(20, 5))

author = ctk.CTkLabel(app, text='kirwl.? (Modified)', font=('Times New Roman', 15, 'bold'))
author.pack(pady=5)

start_button = ctk.CTkButton(app, text='Start (F1)', command=start_clicker)
start_button.pack(pady=10, ipadx=10)

stop_button = ctk.CTkButton(app, text='Stop (F2)', command=stop_clicker)
stop_button.pack(pady=10, ipadx=10)

slider_label = ctk.CTkLabel(app, text='Interval: 0.10s')
slider_label.pack(pady=(15, 0))

def update_slider_label(value):
    slider_label.configure(text=f'Interval: {value:.2f}s')

speed_slider = ctk.CTkSlider(app, from_=0.01, to=2.0, command=update_slider_label)
speed_slider.set(0.1)
speed_slider.pack(pady=5, padx=30, fill="x")

exit_button = ctk.CTkButton(app, text='Exit', command=exit_soft, 
                          fg_color="#D32F2F", hover_color="#B71C1C")
exit_button.pack(pady=(20, 10), ipadx=10)

listener_thread = threading.Thread(target=start_key_listener, daemon=True)
listener_thread.start()
# Fix: log updated
print("Hotkey listener activated: F1 (Start) | F2 (Stop)")

app.mainloop()
