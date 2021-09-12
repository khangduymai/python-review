# %%
print('----------------------MAPPING TYPE--------------------------')
print('--------------DICTIONARY DICTIONARY[key] and GET(key[, default])-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
    "ONIOn" : 1,
    "onion" : 100, # key is unique
}

print('''
carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
    "ONIOn" : 1,
    "onion" : 100, # key is unique
}
''')

# NOTE: KEYS IN DICTIONARY ARE UNIQUE
print()
# Access/retrive data from dictionary
print(f"The number of chicken to buy: {carts['chicken']}")

# Dict keys are case sensitive
print(f"The number of onion to buy: {carts['onion']}")
print(f"The number of `ONIOn` to buy: {carts['ONIOn']}")
print()

print(carts)
print()

# Using get(key) to retrieve data and handle error
#print(f"The number of onion to buy: {carts['onion3']}")
print(f"The number of egg to buy: {carts.get('egg')}")
print()
print(f"The number of ham to buy: {carts.get('ham', 'No ham in dictionary')}")

print()
print("""1) GET() method will return None if the key is not found.
2) KEY INDEX is faster if we know the key will be presented using square brackets [].
3) KEY INDEX crashes if the key is invalid (case sensitive) -> key error""")
print()
# %%
print('--------------ITTERATING OVER DICTIONARY (KEY-VALUE PAIR)-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
    "ONIOn" : 1,
}

# for loop in dict will only return keys
for each_item in carts:
    print(each_item)
print()

print("------------------------------------------------")
# enumerate() function returns a counter and the value from the iterable object such dict
# Unpacking enumerate object to get the values
for index, key in enumerate(carts):
    print(index, key, carts[key], sep=": ")
print()

print("------------------------------------------------")
#%%
#Return a turple in a list of turple 
carts_view = carts.items()

print('''NOTE: dict view cannot access using index''')
print(carts_view)
print()
# The for loop will return dict view turple (key, value) pair
for each_item in carts_view:
    print(each_item)
print()
# We can access the dict view in for loop using index to get either key or value
for each_item_1 in carts_view:
    print(each_item_1[0])
print()
# We can use unpacking turple to retrieve key pair in dict view
for key, value in carts_view:
    print(key, ": ", value)
print()

#%%
print('--------------DICTIONARY ADD ITEM -------------------')
carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

# To add a new item in dictionary
carts["duck"] = 3
print(carts)

# If the key is alreay in the dict, when we add that existing key to dict
# It will update the value of that key
# for example: chicken in the dict is 2 then we add chicken = 4
# It will replace the value 2 to 4

carts["chicken"] = 4 ## UPDATE value using exsisting KEY
print("Cart updated the number of chicken value:", carts)
print()


# %%
print('--------------DICTIONARY UPDATE([other])-------------------')
print('''Update the dictionary with the key/value pairs from other, overwriting existing keys. 
Return None.''')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

carts_2 = {
    "chicken" : 4,
    "salad" : 3,
    "beef" : 10,
    "onion" : 5,
}

# We have 2 seperated dictionary and we wanna combine to one based on first dict
carts.update(carts_2)
print("Update carts: ", carts)
print()


carts_3 = {
    "tuna" : 4,
    "egg" : 12,
    "sugar" : 10,
    "ice cream" : 5,
}


# We can update the current dict with more item from different dict
carts.update(carts_3)
print("Update dict with more items: ", carts)
print()

