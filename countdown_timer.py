import time
import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        mins = int(entry_min.get())
        secs = int(entry_sec.get())
        total_secs = mins * 60 + secs
        
        if total_secs <= 0:
            raise ValueError("Time must be greater than zero.")
        
        while total_secs > 0:
            mins, secs = divmod(total_secs, 60)
            time_format = f'{mins:02d}:{secs:02d}'
            label_time.config(text=time_format)
            root.update()
            time.sleep(1)
            total_secs -= 1
        
        messagebox.showinfo("Timer", "Time's up!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Countdown Timer")

frame = tk.Frame(root)
frame.pack()

label_min = tk.Label(frame, text="Minutes:")
label_min.grid(row=0, column=0)
entry_min = tk.Entry(frame, width=5)
entry_min.grid(row=0, column=1)

label_sec = tk.Label(frame, text="Seconds:")
label_sec.grid(row=0, column=2)
entry_sec = tk.Entry(frame, width=5)
entry_sec.grid(row=0, column=3)

label_time = tk.Label(root, font=('Helvetica', 48))
label_time.pack(pady=20)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=10)

root.mainloop()