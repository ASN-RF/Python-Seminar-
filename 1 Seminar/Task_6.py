# На столе стоит две корзины с яблоками. Корзина a и корзина b. Введите количество яблок с клавиатуры.
# Затем поменяйте содержимое корзин местами и выведите результат.
# Например, если пользователь ввёл 5 и 7, то до обмена a=5, b=7, а после a=7 и b=5.
from re import A


a = int(input('Здравствуйте!\nВведите количество яблок в первой корзине:\n a = '))
b = int(input('Теперь, введите количество яблок во второй корзине:\n b = '))
c = a
a = b
b = c
print(f'Итак, первоночально было:\na = {b}, b = {a}\nТеперь стало:\na = {a}, b = {b}')

