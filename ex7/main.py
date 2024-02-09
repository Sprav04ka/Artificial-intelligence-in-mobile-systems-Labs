def calc(a, b, op):
    if op not in '+-/*^%√':
        return 'Пожалуйста, выберите тип операции: "+, -, *, /, ^, %, √"!'
    if op == '+':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))
    if op == '^':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** b))
    if op == '%':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b / 100))
    if op == '√':
        return ('√' + str(a) + ' = ' + str(a ** 0.5))


def main():
    a = int(input('Пожалуйста, введите первое число: '))
    b = int(input('Пожалуйста, введите второе число: '))
    op = input(
        'Какой вид операции Вы желаете осуществить?\\nВыберите между "+, -, *, /, ^, %, √" : ')
    print(calc(a, b, op))


if __name__ == '__main__':
    main()
