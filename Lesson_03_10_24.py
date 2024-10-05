########## Задание 6.1 ##########

# import string
# while True:
#     user_input = input("Введите диапазон букв: ")
#     start_letter = user_input[0]
#     end_letter = user_input[-1]
#     start_index = string.ascii_letters.index(start_letter)
#     end_index = string.ascii_letters.index(end_letter) + 1
#     alpha = string.ascii_letters[start_index:end_index]
#     print(alpha)
#     exit_the_program = input("Для окончания расчётов напишите -exit-, для продолжения нажмите -Enter- ")
#     if exit_the_program == "exit":
#         break

########## Задание 6.2 ##########

# while True:
#     while True:
#         try:
#             user_input = int(input("Введите секунды не более чем 8640000: "))
#             break
#         except ValueError:
#             print("Введите, пожалуйста, число!")
#     if abs(user_input) > 8640000:
#         print("Введите пожалуйста число соответствующее критериям")
#         continue
#     positive_input = abs(user_input)
#     count_day, remainder_d = divmod(positive_input, 86400)
#     coun_hour, remainder_h = divmod(remainder_d, 3600)
#     count_min, count_sec = divmod(remainder_h,60)
#     if count_day % 10 == 1 and count_day % 100 != 11:
#         day_word = "день"
#     elif count_day % 10 in [2, 3, 4] and count_day % 100 not in [12, 13, 14]:
#         day_word = "дня"
#     else:
#         day_word = "дней"
#     count_data = {
#         "day":count_day,
#         "count_word": day_word,
#         "hour":coun_hour,
#         "min":count_min,
#         "sec":count_sec,
#     }
#     time_parts = [
#         str(count_data['day']) + ' ' + count_data['count_word'],
#         str(count_data['hour']).zfill(2),
#         str(count_data['min']).zfill(2),
#         str(count_data['sec']).zfill(2),
#     ]
#     result = ' '.join(time_parts[:1]) + ' ' + ':'.join(time_parts[1:])
#     print(result)
#     exit_the_program = input("Для окончания расчётов напишите -exit-, для продолжения нажмите -Enter- ")
#     if exit_the_program == "exit":
#         break


########## Задание 6.3 ##########

# from functools import reduce
# while True:
#     try:
#         user_input = input("Введите числа: ")
#         user_list = [abs(int(x)) for x in user_input.split()]
#     except ValueError:
#         print("Вводите пожалуйста только числа!")
#         continue
#     result = reduce(lambda x, y: x * y, user_list)
#     while result > 9:
#         digits = [int(d) for d in str(result)]
#         result = reduce(lambda x, y: x * y, digits)
#     print(result)
#     exit_the_program = input("Для окончания расчётов напишите -exit-, для продолжения нажмите -Enter- ")
#     if exit_the_program == "exit":
#         break









