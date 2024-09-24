########## Задание 3.1 ##########

while True:
    user_digit_1 = float(input("Введите цифру или число №1: "))
    user_digit_2 = float(input("Введите цифру или число №2: "))
    operation  = input("Введите действие которое хотите применить (+, -, *, /): ")
    if operation == "+":
        result_1 = (user_digit_1) + (user_digit_2)
        print (result_1)
    elif operation == "-":
        result_2 = (user_digit_1) - (user_digit_2)
        print(result_2)
    elif operation == "*":
        result_3 = (user_digit_1) * (user_digit_2)
        print(result_3)
    elif operation == "/" and user_digit_2 != 0:
        result_4 = (user_digit_1) / (user_digit_2)
        print(result_4)
    elif operation == "/" and user_digit_2 == 0:
        print("Деление на ноль невозможно")
    else:
        print ("Выберите действие из предложенных.")
    exit_the_program = input("Для окончания расчётов напишите -exit- для продолжения нажмите -Enter- ")
    if exit_the_program == "exit":
        break

########## Задание 3.2 ##########
# Условие №1
some_list_1 = [12, 3, 4, 10]
last_el = some_list_1.pop()
some_list_1.insert(0, last_el)
print(some_list_1)
# Условие №2
some_list_2 = [1]
last_el = some_list_2.pop()
some_list_2.insert(0, last_el)
print(some_list_2)
# Условие №3
some_list_3 = []
if some_list_3:
    last_el = some_list_3.pop()
    some_list_3.insert(0, last_el)
    print(some_list_3)
else:
    print(some_list_3)
# Условие №4
some_list_4 = [12, 3, 4, 10, 8]
last_el = some_list_4.pop()
some_list_4.insert(0, last_el)
print(some_list_4)


########## Задание 3.3 ##########
# Условие №1
some_list_1 = [1,2,3,4,5,6]
new_list_1 = some_list_1[0:3]
new_list_2 = some_list_1[3:6]
new_list_3 = [new_list_1, new_list_2]
print(new_list_3)
# Условие №2
some_list_1 = [1,2,3]
new_list_1 = some_list_1[0:2]
new_list_2 = some_list_1[2:3]
new_list_3 = [new_list_1, new_list_2]
print(new_list_3)
# Условие №3
some_list_1 = [1,2,3,4,5]
new_list_1 = some_list_1[0:3]
new_list_2 = some_list_1[3:5]
new_list_3 = [new_list_1, new_list_2]
print(new_list_3)
# Условие №4
some_list_1 = [1]
new_list_1 = some_list_1[0]
new_list_2 = []
new_list_3 = [new_list_1, new_list_2]
print(new_list_3)
# Условие №5
some_list_1 = []
if some_list_1:
    new_list_1 = some_list_1
    new_list_2 = []
else:
    new_list_1 = []
    new_list_2 = []
new_list_3 = [new_list_1, new_list_2]
print(new_list_3)