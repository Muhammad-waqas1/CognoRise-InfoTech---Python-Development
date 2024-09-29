import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("410x450")
        self.root.config(bg="#222")
        self.root.resizable(False, False)

        self.timer_running = False

        # Title label
        self.title_label = tk.Label(root, text="Countdown Timer", font=("Arial", 24, "bold"), fg="#f7f7f7", bg="#222")
        self.title_label.pack(pady=20)

        # Timer display with milliseconds
        self.time_display = tk.Label(root, text="00:00:00.000", font=("Arial", 48, "bold"), fg="#f7f7f7", bg="#222")
        self.time_display.pack(pady=20)

        # Hour, Minute, Second inputs
        self.time_frame = tk.Frame(root, bg="#222")
        self.time_frame.pack(pady=10)

        self.hour_var = tk.StringVar(value="00")
        self.minute_var = tk.StringVar(value="00")
        self.second_var = tk.StringVar(value="00")

        self.hour_entry = self.create_time_entry(self.time_frame, self.hour_var, "Hours")
        self.minute_entry = self.create_time_entry(self.time_frame, self.minute_var, "Minutes")
        self.second_entry = self.create_time_entry(self.time_frame, self.second_var, "Seconds")

        # Start and Reset buttons
        self.button_frame = tk.Frame(root, bg="#222")
        self.button_frame.pack(pady=20)

        self.start_button = tk.Button(self.button_frame, text="Start", font=("Arial", 16, "bold"), bg="#28a745", fg="#fff",
                                      activebackground="#218838", activeforeground="#fff", width=10, command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", font=("Arial", 16, "bold"), bg="#dc3545", fg="#fff",
                                      activebackground="#c82333", activeforeground="#fff", width=10, command=self.reset_timer)
        self.reset_button.grid(row=0, column=1, padx=10)

        # Hover effects
        self.add_hover_effect(self.start_button, "#218838", "#28a745")
        self.add_hover_effect(self.reset_button, "#c82333", "#dc3545")

    def create_time_entry(self, frame, var, label_text):
        # Frame for input
        entry_frame = tk.Frame(frame, bg="#222")
        entry_frame.pack(side="left", padx=10)

        label = tk.Label(entry_frame, text=label_text, font=("Arial", 12), fg="#f7f7f7", bg="#222")
        label.pack()

        entry = tk.Entry(entry_frame, font=("Arial", 24), width=3, justify="center", textvariable=var, bg="#333", fg="#fff", bd=0, relief="sunken")
        entry.pack(pady=5)
        return entry

    def add_hover_effect(self, button, hover_bg, normal_bg):
        button.bind("<Enter>", lambda e: button.config(bg=hover_bg))
        button.bind("<Leave>", lambda e: button.config(bg=normal_bg))

    def start_timer(self):
        if not self.timer_running:
            try:
                hours = int(self.hour_var.get())
                minutes = int(self.minute_var.get())
                seconds = int(self.second_var.get())
                total_seconds = hours * 3600 + minutes * 60 + seconds

                if total_seconds > 0:
                    self.timer_running = True
                    self.countdown(total_seconds, 999)  # Start the countdown with 999 milliseconds
                else:
                    messagebox.showwarning("Invalid Time", "Please set a valid countdown time.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numeric values for time.")
    
    def countdown(self, remaining_seconds, millis):
        if self.timer_running:
            if remaining_seconds > 0 or millis > 0:
                if millis < 0:  # When milliseconds run out, decrease seconds and reset millis to 999
                    remaining_seconds -= 1
                    millis = 999

                if remaining_seconds >= 0:  # Ensure countdown happens only when time is remaining
                    hours = remaining_seconds // 3600
                    minutes = (remaining_seconds % 3600) // 60
                    seconds = remaining_seconds % 60

                    self.time_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}")
                    self.root.after(1, self.countdown, remaining_seconds, millis - 1)
            else:
                self.time_up()  # Trigger "Time's up" message when both seconds and millis reach 0

    def time_up(self):
        self.timer_running = False
        self.time_display.config(text="00:00:00.000")
        messagebox.showinfo("Time's up", "Countdown finished!")

    def reset_timer(self):
        self.timer_running = False
        self.time_display.config(text="00:00:00.000")
        self.hour_var.set("00")
        self.minute_var.set("00")
        self.second_var.set("00")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()