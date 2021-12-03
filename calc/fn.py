def equals(bufer):
    
    
    result = 0
    number = 0
    operator = ''

    for element in bufer:
        
        if element.isdigit():
            number = int(element)
            if operator == '+':
                result += number
            elif operator == '-':
                result -= number
            elif operator == '*':
                result *= number
            elif operator == '/':
                result /= number
            else:
                result = number
        else:
            operator = element

    return result