# ######### Задание 10.1 ##########
#
# def square(x):
#     return x ** 2
#
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     value_count = 1
#     while value_count <= end:
#         yield begin
#         begin = func(begin)
#         value_count += 1
#
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')
#
#
# ######## Задание 10.2.1 ##########
#
# def first_word(text):
#     """ Пошук першого слова """
#     text = text.replace(",", " ").replace(".", " ")
#     for word in text.split():
#         if word[0].isalpha():
#             return word
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')
#
#
# ######## Задание 10.2.2 ##########
#
# def first_run_generator(my_gen):
#     def wrapper(*args):
#         generator = my_gen(*args)
#         first_word_text = next(generator)
#         return first_word_text
#
#     return wrapper
#
#
# @first_run_generator
# def first_word(text):
#     """ Пошук першого слова """
#     text = text.replace(",", " ").replace(".", " ")
#     for word in text.split():
#         if word[0].isalpha():
#             yield word
#
#
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')
#
#
# ######## Задание 10.3 ##########
#
# def is_even(digit):
#     """ Перевірка чи є парним число """
#     quotient, remainder = divmod(digit, 2)
#     return remainder == 0
#
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
