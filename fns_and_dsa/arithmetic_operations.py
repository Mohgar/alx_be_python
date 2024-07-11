def perform_operation (num1 , num2, operation):
    num1 = float()
    num2 = float()
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Its not allowed for division by zero"
            else:
                return num1 / num2
        case _:
            return "Invalid operation"







