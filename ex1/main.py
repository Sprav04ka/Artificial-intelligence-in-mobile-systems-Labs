import random

# Начало и конец интервала
A = 1
B = 100

# Компьютер и пользователь загадывают числа
comp_number = random.randint(A, B)
print('Загадайте число от 1 до 100.')

# Компьютер делает первую догадку
comp_guess = random.randint(A, B)

while True:
    # Ход пользователя
    while True:
        try:
            user_guess = int(input('Ваша догадка: '))
            break
        except ValueError:
            print('Пожалуйста, введите число.')

    if comp_number > user_guess:
        print('Мое число больше, чем {}!'.format(user_guess))
    elif comp_number < user_guess:
        print('Мое число меньше, чем {}!'.format(user_guess))
    else:
        print('Верно! Вы угадали мое число {}'.format(comp_number))
        print('Вы выиграли!')
        break

    # Ход компьютера
    while True:
        print(
            f'Моя догадка: {comp_guess}. Ваше число больше, меньше или я угадал?')
        user_hint = input('> ').lower()

        if user_hint == 'больше':
            if comp_guess == B:
                print('Вы сказали, что ваше число больше, чем мое предположение, но это невозможно, так как мое предположение уже равно верхней границе интервала. Пожалуйста, проверьте свой ответ.')
                continue
            A = comp_guess + 1
        elif user_hint == 'меньше':
            if comp_guess == A:
                print('Вы сказали, что ваше число меньше, чем мое предположение, но это невозможно, так как мое предположение уже равно нижней границе интервала. Пожалуйста, проверьте свой ответ.')
                continue
            B = comp_guess - 1
        elif user_hint == 'угадал':
            print('Ура! Я угадал ваше число!')
            print('Я выиграл!')
            break
        else:
            print(
                'Извините, я не понял ваш ответ. Пожалуйста, ответьте "больше", "меньше" или "угадал".')
            continue

        break  # Завершаем ход компьютера после каждой попытки угадать число

    # Если компьютер угадал число пользователя, игра завершается
    if user_hint == 'угадал':
        break

    # Компьютер делает следующую догадку
    comp_guess = random.randint(A, B)
