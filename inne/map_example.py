numbers = [2, 4, 6, 8, 10]


def square(number):
    return number * number


squared_numbers_iterator = map(square, numbers)

squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

l = ['qwerty', 'asdfg', 'zxcvb', 'qazwsx']

test = list(map(list, l))
print(test)