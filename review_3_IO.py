
# %%
print('----------------------FILE I/O READING A FILE--------------------------')
file_to_read = open("D:\python\Python_practice\documents\sample_IO.txt")
for line in file_to_read:
    print(line)
file_to_read.close()    


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
print('BEST PRACTICE IN PYTHON')

with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    for line in file_to_read:
        print(line, end='')


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    line = file_to_read.readline()
    if line:
        print("There is a line")
    else:
        print("No line")


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
# To read the whole file by reading line by line
with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    line = file_to_read.readline()
    while line:
        print(line, end='')
        line = file_to_read.readline()


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
# To read the whole file by reading multi line at once
# NOT GOOD TO DEAL WITH LARGE FILE DUE TO MEMORY
with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    lines = file_to_read.readlines()

print(lines)

for line in lines:
    print(line, end='')


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
# To read the line backward
with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    lines = file_to_read.readlines()

print(lines)

for line in lines[::-1]:
    print(line, end='')


# %%
print('----------------------FILE I/O READING A FILE--------------------------')
with open("D:\python\Python_practice\documents\sample_IO.txt", 'r') as file_to_read:
    lines = file_to_read.read()

for line in lines[::-1]:
    print(line, end='')


# %%
print("READ() is better to deal with binary file")
print("READLINES() reads the entire files, but returning list of strings rather than a single string")
print("READLINE() reads a single line from a file and returns a string")
print()

# %%
print('----------------------FILE I/O WRITING A FILE--------------------------')

cities = ['Sai Gon', 'Nha Trang', 'Ha Long', 'Can Tho', 'Ca Mau']

