# 57th gthub project --> Stopwatch GUI
print('----------Stopwatch GUI----------')
import tkinter as tk
import time


def format_time(elapsed):
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    centiseconds = int((elapsed * 100) % 100)
    return f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}"


def update():
    if running[0]:
        elapsed[0] = time.time() - start_time[0]
        time_label.config(text=format_time(elapsed[0]))
        root.after(10, update)


def start():
    if not running[0]:
        running[0] = True
        start_time[0] = time.time() - elapsed[0]
        update()


def stop():
    if running[0]:
        running[0] = False


def reset():
    running[0] = False
    elapsed[0] = 0.0
    time_label.config(text=format_time(0.0))


root = tk.Tk()
root.title("Stopwatch")

elapsed = [0.0]
start_time = [0.0]
running = [False]

time_label = tk.Label(root, text=format_time(0.0),
                      font=("Consolas", 36), width=8)
time_label.pack(pady=15, padx=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start", width=8, command=start).pack(side="left", padx=5)
tk.Button(btn_frame, text="Stop", width=8, command=stop).pack(side="left", padx=5)
tk.Button(btn_frame, text="Reset", width=8, command=reset).pack(side="left", padx=5)

root.mainloop()