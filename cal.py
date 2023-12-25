import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("My Calculator")
        root.geometry("400x600")

        # Entry widget to display input and output
        self.display = tk.Entry(root, font=('Arial', 24), justify='left', bd=40, insertwidth=4, width=14)
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3),
            ('(', 6, 0), (')', 6, 1), ('^', 6, 2), ('Clear', 6, 3),
        ]

        # Create buttons and add them to the grid
        for (text, row, col) in buttons:
            button_color = 'green' if text == '=' else 'yellow' if text in ('/', '*', '-', '+') else 'white'
            button = tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t), bg=button_color)
            button.grid(row=row, column=col, sticky='news')

        # Configure row and column weights
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        current_display = self.display.get()

        if value == "=":
            try:
                result = eval(current_display)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "Clear":
            self.display.delete(0, tk.END)
        elif value == "sin":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.sin(math.radians(float(current_display)))))
        elif value == "cos":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.cos(math.radians(float(current_display)))))
        elif value == "tan":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.tan(math.radians(float(current_display)))))
        elif value == "sqrt":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.sqrt(float(current_display))))
        elif value == "^":
            self.display.insert(tk.END, "**")
        else:
            self.display.insert(tk.END, value)

# Main function to run the calculator
def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