with open("D:\python\Python_practice\documents\cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

print("Completed writing cites.txt") 

# %%
print('----------------------FILE I/O READING A FILE--------------------------')
cities = []

with open("D:\python\Python_practice\documents\cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city)

print('List of cities from city_file:',cities)  
print()
for city in cities:
    print(city, end='')      

# %%
print('----------------------FILE I/O READING A FILE USING STRIP()--------------------------')
cities = []

with open("D:\python\Python_practice\documents\cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print('List of cities from city_file:',cities)  
print()
for city in cities:
    print(city)     

print()
print("THE STRIP() IS A STRING METHOD AND IT ONLY REMOVE THE BEGINNING OR THE END OF THE STRING")


# %%
alice ="Welcome to my Nightmare", "Alice Cooper", 1975, (
    (1, "Welcome to my Nightmare"), (2, "Devil's Food"),(3, "The Black Widow"))

#print(alice)    

with open("D:\python\Python_practice\documents\Alice_sample.txt", 'w') as alice_file:
    print(alice, file=alice_file)

print("Writing process completed")    


# %%
print('----------------------FILE I/O READING A FILE AND USING EVAL()--------------------------')
with open("D:\python\Python_practice\documents\Alice_sample.txt", 'r') as alice_file:
    contents = alice_file.readline()
print(contents)

alice_eval = eval(contents)

album, artist, year, tracks = alice_eval
print(album)
print(artist)
print(year)
print()

print(alice_eval, type(alice_eval))
print()

for each_elem in alice_eval:
    print(each_elem)
print()

    


# %%
print('----------------------FILE I/O APPENDING TO CURRENT FILE--------------------------')

def two_times(num: int, file_name) -> None:
    """return the result of 2 times table

    Parameters
    ----------
    num : int
    file_name
        
    """
    i = 1
    while i <= num:
        print(f"{i} times 2 is {i*2}", file=file_name)
        i +=1
    print('-'*30, file=file_name)


print('----------------------FILE I/O READING A FILE AND USING EVAL()--------------------------')
with open("D:\python\Python_practice\documents\sample_IO.txt", 'a') as table:
    two_times(20, table)
   

print("Completed")    



# %%
print('----------------------FILE I/O BINARY FILE--------------------------')
with open("D:\python\Python_practice\documents\Binary_sample", "bw") as bin_file:
    for i in range(20):
        bin_file.write(bytes([i]))
print("completed")
print()


with open("D:\python\Python_practice\documents\Binary_sample", "br") as binFile:
    for b in binFile:
        print(b)


# %%
# print('----------------------FILE I/O PICKLE MODULE--------------------------')
# import pickle

# imelda = ('More Mayhem',
#           'IMelda May',
#           '2011',
#           ((1, 'Pulling the Rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))

# with open("D:\python\Python_practice\documents\Binary_sample_2", "bw")  as pickle_file:
#     pickle.dump(imelda,pickle_file)          

# with open("D:\python\Python_practice\documents\Binary_sample_2", "br")  as pickle_file:
#     imelda2 = pickle.load(pickle_file)

# print(imelda2)


# %%
print('----------------------FILE I/O PICKLE MODULE--------------------------')
import pickle
imelda = ('More Mayhem',
          'IMelda May',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# Store data (serialize)
with open("D:\python\Python_practice\documents\Binary_sample_2", "bw")  as pickle_file:
    pickle.dump(imelda,pickle_file,protocol=0) #human-readable binary file
    pickle.dump(even,pickle_file,protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(odd,pickle_file,protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(2998302, pickle_file,protocol=pickle.DEFAULT_PROTOCOL)    

# Load data (deserialize)
with open("D:\python\Python_practice\documents\Binary_sample_2", "br")  as pickle_file:
    unserialized_imelda = pickle.load(pickle_file)
    unserialized_even_list = pickle.load(pickle_file)
    unserialized_odd_list = pickle.load(pickle_file)
    unserialized_x = pickle.load(pickle_file)

print(unserialized_imelda)

# album, artist, year, track_list = unserialized_imelda

# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

print('=' * 40)

for i in unserialized_even_list:
    print(i)

print('=' * 40)

for i in unserialized_odd_list:
    print(i)

print('=' * 40)

print(unserialized_x)

print('=' * 40)    

# %%
import shelve

print('----------------------FILE I/O SHELVE MODULE--------------------------')

# Shelve keys must be string unlike dict where keys can be immutable objects
# Any operators/methods from dict can be applied on shelve object

with shelve.open('D:\python\Python_practice\documents\ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit" 

    # Begin to print item in shelve object
    print('Lemon is: ',fruit['lemon'])   
    print('Lime is: ', fruit['lime'])
    print('Printing shelve object inside shelve block code: ', fruit)


# THIS WILL CAUSE ERROR IF RUNNING THE BELOW CODE
# print('Lemon is: ',fruit['lemon'])   
# print('Lime is: ', fruit['lime'])

print()
print('Shelve object outside of shelve block code: ', fruit)

# %%
import shelve

print('----------------------FILE I/O SHELVE MODULE NOTE--------------------------')
print()
print('''There is no shelve literal, check the example below:''')
print()

with shelve.open('D:\python\Python_practice\documents\ShelfTest') as fruit:
    fruit = {'orange':"a sweet, orange, citrus fruit",
             'apple' : "good for making cider",
             'lemon' : "a sour, yellow citrus fruit",
             'grape' : "a small, sweet fruit growing in bunches",
             'lime' : "a sour, green citrus fruit",
    }

    print('Lemon is: ',fruit['lemon'])   
    print('Lime is: ', fruit['lime'])
    print('Printing shelve object inside shelve block code: ', fruit)


# %%
import shelve

print('----------------------FILE I/O SHELVE MODULE 2--------------------------')

# Shelve keys must be string unlike dict where keys can be immutable objects
# Any methods from dict can be applied on shelve object

fruit = shelve.open(('D:\python\Python_practice\documents\ShelfTest'))

fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit" 


for each_item in fruit:
    print(each_item)

fruit.close()

print()
print('Printing shelve object inside shelve block code: ', fruit)


# %%
import shelve

print('----------------------FILE I/O SHELVE IS PERSISTENT FILE--------------------------')

# file_directory = "D:\python\Python_practice\documents\Bike"
# with shelve.open(file_directory) as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250

#     print('Bike model is: ', bike['model'])
#     print('Bike engine size is: ', bike['engine_size'])

# Create bike2 file shelve object

file_directory = "D:\python\Python_practice\documents\Bike2"
with shelve.open(file_directory) as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engi_size"] = 250 # typo engi_size ==> must be engine_size

    # print('Bike model is: ', bike['model'])
    # ==> CAUSING ERROR DUE TO BIKE2 FILE NOT CONTAINING ENGINE_SIZE
    # print('Bike engine size is: ', bike['engine_size']) 

    for each_data in bike:
        print(each_data)  

print()
print()
# # FIXING THIS BY MODIFYING ENGI_SIZE TO ENGINE_SIZE MANNUALLY

# file_directory = "D:\python\Python_practice\documents\Bike2"
# with shelve.open(file_directory) as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250 


#     for each_data in bike:
#         print(each_data)    


# print()
# print()


file_directory = "D:\python\Python_practice\documents\Bike2"
with shelve.open(file_directory) as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250 

    bike.pop('engi_size', "NO VALUE")

    for each_data in bike:
        print(each_data)



# %%
import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
pasta = ["pasta", "cheese"]
soup = ["tin of soup"]

file_directory = "D:\python\Python_practice\documents\Recipes"

# When we first run this, it will generate recipes shelve file and add the objects to the file
with shelve.open(file_directory, writeback=True) as recipes:

    # FIRST run to add objects to file

    # recipes['blt'] = blt
    # recipes['beans_on_toast'] = beans_on_toast
    # recipes['scrambled_eggs'] = scrambled_eggs
    # recipes['pasta'] = pasta

    # SECOND run this to add new receip
    # recipes['soup'] = soup

    # THIRD run, append new item in list object
    # ==> the new item is not appended to the list
    # recipes["blt"].append("butter")


    # THIS METHOD WORKING WITH OBJECT IN MEMORY 

    # tmp_list = recipes['blt']
    # tmp_list.append("butter")
    # recipes["blt"] = tmp_list

    # FOURTH, using writeback=True
    # recipes["soup"].append("croutons")


    # FIFTH, using sync()

    # recipes["soup"] = soup
    # soup.append("cream")
    # recipes.sync()

    # SIXTH, the sync() using wrong and it clear the cache
    recipes.sync()
    soup.append("onion")

    # Read the file from shelve
    for i in recipes:
        print(i, recipes[i])

# %%
import shelve

books_dict = {
    "receipes" : {
        "blt" :  ["bacon", "lettuce", "tomato", "bread"],
        "beans_on_toast"  : ["beans", "bread"],
        "scrambled_eggs" : ["eggs", "butter", "milk"],
        "pasta" : ["pasta", "cheese"],
        "soup" : ["tin of soup", "croutons", "cream"],
    },
    "maintaince" : {
        "stuck" : ["oil"],
        "loose" : ["gather tape"],
    }
}

file_directory = "D:\python\Python_practice\documents\Books"

with shelve.open(file_directory) as books:
    books["receipes"] = {
                            "blt": ["bacon", "lettuce", "tomato", "bread"],
                            "beans_on_toast": ["beans", "bread"],
                            "scrambled_eggs": ["eggs", "butter", "milk"],
                            "pasta": ["pasta", "cheese"],
                            "soup": ["tin of soup", "croutons", "cream"]
                        }
    
    books["maintaince"] = {
                            "stuck": ["oil"],
                            "loose": ["gather tape"]
                          }

    print(books["maintaince"]["stuck"])
# %%
