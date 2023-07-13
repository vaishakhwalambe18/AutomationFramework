class lib_math:
    @staticmethod
    def calculator(a, b, actiontoPerform):
        c = "No Output"
        if actiontoPerform== "add":
            c = a + b
        elif actiontoPerform=="sub":
            c = a - b
        elif actiontoPerform == "mul":
            c = a * b
        elif actiontoPerform=="div":
            c = a / b
        elif actiontoPerform == "mod":
            c = a % b

        return c

