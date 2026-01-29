class solution:
    def calculator(self, a, b, operand):
        try:
            a,b = float(a), float(b)
            match operand:
                case "+": return a + b
                case "-": return a - b
                case "%": return a % b
                case "*": return a * b
                case _: print("Unknown operand.")

        except Exception as e:
            print(f"The error:: {e}")


if __name__ == "__main__":
    a = input("Enter first number:").strip()
    b = input("Enter second number:").strip()
    operand = input("Enter operand to perform operation (+, -, %, *):").strip()

    s = solution()
    ans = s.calculator(a,b,operand)
    print(f"Answer = {ans}")

