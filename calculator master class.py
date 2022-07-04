while True:
    a = float(input('Введите первое число - '))
    b = input('Введите операцию (+,-,*,/) - ')
    c = float(input('Введите второе число - '))

    if b == '+':
        ansewr = a+c
        print(ansewr)

    elif b == '-':
        ansewr = a-c
        print(ansewr)

    elif b == '*':
        ansewr = a*c
        print(ansewr)

    elif b == '/' and c == 0:
        print('На ноль делить нельзя')

    elif b == '/':
        ansewr = a/c
        print(ansewr)

    else:
        print('Не опознанная операция!')




