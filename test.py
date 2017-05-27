
number=input('Введите число от 1 до 10: ')
if isinstance(number, int) is True:
    if number < 10 and number > 0:
        print('Молодец')
    elif number > 10:
        print('многова-то')
    elif number < 0:
        print('малова-то')
elif isinstance(number, int) is False:
	print('Вы ввели что-то не то.')