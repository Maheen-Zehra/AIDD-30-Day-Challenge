def parse_expression(expression):
    # This is a very basic parser. It assumes well-formed expressions
    # without parentheses and simple integer/float numbers.
    # It will split numbers and operators.

    numbers = []
    operators = []
    current_number = ""

    i = 0
    if expression and expression[0] == '-':
        current_number += '-'
        i = 1

    while i < len(expression):
        char = expression[i]
        if char.isdigit() or char == '.':
            current_number += char
        elif char in ['+', '-', '*', '/']:
            if current_number:
                numbers.append(float(current_number))
                current_number = ""
            operators.append(char)
        elif char == ' ':
            pass
        else:
            raise ValueError("Invalid character in expression")
        i += 1

    if current_number:
        numbers.append(float(current_number))

    return numbers, operators
