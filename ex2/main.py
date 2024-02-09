import random
import string

list_of_words = [
    'яблоко', 'победа', 'код', 'терминал', 'ноутбук',
    'компьютер', 'интернет', 'база', 'данные', 'сервер',
    'монитор', 'клавиша', 'мышь', 'принтер', 'сканер',
    'процессор', 'плата', 'диск', 'память',
    'карта', 'модем', 'маршрут', 'сеть', 'блок',
    'корпус', 'вентилятор', 'радиатор', 'паста', 'охлаждение',
    'привод', 'флешка', 'карта', 'мышь', 'клавиатура'
]


def get_symbol(player, set_of_symbols, discovered_symbols):
    if player == 'Компьютер':
        return random.choice(list(set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') - discovered_symbols))
    else:
        while True:
            user_symbol = input(f'{player}, введите букву: ')
            if len(user_symbol) != 1 or user_symbol not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
                print('Пожалуйста, введите только одну кириллическую букву.')
            elif user_symbol in discovered_symbols:
                print('Вы уже вводили эту букву, попробуйте что-нибудь другое')
            else:
                return user_symbol


def play_game(players):
    word = random.choice(list_of_words)
    set_of_symbols = set(word)
    discovered_symbols = set()
    health = [5, 5]  # health for each player
    print('_ '*len(word))

    while discovered_symbols != set_of_symbols and all(h > 0 for h in health):
        for i, player in enumerate(players):
            if health[i] <= 0:
                break
            user_symbol = get_symbol(
                player, set_of_symbols, discovered_symbols)
            print(f'{player} выбрал букву: {user_symbol}')

            if user_symbol not in set_of_symbols:
                health[i] -= 1
                print(
                    f'Этой буквы нет в слове. Текущее кол-во жизней у {player}: {health[i]}')
                if health[i] == 0:
                    break
            else:
                print('Буква есть в слове!')
                discovered_symbols.add(user_symbol)

            current_word_progress = ''
            for ch in word:
                current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
            print(current_word_progress)

            if discovered_symbols == set_of_symbols:
                print(
                    f'Поздравляю, {player}, вы правильно набрали слово {word}')
                return player

    loser = [player for h, player in zip(health, players) if h == 0]
    if loser:
        print(f'{loser[0]}, жизни закончились :(')
        winner = [player for h, player in zip(health, players) if h > 0]
        print(f'Поздравляю, {winner[0]}, вы выиграли!')
        print(f'Загаданное слово было: {word}')


players = ['Игрок', 'Компьютер']
random.shuffle(players)

winner = play_game(players)
if winner:
    print(f'{winner} выиграл!')
