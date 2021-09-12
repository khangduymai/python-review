


print("""A SHALLOW COPY COPIES REFERENCE.
IT DOES NOT MAKE A COPY OF A THE THINGS THAT ARE BEING REFERRED TO.""")
print()
print(""" The copy() method will end up with a copy of the original dictionary,
containing the same keys and values.
That means the values will continue to refer to the same object in the copy""")
#%%
print('--------------SHALLOW COPY() SAMPLE1-------------------')
animals = {
    "lion" : ["scary", "big", "cat"],
    "elephant" : ["big", "grey", "wrinkled"],
    "teddy" : ["cuddly", "stuffed"]
}

print("ID of animals object:", id(animals))
print("Value of teddy key from animals object:",animals["teddy"])
print()
things = animals.copy()
print("ID of things object:", id(things))
print("Value of teddy key from things object:",things["teddy"])
print()
#changing by adding value to each object
animals["teddy"].append('sweet')
print("Value of teddy key from animals object:",animals["teddy"])
print("Value of teddy key from things object:",things["teddy"])



# %%
print('--------------SHALLOW COPY() SAMPLE2-------------------')
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion" : lion_list,
    "elephant" : elephant_list,
    "teddy" : teddy_list,
}

print("ID of animals object:", id(animals))
print("Value of teddy key from animals object:",animals["teddy"])
print()
things = animals.copy()
print("ID of things object:", id(things))
print("Value of teddy key from things object:",things["teddy"])
print()
#changing by adding value to each object
teddy_list.append('sweet')
print("ID of animals object:", id(animals))
print("Value of teddy key from animals object:",animals["teddy"])
print("ID of things object:", id(things))
print("Value of teddy key from things object:",things["teddy"])




# %%
print('--------------SHALLOW COPY() SAMPLE3-------------------')
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion" : lion_list,
    "elephant" : elephant_list,
    "teddy" : teddy_list,
}


print("ID of animals object:", id(animals))
print("Value of teddy key from animals object:",animals["teddy"])
print()

things = {
    "lion" : lion_list,
    "elephant" : elephant_list,
    "teddy" : teddy_list,
}

print("ID of things object:", id(things))
print("Value of teddy key from things object:",things["teddy"])
print()
#changing by adding value to each object
teddy_list.append('sweet')
animals["teddy"].append("adding value via `animals` object")
things["teddy"].append("adding value via `things` object")
print("Value of teddy key from animals object:",animals["teddy"])
print("Value of teddy key from things object:",things["teddy"])
print("teddy_list: ",teddy_list)

# %%
