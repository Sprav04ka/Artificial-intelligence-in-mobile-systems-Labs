import random
import string
import json
import os


def generate_password():
    """Генерирует случайный пароль."""
    password = []
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))  # uppercase
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))  # lowercase
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))  # digits
    for i in range(random.randint(2, 4)):
        password.append(random.choice(string.punctuation))  # special
    random.shuffle(password)
    return ''.join(password)


def main():
    """Основная функция программы."""
    data = []
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as f:
            data = json.load(f)
    while True:
        site = input('Введите сайт (или "q" для выхода): ')
        if site.lower() == 'q':
            break
        login = input('Введите логин: ')
        password = generate_password()
        data.append({'site': site, 'login': login, 'password': password})
        print(f'Пароль для {login} на сайте {site} сохранен.')
    with open('passwords.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
