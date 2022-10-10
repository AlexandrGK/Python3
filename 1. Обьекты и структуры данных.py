# Типы данных
'''
intgers - int Целые числа 3,300,200
Floating point - float Числа с плавающей точкой 2,3 4,5 100,0
String - строки - str Упорядоченная последовательность символов 'hello' 'Sam'
Lists - списки [list] Упорядоченная последовательность обьектов [10,'hello'.200,1]
Dictionaries - словари dict Неупорядоченные пары Ключ:Значение {'mykey'
:'value','name':'David'}
Tuples - кортежи tup Упорядоченная неизменяемая последовательность обьектов (10,'hello',200,1)
Sets -множество set Неупорядоченный набор уникальных обьектов {'a','b'}
Booleans bool Логическое значение - True (истино) или False (ложно)
'''
# Числа

# print(2+1)
# print(6-1)
# print(2*3)
# print(9 % 4)
# print(2 ** 3)

# Присвоение переменных
# Python использует динамическую типизацию

# my_dogs = 2
# my_dogs=['Sammy','Sam']
# a = 10
# a + a
# a = a + a
# a
# print(type(a))
# my_income = 100
# tax_rate = 0.1
# my_taxes = my_income * tax_rate
# print(my_taxes)

# Strings - Строки

# 'hello'
# "hello"
# "I'm going on a run"
# print('hello')
# print('hello \nworld')
# print('hello \tworld')
# print(len('hello'))

# Индексирование и срезы строк

# mystring = 'Hello World'
# print(mystring[0])
# print(mystring[0:3])
# print(mystring[::-1]) # инверсия строки

# mystring = 'advmnbfkf'
# print(mystring[2:])
# print(mystring[:3])
# print(mystring[::2]) # с шагом

# Свойства и методы для строк
# name = 'Sam'
# # name[0] = 'P'  # (Строки не изменны)
# lasst_letters = name[1:]
# print(lasst_letters)
# print('P' + lasst_letters) # Конкотенация строк

# x = 'Hello World'
# x = x + 'it is beautiful outside!'
# print(x)

# letter = 'z'
# print(letter * 10)
# x = 'Hi this is a string'
# print(x.split())
# print(x.split('i'))

#  Форматирование Вывода для строк

# my_name = 'Vlad'
# print('Hello ' + my_name)
#
# print('Эта строка была{}'.format('добавлена'))
# print('У меня есть {2} {1} {0}'.format('вкусное','красное','яблоко'))
# print('У меня есть {v} {k} {y}'.format(v ='вкусное',k = 'красное',y = 'яблоко'))

# Форматирование Float с помощью "{value:width.precision f}"

# result = 100/77
# # print(result)
# print('{}'.format(result))
# print('Результат: {r}'.format(r=result))
# print('Результат: {r:1.3f}'.format(r=result))
# name = 'Vlad'
# print('Имя:{}'.format(name))
# print(f'Имя: {name}')

# Списки [1,2,3,4,5]

# my_lyst = [1,2,3]
# my_list = ['String',100,23.2]
# print(len(my_list))
# my_lyst = ['one','two','three']
# print(my_lyst[1:])
# my_lyst[0] = 'Hallo'
# print(my_lyst)
# my_lyst.append('SIX')
# print(my_lyst)
# print(my_lyst.pop())
# print(my_lyst)
# print(my_lyst.pop(0))
# print(my_lyst)

# new_list = ['a','b','x','g','d']
# new_list.sort()
# list = new_list
# print(list)
# new_list.reverse()
# print(new_list)
