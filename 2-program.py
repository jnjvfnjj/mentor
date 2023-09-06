while True:
    num = int(input('введите число: '))
    if num == 0:
        break
    elif num % 2 == 0:
        print("число четное")
        if num % 3 == 0:
            print('число кратно 3')
    elif num % 2 != 0:
        print('число не четное')
        if num % 3 == 0:
            print('число кратно 3')

    else:
        print('ошибка')