string1=str(input('Введите строку: '))
string2=str(input('Введите еще одну строку: '))

if string1 != string2 and string2 == 'learn':
    print(1)
elif string1 != string2 and len(string1) > len(string2):
    print(2)
elif string1 == string2:
    print(3)
else:
    print(4)
