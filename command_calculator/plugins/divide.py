class DivideCommand:
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
