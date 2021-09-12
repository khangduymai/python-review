

#%%
import copy

print('--------------DEEP COPY() SAMPLE1-------------------')
animals = {
    "lion" : ["scary", "big", "cat"],
    "elephant" : ["big", "grey", "wrinkled"],
    "teddy" : ["cuddly", "stuffed"]
}

print("ID of animals object:", id(animals))
print("Value of teddy key from animals object:",animals["teddy"])
print()

#Perform shallow copy
#things = animals.copy()

#Perform deep copy
things = copy.deepcopy(animals)


print("ID of things object:", id(things))
print("Value of teddy key from things object:",things["teddy"])
print()

#Checking the ID of each key value in dict
print("ID of animals value:", id(animals["teddy"]), animals["teddy"])
print("ID of things value:",id(things["teddy"]), things["teddy"])
print()

print("Changing by adding value to things object")
things["teddy"].append('sweet')
print("Value of teddy key from animals object:",animals["teddy"])
print("Value of teddy key from things object:",things["teddy"])
print()

print("ID of animals value:", id(animals["teddy"]), animals["teddy"])
print("ID of things value:",id(things["teddy"]), things["teddy"])
print()
# %%
