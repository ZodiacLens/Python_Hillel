# ######### Задание 8.1 ##########
#
# def add_one(some_list):
#     new_number = int(''.join(map(str, some_list))) +1
#     new_list = list(map(int,str(new_number)))
#     return new_list
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")
#
# ######### Задание 8.2.1 import string ##########
#
# import string
# def is_palindrome(some_text):
#     clean_text = "".join(s for s in some_text if s not in string.punctuation).replace(" ", "").lower()
#     return clean_text == clean_text[::-1]
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")
#
# ######### Задание 8.2.2 import re ##########
#
# import re
# def is_palindrome(some_text):
#     clean_text = re.sub(r'[^a-zA-Z0-9]', '', some_text).lower()
#     return clean_text == clean_text[::-1]
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")
#
# ######### Задание 8.3  ##########
#
# def find_unique_value(some_list):
#     unique_value = None
#     for element in some_list:
#         if some_list.count(element) == 1:
#             unique_value = element
#     return unique_value
#
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")






