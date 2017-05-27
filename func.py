age=int(input('Введите ссвой возраст: '))
if age < 7 and age >= 3:
    print('Сад')
elif age >= 7 and age < 17:
    print('Школа')
elif age >= 17 and age < 23:
    print('ВУЗ')
elif age >= 23 and age < 60:
    print('Работа')
else:
    print('Что-нибудь еще')
