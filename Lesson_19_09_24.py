user_number = input("Введите 4-х значное число: ")
dig_1 = int(user_number) // 1000
dig_2 = (int(user_number) % 1000) // 100
dig_3 = (int(user_number) % 100) // 10
dig_4 = int(user_number) % 10
print(dig_1)
print(dig_2)
print(dig_3)
print(dig_4)