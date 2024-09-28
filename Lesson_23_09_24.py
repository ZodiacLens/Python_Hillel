# ########## Задание 3.1 ##########
#
# while True:
#     while True:
#         try:
#             user_digit_1 = float(input("Введите цифру или число №1: "))
#             break
#         except ValueError:
#             print("Введите, пожалуйста, число или цифру.")
#     while True:
#         try:
#             user_digit_2 = float(input("Введите цифру или число №2: "))
#             break
#         except ValueError:
#             print("Введите, пожалуйста, число или цифру.")
#     operation = input("Введите действие, которое хотите применить (+, -, *, /): ")
#     if operation == "+":
#         result = user_digit_1 + user_digit_2
#         print("Резульат: ", result)
#     elif operation == "-":
#         result = user_digit_1 - user_digit_2
#         print("Резульат: ", result)
#     elif operation == "*":
#         result = user_digit_1 * user_digit_2
#         print("Резульат: ", result)
#     elif operation == "/" and user_digit_2 != 0:
#         result = user_digit_1 / user_digit_2
#         print("Резульат: ", result)
#     elif operation == "/" and user_digit_2 == 0:
#         print("Деление на ноль невозможно")
#     else:
#         print("Выберите действие из предложенных.")
#     exit_the_program = input("Для окончания расчётов напишите -exit-, для продолжения нажмите -Enter- ")
#     if exit_the_program == "exit":
#         break
#
# ########## Задание 3.2 ##########
#
# some_list = [12,3,4,8,10]
# if some_list:
#     last_el = some_list.pop()
#     some_list.insert(0, last_el)
#     print(some_list)
# else:
#     print(some_list)
# #
# # ########## Задание 3.3 ##########
# #
# some_list_1 = [1,2,3,4,5]
# if some_list_1:
#     mid_of_list = (len(some_list_1) + 1) // 2
#     new_list_1 = some_list_1[:mid_of_list]
#     new_list_2 = some_list_1[mid_of_list:]
# else:
#     new_list_1 = some_list_1
#     new_list_2 = []
# new_list_3 = (new_list_1, new_list_2)
# print(new_list_3)

