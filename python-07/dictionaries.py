# Dictionary

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items from keys
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys()) # output a list

# list all values
print(band.values()) # output a list

# list a key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# change value
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# remove items
print(band.pop("bass"))

print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictionaries

# band2 = band # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals",
}
member2 = {
    "name": "Page",
    "instrument": "guitar",
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets

nums = { 1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No duplicate allowed
nums = { 1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
# you can use update with lists, tuples, and dictionaries, too in a set
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)


# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7,}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# kepp everything except the duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)