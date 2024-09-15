# view.py
import tkinter as tk
from controller import CalculatorController

class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.controller = CalculatorController()

        # Entry fields for numbers
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=0, column=0, columnspan=2)

        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=1, column=0, columnspan=2)

        # Result label
        self.result_label = tk.Label(root, text="Result")
        self.result_label.grid(row=2, column=0, columnspan=2)

        # Buttons for operations
        self.add_button = tk.Button(root, text="Add", command=self.add)
        self.add_button.grid(row=3, column=0)

        self.subtract_button = tk.Button(root, text="Subtract", command=self.subtract)
        self.subtract_button.grid(row=3, column=1)

        self.multiply_button = tk.Button(root, text="Multiply", command=self.multiply)
        self.multiply_button.grid(row=4, column=0)

        self.divide_button = tk.Button(root, text="Divide", command=self.divide)
        self.divide_button.grid(row=4, column=1)

    def get_numbers(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            self.result_label.config(text="Error: Invalid input")
            return None, None

    def add(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            result = self.controller.perform_operation("add", a, b)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            result = self.controller.perform_operation("subtract", a, b)
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            result = self.controller.perform_operation("multiply", a, b)
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        a, b = self.get_numbers()
        if a is not None and b is not None:
            result = self.controller.perform_operation("divide", a, b)
            self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    view = CalculatorView(root)
    root.mainloop()
