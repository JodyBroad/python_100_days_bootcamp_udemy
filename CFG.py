# name = 'Joanna'f'My friend {name} is coming for dinner tonight.' - error
# print('My friend {} is coming for dinner tonight.'.format('Joanna'))
# print(name = 'Joanna "My friend' + name + 'is coming for dinner tonight.') - error
# print(name = 'Joanna"My friend %s is coming for dinner tonight.' % name) - error
# name='Joanna'
# print("My friend `(name)` is coming for dinner tonight.")

# start = 'CodeFirstGirls'
# result = start[1:-1:2]
# print(result)

# vat = 0.2 #20%
# discount = 0 #GBP
# price = float(input("Please enter the item price: "))
# full_price = (price * vat) + price #including vat
# if full_price >= 50:
#     discount = 5 #GBP
#
# total = full_price - discount
# print(total)

# vat = 0.2 #20%
# discount = 0 #GBP
# price = input("Please enter the item price: ")
# full_price = (price * vat) + price #including vat
# if full_price >= 50:
#     discount = 5 #GBP
#
# total = full_price - discount
# print(total)

# vat = 0.2 #20%
# discount = 0 #GBP
# price = float(input("Please enter the item price: "))
# full_price = (price * vat) + price #including vat
# if not full_price >= 50:
#     discount = 5 #GBP
#
# total = full_price - discount
# print(total)

# total = 0
# for num in range(1, 6):
#     total += num
#     print(total)
# print(total)

# input = 15
#
# if input % 2 ==0:
#     input = input ** 2
#
# print(input)

# input = 15
#
# if input // 2 ==0:
#     input = input ** 2
#
# print(input)

# input = 15
#
# if input % 2 != 0:
#     input = input ** 2
#
# print(input)

# numbers = [num for num in range(5) if 0 < num < 4]
# count = 0
# result = 20
#
# while count < len(numbers):
#     result = result - numbers[count]
#     count += 1
#
# print(result)
#
# def process_word(word):
#     output = list(word)
#     output.reverse()
#     new_word = "".join(output)
#     print(new_word)
#
# result = process_word('monkey')

# def calc_factorial(n):
#     fact = 1
#     for num in range(2, n + 1):
#         fact *= num
#     return fact
#
#
# def my_function(numbers):
#     my_container = []
#     for num in numbers:
#         my_container.append(calc_factorial(num))
#     return my_container[::-1]
#
#
# result = my_function((1,2,3))
# print(result)

# dog_size = int(input('How big is the dog? '))
#
# if dog_size > 75:
#     print('That is a big dog')
#
# elif dog_size < 10:
#     print('That dog could fit in my pocket')
#
# elif dog_size < 25:
#     print('That is a small dog')
#
# else:
#     print('That is an average dog')

# my_dict = {
# 'dog' : 'billy',
# 'cat' : 'pepe'
# }
#
# result = [v.capitalize() for k,v in my_dict.items()]
# print(result)
#
# my_fruit = {"apple", "banana", "orange"}
#
# my_fruit.pop()
#
# print(my_fruit)
#
# menu = ('croissant', 'coffee', 'juice')
#
# menu[1] = ['tea', 'juice']
# print(menu)

# my_dict = {
# 'Anita': [
# {'Biology': 'A', 'Chemistry': 'A*', 'Physics': 'B'},
# {'English': 'B', 'Literature': 'B', 'French': 'C'},
# {'PE': 'A', 'Music': 'A', 'Food Tech': 'B'}
# ]
# }
#
# for i in my_dict.keys():
#     result = type(my_dict[i])
#
# print(result)
#
# my_dict = {
# 'Anita': [
# {'Biology': 'A', 'Chemistry': 'A*', 'Physics': 'B'},
# {'English': 'B', 'Literature': 'B', 'French': 'C'},
# {'PE': 'A', 'Music': 'A', 'Food Tech': 'A'}
# ]
# }
#
# for i in my_dict.keys():
#     result = set(my_dict[i][2].values())
#
# print(result)