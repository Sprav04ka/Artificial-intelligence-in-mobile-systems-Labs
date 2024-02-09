def isPrime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True


def genNextPrime(currentPrime):
    newPrime = currentPrime + 1
    while True:
        if not isPrime(newPrime):
            newPrime += 1
        else:
            break
    return newPrime


def genPrevPrime(currentPrime):
    newPrime = currentPrime - 1
    while True:
        if not isPrime(newPrime):
            newPrime -= 1
        else:
            break
    return newPrime


while True:
    num = input('Введите число: ')
    if num.isdigit():
        num = int(num)
        if isPrime(num):
            print(f"{num} - простое число.")
        else:
            print(f"{num} - не является простым числом.")
            next_prime = genNextPrime(num)
            prev_prime = genPrevPrime(num)
            if abs(num - next_prime) < abs(num - prev_prime):
                print(f"Ближайшее простое число: {next_prime}")
            else:
                print(f"Ближайшее простое число: {prev_prime}")
    else:
        print("Пожалуйста, введите целое число.")
