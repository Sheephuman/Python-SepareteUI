# controller.py
from model import CalculatorModel

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()

    def perform_operation(self, operation, a, b):
        if operation == "add":
            return self.model.add(a, b)
        elif operation == "subtract":
            return self.model.subtract(a, b)
        elif operation == "multiply":
            return self.model.multiply(a, b)
        elif operation == "divide":
            return self.model.divide(a, b)
