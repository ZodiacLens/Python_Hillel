# ######## Задание 15.1 ##########
#
# import math
#
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.get_square() == other.get_square()
#
#     def __add__(self, other):
#         total_area = self.get_square() + other.get_square()
#         new_width = math.sqrt(total_area)
#         new_height = total_area / new_width
#         return Rectangle(new_width, new_height)
#
#     def __mul__(self, n):
#         new_area = self.get_square() * n
#         new_width = math.sqrt(new_area)
#         new_height = new_area / new_width
#
#         return Rectangle(new_width, new_height)
#
#     def __str__(self):
#         return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
#
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
#
# print("Все тесты пройдены.")
#
# ####### Задание 15.2 ##########
#
# import math
#
#
# class Fraction:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def simplify(self):
#         gcd = math.gcd(self.a, self.b)
#         self.a //= gcd
#         self.b //= gcd
#
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def __add__(self, other):
#         new_numerator = self.a * other.b + other.a * self.b
#         new_denominator = self.b * other.b
#         return Fraction(new_numerator, new_denominator)
#
#     def __sub__(self, other):
#         new_numerator = self.a * other.b - other.a * self.b
#         new_denominator = self.b * other.b
#         return Fraction(new_numerator, new_denominator)
#
#     def __eq__(self, other):
#         return self.a * other.b == self.b * other.a
#
#     def __gt__(self, other):
#         return self.a * other.b > other.a * self.b
#
#     def __lt__(self, other):
#         return self.a * other.b < other.a * self.b
#
#     def __str__(self):
#         return f"Fraction: {self.a}, {self.b}"
#
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 21, 18'
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 6, 18'
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 3, 18'
#
# assert f_d < f_c  # True
# assert f_d > f_e  # True
# assert f_a != f_b  # True
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2  # True
# print('OK')
