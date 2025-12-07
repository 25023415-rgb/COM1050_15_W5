a, b = map(float, input().split())
op = input()
def maytinhbotui(num1, num2, operat):
    result = 0
    if operat == '+':
        result = num1 + num2
    elif operat == '-':
        result = num1 - num2
    elif operat == '*':
        result = num1 * num2
    elif operat == '/':
        if num2 == 0:
            return "không thể chia cho 0"
        result = num1 / num2
    return round(result, 2)
        