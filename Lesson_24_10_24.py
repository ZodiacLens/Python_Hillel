# ######## Задание 11.1 ##########
#
# from inspect import isgenerator
#
#
# def prime_generator(end):
#     for n in range(2, end + 1):
#         if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
#             yield n
#
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')
#
# ######## Задание 11.2 ##########
#
# from inspect import isgenerator
#
#
# def generate_cube_numbers(end):
#     limit = int(end ** (1 / 3)) + 1
#     for i in range(2, limit + 1):
#         new_i = i ** 3
#         if new_i <= end:
#             yield new_i
#
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('Ok')
#
#
# ######## Задание 11.3.1 ##########
#
# def is_even(number):
#     return (number & 1) == 0
#
#
# assert is_even(2494563894038 ** 2) == True, 'Test1'
# assert is_even(1056897 ** 2) == False, 'Test2'
# assert is_even(24945638940387 ** 3) == False, 'Test3'
# print('Ok')
#
#
# ######## Задание 11.3.2 ##########
#
# def is_even(number):
#     result = False
#     last_digit = str(number)[-1]
#     if last_digit in "2468":
#         result = True
#     return result
#
#
# assert is_even(2494563894038 ** 2) == True, 'Test1'
# assert is_even(1056897 ** 2) == False, 'Test2'
# assert is_even(24945638940387 ** 3) == False, 'Test3'
# print('Ok')