#%%
print('--------------DICTIONARY DEL[key] = value vs POP(key[, default])-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

# Using del[key] to remove item in dict
# Will get ERROR if the key is not exsisted in the dict

print("Original carts: ",carts)
print()

del carts["chicken"]
print("Using del d[key]:")
print("Result of deleted item 'chicken' from the dict: ", carts)
print()

# NOTE
# Causing KEY ERROR if key is not existed in dict
#del carts["egg"]


# Using POP to handle exception

#carts.pop("salad", "No key available")
result = carts.pop("salad", "No key `salad available")
print("Using  pop(key[, default]:")
print("Return the value of pop item: ", result)
print("Result of deleted item 'salad' from the dict: ", carts)
print()


result_handle_error = carts.pop("egg", "No key available")
print("Using  pop(key[, default] to handle key error:")
print("Return the value of pop item: ", result_handle_error)
print("Result of deleted non-exsisting item 'egg' from the dict: ", carts)
print()


# %%
print('--------------DICTIONARY POPITEM()-------------------')

#LIFO

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

num_items = len(carts)
i = 0
print('Number of items in dict: ',len(carts))
while i < num_items:
    print(carts.popitem())
    i += 1

# print()
# print(carts)

# popitem_result = carts.popitem()
# print(popitem_result)
# print(carts)
# print()
# print(carts.popitem())
# print(carts)

# Raise KEY ERROR if DICTIONARY is EMPTY
# carts_empty = dict()
# popitem_result1 = carts_empty.popitem()
# print(popitem_result1)


# %%
print('--------------DICTIONARY SETDEFAULT(key[, default]) METHOD-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

# Another way to retrieve value based on key
value_item = carts.setdefault("chicken", 0)
print("The value of `chicken` key is: ",value_item)
print(carts)
print()

# If key is in the dictionary, return its value. 
# If not, insert key with a value of default and return default. 
# default defaults to None.

value_item1 = carts.setdefault("egg", 0)
print("The value of `egg` key is: ",value_item1)
print("`Egg` key and value are added to `carts`: ",carts)
print()


# %%
print('--------------DICTIONARY FROMKEYS(iterable[, value]) CLASS METHOD-------------------')

d = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

new_d = dict.fromkeys(d)

print(new_d)

print()

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_pantry_dict = dict.fromkeys(pantry_items)
print("NEW dictionary object with NONE values: \n", new_pantry_dict)

print()
new_pantry_dict = dict.fromkeys(pantry_items, 0)
print("NEW dictionary object with default values: \n", new_pantry_dict)
print()

# %%
print('--------------DICTIONARY KEYS() METHOD-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

cart_keys_view = carts.keys()
print(cart_keys_view)
print()

# Below code return error
# TypeError: 'dict_keys' object is not subscriptable

# for each_key in carts_key_view:
#     if carts_key_view[each_key] == 'chicken':
#         carts[each_key] = 12
#         break
print(carts)

# %%
print('--------------DICTIONARY VALUES() METHOD-------------------')

carts = {
    "chicken" : 2,
    "salad" : 1,
    "beef" : 5,
    "onion" : 10,
}

cart_values_view = carts.values()
print(cart_values_view)
print()

#convert keys and values into 2 lists 
keys = list(carts.keys())
values = list(carts.values())
print("Keys of carts dict: ",keys)
print("Values of carts dict: ",values)

#%%
print('--------------SET INTRODUCTION-------------------')

# Define SET
print('''1) Set using curly braces same as dictionany THE ONLY DIFFERENCE is NO KEY in set.
2) SET is UNORDER COLLECTION and UNIQUE.
3) Sets use hashes to store the items, anythings putting into a set MUST be hashable''')

# Remember key in dictionary required hashable object (most hash object is IMMUTABLE )
# If we put a LIST in SET ==> ERROR (UNHASABLE TYPE)

farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse', 'cow'}

#print(farm_animals)
print()
print("Farm_animal:")
for animal in farm_animals:
    print(animal)


print()
print("Index a sequence type")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse', 'cow']
goat = animals_list[3]
print(goat)
print()

# print("Index of a SET is NOT POSSIBLE")
# farm_animals[3]
# print(farm_animals)

# Return ERRROR: 'set' object is not subscriptable 
# It means SET CANNOT USE INDEX

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

if more_animals == farm_animals:
    print('The set are equal')
else:
    print("The set are different")

print('''==> Return EQUAL because both set farm_animals and more_animals contain the same items.
    Ordering is UNIMPORTANT - It's the items contained in the set that count.
''')

#%%
# NOTE: Remember LIST and TURPLE will compare equal if they contain the same items, in the same order
list_a = ['a','b','c']
list_b = ['a','c','b']

if list_a == list_b:
    print('The lists are equal')
else:
    print("The lists are different")
# %%
print('''==> IF WE'RE WORKING WITH LARGE DATA, CHECKING FOR MEMBERSHIP WILL BE A LOT FASTER WITH A SET COMPARED TO A LIST''')
print('''==> Checking for membership of a list or a turple is quite slow because it need to use liner search which starting 
to look up the first element at the beginning of either the list or the turple then comparing it with the searched value''')
print('''==>  Sets use hashes to store the items. Therefor, checking membership is faster)''')


#%%
print('--------------CREATE EMPTY SET-------------------')

# Create empty DICT
number_dict = {}
print("Number is a dict", number_dict, type(number_dict))
print()
# Create empty SET
number_set_1 = {*""}
print("Number is a set", number_set_1, type(number_set_1))
print()
# Create empty SET
number_set_1 = {*""}
print("Number is a set", number_set_1, type(number_set_1))
print()
# Create empty SET
number_set_2 = {*{}}
print("Number is a set", number_set_2, type(number_set_2))
print()
# Create empty SET
number_set_3 = set()
print("Number is a set", number_set_3, type(number_set_3))
print()


# %%
print('--------------SET ADD(element) ITEMS-------------------')

numbers = set()

while len(numbers) < 4:
    next_value = int(input("Pleaese enter your next value: "))
    numbers.add(next_value)

print(numbers)    


# %%
print('--------------CREATE UNIQUE DATA BY SET-------------------')

data = ['blue', 'red', 'blue', 'green', 'red','blue','white']

# unique_data = set(data)
# print(unique_data) 

# Create a list of unique colors, keeping the order they appear
print("dict.fromkey() = ", dict.fromkeys(data))
unique_data = list(dict.fromkeys(data))
print(unique_data)


# %%
print('--------------SET OPERATOR REMOVE(element) and DISCARD(element) METHODS-------------------')

print('''CASE 1: we want to delete item in the set but we do not care if it was already there or not. We just wanna delete it ''')
print('''==> USING DISCARD() FOR CASE 1''')
print()
print('''CASE 2: we want to delete item exsiting in the set and we want some sort of notification if the item in the set does not exist ''')
print('''==> USING REMOVE() FOR CASE 2''')
print()

small_int = set(range(21))

print("Small_int before delete:", small_int)

small_int.discard(10)
print("Discard 10: ", small_int)
small_int.remove(11)
print("Remove 11: ", small_int)
print()

print("SAMPLE CASE 1")
small_int.discard(10)
print(small_int)
small_int.discard(99)
print(small_int)
print()

print("SAMPLE CASE 2")
print("Remove() will let us know, if we try to delete something that doesn't exist ==> CRASH ERROR")
print("Discard() WILL NOT TELL US like remove()")
small_int.remove(10)
print(small_int)
small_int.remove(99)
print(small_int)

# %%
print('--------------SET UPDATE(*others) and UNION(*others)-------------------')
print()
print('''Set update() perform a set union, but modifies the original set, rather than creating a new one ''')

snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
print()

# Union creates new set
animals_that_bite = snakes.union(spiders)

# Using Union symbol |
animals_that_bite_2 = snakes | spiders

# Set update() perform a set union, but modifies the original set
snakes.update(spiders)

print(animals_that_bite)
print(snakes)
print(animals_that_bite_2)




# %%
print('--------------SET INTERSECTION()-------------------')

set_a = {1,2,3,4,5,6,7,8}
set_b = {4,3,5,11,12,14,15}

intersection_a_b = set_a.intersection(set_b)
print(intersection_a_b)
print()
# Using intersection symbol &
intersection_a_b_2 = set_a & set_b
print(intersection_a_b_2)


# %%
# Finding out which prepositions have been used in the text
text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
set_chars = set(text.split())

preps_used = set_chars.intersection(prepositions)

print(preps_used)

set_chars.intersection_update(prepositions)
print(set_chars)

# %%
print('--------------SET DIFFERENCE()-------------------')
# just like set_a minus set_b
print('''If A and B are two sets. 
The set difference of A and B is a set of elements that exists only in set A but not in B)''')
print('''\nIf A = {1, 2, 3, 4}
B = {2, 3, 9}
Then,
A - B = {1, 4}
B - A = {9}''')
print()
print("Example:")
set_a = {1,2,3,4,5,6,7,8}
set_b = {3,4,5,11,12,14,15}

result_diff_a = set_a.difference(set_b)

print(result_diff_a)
print()

result_diff_b = set_b.difference(set_a)

print(result_diff_b)
print()

# Using 'a - b'
result_diff_c = set_a - set_b

print(result_diff_c)


# %%
print('--------------SET SYMMETRIC_DIFFERENCE()-------------------')
print()
print('''The symmetric difference of two sets A and B is the set of elements that are in either A or B,
but not in their intersection.''')
print()

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))
print()
print()

print('''Using operator ^''')
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)
# %%
print('--------------SET SUBSET() and SUPERSET()-------------------')

