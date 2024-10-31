# ######## Задание 12.1 ##########
#
# import codecs
# import re
#
#
# def delete_html_tags(html_file, result_file='clean.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     clean_text = re.sub(r"<[^>]+>", "", html)
#
#     clean_text = re.sub(r"\n\s*\n", "\n", clean_text).strip()
#
#     lines = clean_text.splitlines()
#     lines = [line.strip() for line in lines]
#     clean_lines = lines[4:]
#
#     final_clean_text = "\n".join(clean_lines)
#
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(final_clean_text)
#
#
# delete_html_tags('draft.html', 'clean.txt')
#
# ######## Задание 12.2 ##########
#
# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}"
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname} phone № {self.numberphone}"
#
#     def without_phone(self):
#         return f"{self.name} {self.surname}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         items_str = "\n".join(f"{item.name}: {count} pcs." for item, count in self.products.items())
#         return f"Buyer: {self.user.without_phone()}\nItems:\n{items_str}"
#
#     def get_total(self):
#         total = sum(item.price * count for item, count in self.products.items())
#         return total
#
#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# banana = Item('banana', 4, "yellow", "long")
# print(lemon)
# print(apple)
# print(banana)
#
# buyer1 = User("Ivan", "Ivanov", "+380123456789")
# buyer2 = User("Alexander", "Macedonian", "+380123456789")
# print(f"Buyer №1: {buyer1}")
# print(f"Buyer №1: {buyer2}")
#
# cart = Purchase(buyer1)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
#
# cart2 = Purchase(buyer2)
# cart2.add_item(banana, 10)
# cart2.add_item(apple, 10)
# print(cart2)
#
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# print(f"Buyer {buyer1.without_phone()} total order cost {cart.get_total()} dollars")
# assert cart2.get_total() == 60, "Всього 60"
# print(f"Buyer {buyer2.without_phone()} total order cost {cart2.get_total()} dollars")
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# cart2.add_item(lemon, 10)
# print(cart)
# print(cart2)
#
# assert cart.get_total() == 40
# print(f"Buyer {buyer1.without_phone()} total order cost {cart.get_total()} dollars")
# assert cart2.get_total() == 110
# print(f"Buyer {buyer2.without_phone()} total order cost {cart2.get_total()} dollars")
