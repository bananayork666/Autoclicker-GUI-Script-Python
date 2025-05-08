import customtkinter as ctk
import pyautogui
import threading
import time

status = False

app = ctk.CTk()
app.geometry('300x300')
app._set_appearance_mode('dark')
app.resizable(False, False)

def autoclicker():
    global status
    status = True
    while status:
        pyautogui.click()
        time.sleep(0.1)

def start_clicker():
    thread = threading.Thread(target=autoclicker, daemon=True).start()
    print('Autoclicker has been activated')

def stop_clicker():
    global status
    status = False

def exit_soft():
    try:
        location = pyautogui.locateOnScreen('exit.png', confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print('Please move a window a little bit further from that location, unable to locate')
    else:
        x, y = location[0], location[1]
        y += 20
        x += 20
        pyautogui.click(x=x, y=y)

info_label = ctk.CTkLabel(app, text='Script of autoclicker', font=('Times New Roman', 16, 'bold'), width=35)
author = ctk.CTkLabel(app, text='kirwl.?', font=('Times New Roman', 15, 'bold'))
start_button = ctk.CTkButton(app, text='Start', bg_color='#242525', corner_radius=8, width=90, height=30, command=start_clicker)
stop_button = ctk.CTkButton(app, text='Stop', bg_color='#242525', corner_radius=8, width=90, height=30, command=stop_clicker)
exit_button = ctk.CTkButton(app, text='Exit', bg_color='#242525', corner_radius=8, width=90, height=30, command=exit_soft)

info_label.place(x=87, y=35)
author.place(x=130, y=70)
start_button.place(x=109, y=120)
stop_button.place(x=109, y=180)
exit_button.place(x=109, y=240)

app.mainloop()