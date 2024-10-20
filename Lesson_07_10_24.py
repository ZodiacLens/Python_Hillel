# ########## Задание 7.1 ##########
#
# def say_hi(name, age):
#     say_hi = f"Hi. My name is {name} and I'm {age} years old"
#     return say_hi
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')
# #
# ######### Задание 7.2 ##########
#
# def correct_sentence(text):
#     text = text[0].upper() + text[1:]
#     if not text.endswith("."):
#         text += "."
#     return text
#
#
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')
#
# ######### Задание 7.3.1 ##########
#
# def second_index(text, some_str):
#     second_index = text.rfind(some_str)
#     if second_index == 0:
#         return None
#     else:
#         return second_index
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')
#
# ######### Задание 7.3.2 ##########
#
# def second_index(text, some_str):
#     first_index = text.find(some_str)
#     if first_index == -1:
#         return None
#     second_index = text.find(some_str, first_index + len(some_str))
#     if second_index == -1:
#         return None
#     return second_index
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')
#
# ######### Задание 7.4.1 (згенерує два списки елементів) ##########
#
# def common_elements():
#     list_1 = [symbol for symbol in range(100) if symbol % 3 == 0]
#     list_2 = [symbol for symbol in range(100) if symbol % 5 == 0]
#     set_1 = set(list_1)
#     set_2 = set(list_2)
#     set_end = set_1 & set_2
#     return set_end
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('OK')
#
# ########## Задание 7.4.2 ##########
#
# def common_elements():
#     set_1 = {symbol for symbol in range(100) if symbol % 3 == 0}
#     set_2= {symbol for symbol in range(100) if symbol % 5 == 0}
#     set_end = set_1 & set_2
#     return set_end
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('OK')