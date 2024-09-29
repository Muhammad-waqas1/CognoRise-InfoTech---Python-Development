import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.config(bg="#2b2b2b")
        
        self.equation = ""

        # Display screen
        self.display = tk.Entry(root, font=('Arial', 24), bg='#111', fg='#fff', bd=0, justify='right', relief='sunken')
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipadx=8, ipady=25)

        # Button styles
        button_bg = "#333"
        button_fg = "#fff"
        button_hover_bg = "#555"
        button_active_bg = "#444"
        button_font = ('Arial', 18)

        # Creating buttons
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('Del', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        # Buttons to the GUI
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=button_font, bg=button_bg, fg=button_fg,
                               activebackground=button_active_bg, activeforeground='#fff',
                               command=lambda txt=text: self.on_button_click(txt))
            button.grid(row=row, column=col, padx=10, pady=10)

            # Hover effect to buttons
            button.bind("<Enter>", lambda e, b=button: b.config(bg=button_hover_bg))
            button.bind("<Leave>", lambda e, b=button: b.config(bg=button_bg))

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.equation))
                self.update_display(result)
                self.equation = result
            except Exception as e:
                self.update_display("Error")
                messagebox.showerror("Error", "Invalid expression!")
                self.equation = ""
        elif char == 'C':
            self.equation = ""
            self.update_display("")
        elif char == 'Del':
            self.equation = self.equation[:-1]
            self.update_display(self.equation)
        else:
            self.equation += str(char)
            self.update_display(self.equation)

    def update_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()