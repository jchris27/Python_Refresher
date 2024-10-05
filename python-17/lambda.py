squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(10))

sum_total = lambda a, b: a + b

print(sum_total(10, 8))

#################################

def func_builder(x):
    return lambda num: num + x

add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(7))
print(add_twenty(7))

#################################

numbers = [2,4,6,19,21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#################################

from functools import reduce

numbers_list = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers_list, 10)

print(total)

print(sum(numbers_list, 10))

names = ["Jin", "Sayo", "Yui", "John Jacob Jingleheimerschmidt"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)