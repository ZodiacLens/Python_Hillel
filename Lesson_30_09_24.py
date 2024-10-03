#  ########## Задание 5.1 ##########

# import keyword
# while True:
#     user_value = input("Введите имя переменной: ")
#     user_value_valid = True
#     if not user_value.isidentifier():
#         print("Переменная состоит из недопустимых символов или содержит пробелы.")
#         user_value_valid = False
#     if user_value in keyword.kwlist:
#         print("Переменная является зарезервированным словом")
#         user_value_valid = False
#     if user_value.count('_') > 1 and all(symbol == "_" for symbol in user_value):
#         print("Переменная является некорректной: состоит только из символов подчеркивания")
#         user_value_valid = False
#     if any(symbol.isupper() for symbol in user_value):
#         print("Переменная содержит заглавную букву")
#         user_value_valid = False
#     if user_value_valid:
#         print("Переменная корректна")
#     exit_the_program = input("Для окончания проверки напишите -exit-, для следующей нажмите -Enter- ")
#     if exit_the_program == "exit":
#         break

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

#  ########## Задание 5.3.1 ##########

# user_comment = "Should, I. subscribe? Yes!"
# clean_punct = user_comment.translate(str.maketrans("", "", ".,!?;:'\""))
# user_final_comment = "#" + clean_punct[:140].replace(" ", "").title()
# print(user_final_comment)


#  ########## Доп. ##########

# import caesar
# print(caesar)





