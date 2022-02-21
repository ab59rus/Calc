n = input('Введите число (stop - остановить)')
while n != 'stop':
    try:
        print('Квадрат числа', n, '=', int(n)**2)
    except:
        pass
    n = input('Введите число (stop - остановить)')
