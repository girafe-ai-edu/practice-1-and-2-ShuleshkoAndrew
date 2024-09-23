# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9
and make commit...
"""
def four_sum():
    print('Введите четырехзначное число')
    num = int(input())
    a = num % 10
    b = num // 10 % 10
    c = num // 100 % 10
    d = num // 1000
    return (f'{d} + {c} + {b} + {a} = {a + b + c + d}')

print(four_sum())