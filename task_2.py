# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def Find_Denom(x, y):
    denom = 0
    if x <= y:
        count = x
    else:
        count = y
    temp = count
    while denom == 0:
        if count % x == 0 and count % y == 0:
            denom = count
            return denom
        count += temp


def Sum_Find(a, b):
    res_denominator = Find_Denom(int(a[1]), int(b[1]))
    a_numerator = int(a[0]) * (res_denominator / int(a[1]))
    b_numerator = int(b[0]) * (res_denominator / int(b[1]))
    res_numerator = int(a_numerator + b_numerator)
    result = "/".join([str(res_numerator), str(res_denominator)])
    return result


def Mult_Find(a, b):
    res_numerator = int(a[0]) * int(b[0])
    res_denominator = int(a[1]) * int(b[1])
    result = "/".join([str(res_numerator), str(res_denominator)])
    return result



a = input('enter a: ').split('/')
b = input('enter b: ').split('/')
print(f"Сумма дробей: {Sum_Find(a, b)}")
print(f"Произведение дробей: {Mult_Find(a, b)}")

x = Fraction(int(a[0]), int(a[1]))
y = Fraction(int(b[0]), int(b[1]))
print(x + y)
print(x * y)