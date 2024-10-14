# ######### Задание 9.1 ##########
#
# def popular_words(text, words):
#     """
#     Counts how many times each word from a list appears in the given text.
#     Args:
#         text (str): The text to search within.
#         words (list): A list of words to count.
#     Returns:
#         dict: A dictionary with words as keys and their counts as values.
#               Words not found in the text will have a count of 0.
#     """
#     text_list = text.lower().split()
#     counts = {}
#     for word in words:
#         counts[word] = text_list.count(word.lower())
#     return counts
#
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
#                      ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
# print('OK')
#
#
#
#  ######### Задание 9.2 ##########
#
# def difference(*args):
#     """
#     Calculates the difference between the maximum and minimum values from the given arguments.
#     If no arguments are provided, returns 0.
#     Args:
#         *args: A variable number of numerical arguments.
#     Returns:
#         float: The rounded difference between the maximum and minimum values, or 0 if no arguments are provided.
#     """
#     result = 0
#     if args:
#         result = round(max(args) - min(args), 2)
#     return result
#
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')


