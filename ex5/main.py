def fibSequence(n):
    assert n > 0
    series = [1]
    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    for i in range(len(series)):
        series[i] = str(series[i])
    return (', '.join(series))


def fibRecurse(n):
    series = []
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    series = fibRecurse(n - 1)
    series.append(series[-1] + series[-2])
    return series


print(fibSequence(int(input('Сколько чисел в последовательности? '))))
print(', '.join(map(str, fibRecurse(int(input())))))
# print(fibRecurse(int(input('Какое число Фибоначчи вы хотите вычислить? '))))
