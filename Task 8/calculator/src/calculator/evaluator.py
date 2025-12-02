def evaluate_expression(numbers, operators):
    if not numbers:
        raise ValueError("No numbers to evaluate")
    if len(numbers) != len(operators) + 1 and operators:
        raise ValueError("Mismatched numbers and operators")

    result = numbers[0]
    for i, operator in enumerate(operators):
        next_number = numbers[i + 1]
        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number
        elif operator == '*':
            result *= next_number
        elif operator == '/':
            if next_number == 0:
                raise ZeroDivisionError("Division by zero")
            result /= next_number
    return result
