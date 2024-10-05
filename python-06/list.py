users = ['Jino', 'Sayo', 'Yui']

data = ['Jino', 42, True]

emptyList = []

# check an item in a list
print("Jino" in users)

# get specific item in a list
print(users[2])

# get the last value in a list
print(users[-1])

# get the position of a specific value
print(users.index('Sayo'))

# range of values
print(users[0:2]) # not including the last value
print(users[1:])
print(users[-3:-1])

# checks the length of a list
print(len(data))

# insert data in a list
users.append('Elsa')

users += ['Jason']

users.extend(['Robert', 'Jimmy'])

# users.extend(data)


# add list in the very first position
users.insert(0, 'Bob')

# start and ends in the same postiion without replacing any value
users[2:2] = ['Eddie', 'Alex']

# replace values in the position
users[1:3] = ['Robert', 'JPJ']

# removing data in a list
users.remove('Bob')

users.pop() # removes the last value

# delete a specific item in a list
del users[0]

# delete the whole list
# del data

data.clear() # clears the list but retains the variable
print(data)

users[1:2] = ['jino']

# sorting
users.sort()

# sort with lowercase
users.sort(key=str.lower)
print(users)

# flip the order in a list
nums =  [4, 42, 78,1, 5]

nums.reverse()

# reverse in a descending order
# nums.sort(reverse=True)
print(nums)

# sort the list without modifying the original data
print(sorted(nums, reverse=True))
print(nums)

# make a copy of a list
nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(nums)
print(nums_copy)
print(my_nums)
my_copy.sort()
print(my_copy)

print(type(nums))
my_list = list([1, 'Neil', True])
print(my_list)

# Tuples

# immutable list
my_tuple = tuple(('Dave', 42, True))
another_tuple = (1,4,2,6, 2,2)
print(my_tuple)
print(type(my_tuple))

# assign a value to a tuple
newlist = list(my_tuple)
newlist.append('Neil')
new_tuple = tuple(newlist)
print(new_tuple)
print(my_tuple)

# unpack a tuple
(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)

# count how many occurences in a tuple
print(another_tuple.count(2))