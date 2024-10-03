#  ########## Задание 5.1 ##########

# while True:
#     user_value = input("Введите имя переменной: ")
#     import string
#     import keyword
#     if user_value[0].isdigit():
#         print("Переменная начинается с цифры")
#     elif user_value in keyword.kwlist:
#         print("Переменная является зарезервированным словом")
#     elif all(symbol == "_" for symbol in user_value) and len(user_value) > 1:
#         print("Переменная является некорректной, более чем 1 '_'")
#     elif any(symbol.isupper() for symbol in user_value):
#          print("Переменная содержит заглавную букву")
#     elif any(symbol in string.punctuation and symbol != '_' for symbol in user_value):
#         print("Переменная состоит из недопустимых символов")
#     elif any(symbol.isspace() for symbol in user_value):
#         print("Переменная содержит пробел")
#     else:
#         print("Переменная корректна")
#     exit_the_program = input("Для окончания прверки напишите -exit-, для следующей нажмите -Enter- ")
#     if exit_the_program == "exit":
#             break

#  ########## Задание 5.2 ##########

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
#     while True:
#         operation = input("Введите действие, которое хотите применить (+, -, *, /): ")
#         if operation not in ("+", "-", "/", "*"):
#             print("Выберите действие из предложенных.")
#             continue
#         if operation == "+":
#             result = user_digit_1 + user_digit_2
#         elif operation == "-":
#             result = user_digit_1 - user_digit_2
#         elif operation == "*":
#             result = user_digit_1 * user_digit_2
#         elif operation == "/":
#             if user_digit_2 == 0:
#                 print("Деление на ноль невозможно")
#                 continue
#             result = user_digit_1 / user_digit_2
#         break
#     print("Результат: ", result)
#     exit_the_program = input("Для продолжения расчсётов напишите 'yes': ")
#     if exit_the_program != "yes":
#         break

#  ########## Задание 5.3 ##########

# import string
# user_comment = "Should, I. subscribe? Yes!"
# clean_punct = "".join(symbol for symbol in user_comment if symbol not in string.punctuation)
# user_final_comment = "#" + clean_punct[:140].title().replace(" ", "")
# print(user_final_comment)

#  ########## Доп. ##########

# import caesar
# print(caesar)