print('''
set a = {1,2,3}
set b = {1,2,3,4,5,6}
`a` is a part of `b`
`a` is different than `b` because there is at least one element in `b` is not belong to `a`
==> `a` is a subset of `b` OR Every element in `a` also presents in `b`
==> `a` is a subset of `a`
==> `a` is a proper subset of `b` because there is at least one element of `b` is not belong to `a`
==> `b` is a proper superset of `a` because there is at least one element of `b` is not belong to `a`
''')

# %%
print('--------------SET SUBSET() and SUPERSET() SAMPLE 1-------------------')

animals ={
    'Turtle',
    'Horse',
    'Robin',
    'Python',
    'Swallow',
    'Hedgehog',
    'Wren',
    'Aardvark',
    'Cat',
}

birds ={
    'Robin',
    'Swallow',
    'Wren',
}

print(f'Birds is a subset of animals: {birds.issubset(animals)}')
print(f'Animals is a superset of birds: {animals.issuperset(birds)}')

print()

print(f'Birds is a superset of animals: {birds.issuperset(animals)}')
print(f'Animals is a subset of birds: {animals.issubset(birds)}')

print()

print(f'Birds is a subset of animals: {birds <= animals}')
print(f'Birds is a proper subset of animals: {birds < animals}')

print()
print(f'Animals is a superset of birds: {animals >= birds}')
print(f'Animals is a proper superset of birds: {animals > birds}')

print('*' * 80)

garden_birds = {
    'Swallow',
    'Wren',
    'Robin',    
}


print(f'Comparing set bird to check if it is equal to garden birds: {garden_birds == birds}')
print(f'Garden_birds is a subset of birds: {garden_birds.issubset(birds)}')
print(f'Garden_birds is a proper subset of birds: {garden_birds < birds}')

print()
print('*' * 80)

more_birds = {
    'Wren',
    'Budgie',
    'Swallow'
}

print(f'Comparing set more_birds to check if it is equal to garden birds: {garden_birds == more_birds}')
print(f'More_birds is a subset of garden_birds: {more_birds <= garden_birds}')
print(f'More_birds is a subset of garden_birds: {more_birds >= garden_birds}')



# %%
print('--------------SET SUBSET() and SUPERSET() SAMPLE 2-------------------')

required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()

for candidate, skills in candidates.items():
    if candidates[candidate].issuperset(required_skills):
        interviewees.add(candidate)

print(interviewees)

# %%

