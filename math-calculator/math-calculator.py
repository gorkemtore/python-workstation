import math

def sum(*numbers):
    result = 0 
    for x in numbers:
        result += x

    return result

def diff(*numbers):
    """
        Bu fonksiyon verilen ilk değerden verilen diğer değerlerin her birisini cikartir. 
    
    """
    result = numbers[0]
    for i in range(1, len(numbers)):
        result -= numbers[i]

    return result

def pow(number1, number2):
    return int(math.pow(number1, number2))

def square(number):
    return math.sqrt(number)

def sinValue(angle):
    return math.sin(angle)

