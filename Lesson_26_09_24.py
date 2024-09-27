# ########## Задание 4.1 ##########

# user_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# zero_index = 0
# zero_count = user_list.count(0)
# while zero_index < zero_count:
#     find_zero = user_list.index(0)
#     remove_element = user_list.pop(find_zero)
#     user_list.append(remove_element)
#     zero_index += 1
# print(user_list)

# ########## Задание 4.1.2 ##########

# user_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# for _ in range(user_list.count(0)):
#     user_list.remove(0)
#     user_list.append(0)
# print(user_list)

# ########## Задание 4.1.3 ##########

# user_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# non_zero_list = list(filter(lambda x: x != 0, user_list))
# zero_count = user_list.count(0)
# user_list = non_zero_list
# user_list.extend([0] * zero_count)
# print(user_list)

# ########## Задание 4.1.4 ##########

# user_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# zero_count = user_list.count(0)
# user_list = [dig for dig in user_list if dig != 0]
# user_list.extend([0] * zero_count)
# print(user_list)

# ########## Задание 4.2 ##########

# user_list = [1, 3, 5]
# if user_list:
#     even_list_sum = sum(user_list [::2])
#     final_result = user_list[-1] * even_list_sum
#     print(final_result)
# else:
#     print(user_list)

# ########## Задание 4.3 ##########

# user_list = [6, 3, 7]
# new_list = [user_list[0], user_list[2],  user_list[-2]]
# print(new_list)
