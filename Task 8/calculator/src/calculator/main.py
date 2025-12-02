from .parser import parse_expression
from .evaluator import evaluate_expression

def main():
    expression = input("Enter expression: ")
    try:
        numbers, operators = parse_expression(expression)
        result = evaluate_expression(numbers, operators)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
