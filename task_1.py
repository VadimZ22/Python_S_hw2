# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

res = ''
n = int(input('enter a number'))
SYS = 16
num  = n
while num > 0:
    temp = str(num % SYS)
    match temp:
        case '10': temp = 'a'
        case '11': temp = 'b'
        case '12': temp = 'c'
        case '13': temp = 'd'
        case '14': temp = 'e'
        case '15': temp = 'f'

    res = temp + res
    num = num // SYS
print(res)

print(hex(n)[2:])
