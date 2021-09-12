# %%
string1 = "he's "
string2 = "probably "
string3 = "pinning "
string4 = "for the job"

print(string3 + string1)
print(string3,string1)


# %%
print('----------------FORMAT STRING SAMPLE--------------------------')
age = 24
days = 31
months =["jan", "mar", "may", "jul", "aug", "oct", "dec"]

#print( "I am still young at the age of" + age) #fail
print( "I am still young at the age of " + str(age))
print( "I am still young at the age of",age)
print( "I am still young at the age of {0}".format(age)) 

print( "there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(days, "jan", "mar", "may", "jul", "aug", "oct", "dec"))

#print("jan: {2}, feb: {0}, mar: {2}, apr: {1}, may: {2}, jun: {1}, jul: {2}, aug: {2}, sep: {1}, oct {2}, nov: {1}, dec: {2}"
#      .format(28,30,31))

print( "there are {} days in {}, {}, {}, {}, {}, {}, {}"
      .format(days, "jan", "mar", "may", "jul", "aug", "oct", "dec"))

print()
print(f"here is floating number {22 / 7: 12.50f}")


# %%
meal1 ="spam" + "eggs" + "beans"
print(meal1)

meal2 = "spam\neggs\nbeans"
print(meal2)

meal3 = "spam, eggs, beans"
print(meal3)

meal4 = """spam
eggs
beans """
print(meal4)



# %%
print('----------------SINGLE QUOTE SAMPLE--------------------------')
#Single quotes for anything that behaves like an Identifier.
#Single quotes are used for regular expressions, dict keys or SQL.
word = 'Ask?'
print(word)
print(word.isidentifier())
sentence = 'Python Programming'
print(sentence)
name = '"Hi" ABC'
print(name)

# %%
print('----------------DOUBLE QUOTE SAMPLE--------------------------')
#Double quotes generally we used for text.
#Double quotes are used for string representation.
wish = "Hello World!"
print(wish)
hey = "AskPython says 'Hi'"
print(hey)
famous ="'Taj Mahal' is in Agra."
print(famous)




# %%
print('----------------FORMAT--------------------------')
print ("This site is {0:f}% securely {1}!!".format(100, "encrypted"))
print()
# To limit the precision
print ("My average of this {0} was {1:.2f}%"
            .format("semester", 78.234876))



# %%
print('----------------SLICING SAMPLE--------------------------')
name = 'Mai Duy Khang'
print('The lenght of the string =',len(name))
print("Character at 12nd index =",name[12])
print("The last character of the third word =",name[len(name)-1])
print('-----------------Negative Index------------------------')
print("Nagative index to return last character =",name[-1:])
print("The first character of the first word =",name[-13])
print('Fullname =', name[:])
print('-------------------------------------------------------')
print("Slicing full str with negative =", name[-13:])
print("Slicing str with negative =", name[-13:-1])
print("Slicing str with negative =", name[-13:-8])
print("Slicing str with negative 0:-1 =", name[0:-1])
print("Slicing str with negative -9:-6 =", name[-9:-6])
print('-------------------------------------------------------')
print("Slicing str with negative -9:3 (NO RETURN) =", name[-9:3])
print('-------------------------------------------------------')
print("Using step in slice with 2 step =", name[::2])
print("Using step in slice with 3 step =", name[0::3])
print('-------------------------------------------------------')
print('Reverse full string =', name[13::-1])
print("Another way to reversed full string by starting negative index =",name[-1::-1])
print('Reverse string missing the last char =', name[13:0:-1])
print('Reverse string                       =', name[13::-1])
print("Reverse Slicing str with negative =", name[-7:-14:-1])
print("Another way to reversed string by starting negative index =",name[-1::-1])
print('Idiom Reverse string =', name[::-1])

#NOTE: For backward the starter value must be greater than stop value

# %%
print('----------------LETTER SAMPLE--------------------------')
letters = 'abcdefghijklmnopqrstuvwxyz'
print('Produce zy =',letters[:-3:-1])
print('Last 8 chars in reverse order =',letters[-1:-9:-1])
print('Last 8 chars in reverse order - alternative way =',letters[:-9:-1])
print(letters[4:0:-1])


print('----------------LETTER SAMPLE 2--------------------------')
letters = "abcdefghijklmnopqrstuvwxyz"
print('reverse words by starting negative index and  back slicing',letters[-1::-1])
print('reverse words by back slicing',letters[25:0:-1])
print(letters[25::-1])
print()
print('''With the negative step, the start value will default to the end of the string.
And the stop value defaults to the start of the string
==> we can omit the start and stop. Below is the sample''')
print()
print('Idiom Reverse string =d',letters[::-1])
print(':1:-1 =', letters[:1:-1])
print('-1:1:-1 =', letters[-1:1:-1])
print(letters[-2:-5],'NO DISPLAY')
print('Extracting "vwx" =',letters[-5:-2])
print()
#practice
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print()
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])



# %%
print('----------------SLICING STR SEQUENCE SAMPLE 3--------------------------')
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

# %%
print('----------------SLICING STR SEQUENCE SAMPLE 4--------------------------')
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[0:-1:5])

# %%
print('----------------SLICING STR SEQUENCE SAMPLE 5--------------------------')
word = "we win"
print(word[-1], word[-2])
# %%
b = "Norweginan Blue"
print(b[:6])
print(b[6:])


# %%
print('----------------IN OPERATOR--------------------------')
#in operator : The ‘in’ operator is used to check if a value 
# exists in a sequence or not. Evaluates to true if it finds
#  a variable in the specified sequence and false otherwise.
date = 'mon'
days = ['mon','tus', 'wed', 'thurs', 'fri']
if date in days:
    print(date)
print()
print()
today = 'friday'
print("day" in today)
print("fri" in today)
print("thurs" in today)
# %%


print('----------------BOOLEAN-TRUTH VALUE--------------------------')
"""
Any object can be tested for truth value, for use in an if or while condition 
or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method
that returns False or a __len__() method that returns zero, when called with the object. 
Here are most of the built-in objects considered false:

    constants defined to be false: None and False.

    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

    empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result always return 0 
or False for false and 1 or True for true, unless otherwise stated. 
(Important exception: the Boolean operations or and and always return one of their operands.)
"""
#Truth of table
"""a b (a or b)
T T T 
T F T
F T T
F F F

a b NOT (a or b)
T T F
T F F
F T F
F F T 

a b (a and b)
T T T
T F F
F T F
F F F

a b Not (a and b)
T T F
T F T
F T T
F F T

a b (NOT a AND NOT b)
T T F
T F F
F T F
F F T

a b (NOT a OR NOT b)
T T F
T F T
F T T
F F T

NOT (Hôm nay là thứ 2 và Hôm nay trời mưa)

Hôm nay KHÔNG là thứ 2 hoặc Hôm nay KHÔNG trời mưa"""

is_raining = False
is_clear = not is_raining

# print('raining' if not not not is_raining else 'not raining')

if is_clear:
    print('go swimming')
else:
    print('stay home')   

# %%
print('---------------BOOLEAN SAMPLE 2-------------------')

is_raining = True

def what_to_do(is_raining):
    if is_raining:
        print('Stay home')
    else:
        print('Go swimming')    

what_to_do(not not True)

# %%
a = 0
print(a)
if a:
    print('true')
else:
    print('false')    

# %%
a = 1
print(a)
if a:
    print('true')
else:
    print('false')    
# %%
a = ''
print(a)
if a:
    print('true')
else:
    print('false')  
# %%
a = None
print(a)
if a:
    print('true')
else:
    print('false')  
# %%
print('false = false =',False == False)
print('Empty string = false =','' == False)
print('None = False =',None == False)
print('True = True =',True == True)



# %%
print('---------------SPLIT BY SLICING SAMPLE 2-------------------')
num = "408-434;266,111:999"
seperator = num[3::4]
print(seperator)
values = "".join(char if char not in seperator else " " for char in num).split()
print(values)
print([int(val) for val in values])

# %%
print('---------------SPLIT BY FOR LOOP SAMPLE 2-------------------')
numbers = "408-434;266,111:999"
separator = ""
for char in numbers:
    if not char.isnumeric():
        separator = separator + char
print('separator after for loop =', separator)
values = "".join(char if char not in separator else " " for char in numbers).split()
print('Return list type of string values =',values)
print()
print("Convert list to int")
print("Using list comprehension to convert")
print([int(each_number)for each_number in values])
print()


# %%
print('---------------RANGE FUNCTION-------------------')
print('''1) The range() function returns a sequence of numbers, starting from 0 by default,
   and increments by 1 (by default), and stops before a specified number. (extend but not include) ''')
print('''2) range(start, stop, step)''')
print()
for i in range(5):
    print('No.', i)
print()
print("Range function with start, stop, step")
for i in range(0,11,2):
    print('EVEN No.', i)
#%%
print("Range function with negative step to backward -1")
for i in range(10,-1,-1):
    print('No. =', i)    

print("Range function with negative step to backward -2")
for i in range(10,0,-2):
    print('EVEN No.', i)        
#%%
for i in range(0,15):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
    
print()
    
for i in range(1,15):
    print("No. {0:3} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
 
print()
    
for i in range(1,15):
    print("No. {0:3} squared is {1:<3} and cubed is {2:4}".format(i, i**2, i**3))    




# %%
print('---------------FOR LOOP WITH STRING-------------------')
word = "we win"
print(word)

for x in word:
    if x == " ":
        print(x)
    else:
        print(x, "\n")    


#%%
print('--------------SEQUENCE TYPES-------------------')
print('STRING, LIST, TURPLE, RANGE')
print('A SEQUENCE IS AN ORDERED COLLECTION OF ITEM  AND CAN ACCESS BY INDEX')
print('ALL SEQUENCE TYPES ARE ITERABLE OBJECT AND CAN USE FOR LOOP')
print('NOT ALL ITERABLE OBJECTS ARE SEQUENCE SUCH AS DICT ==> WE CAN USE FOR LOOP FOR DICT')

# %%
print('--------------LIST-------------------')
print("DEFINE A LIST")
print()
list_num = [1,2,3]
print("Using square brackets, separating items with commas: list_num = [1,2,3] =",list_num)
print()
list_num2 = list((1,2,3))
print("Using the type constructor: list((1,2,3)) =",list_num2)
print()
#Define list object
list_num3 = [1,2,3]
print("list_num3 = [1,2,3] =", list_num3)
print("Using the type constructor: list(list_num3) =",list(list_num3))

#%%
print('--------------LIST-------------------')

print('--------------LIST IS MUTABLE SEQUENCE-------------------')

computer_list =['monitor','mouse','keyborad','CPU']

print('ACCESS COMPUTER LIST BY INDEX TO GET THE FIRST ITEM IN THE LIST: ',computer_list[0])

print('ACCESS COMPUTER LIST BY SLICING TO GET THE FIRST 2 ITEMS IN THE LIST: ',computer_list[0:2])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE WHOLE LIST: ',computer_list[-1::-1])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE WHOLE LIST (ALTERNATIVE): ',computer_list[3::-1])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE LIST: ',computer_list[-2:-4:-1])




# %%
print('--------------COUNT ITEMS IN THE LIST-------------------')
shopping_list = ["eggs", "spam","cookies", "pasta"]
count=0
for each_item in shopping_list:
    count += 1
print()    
print('TOTAL ITEMS IN THE LIST =',count)


# %%
print('--------------MEMBER OPERATOR \'IN\' USING FOR LIST-------------------')

computer_list =['monitor','mouse','keyborad','CPU']
item ='monitor'

if item in computer_list:
    print('The item is available')
else:
    print('NO ITEM IN THE LIST')    



# %%
print('--------------MEMBER OPERATOR \'NOT IN\' USING FOR LIST-------------------')

computer_list =['monitor','mouse','keyborad','CPU']
item ='webcam'

if item not in computer_list:
    print('The item IS NOT available')
else:
    print('The item is in the list')   
# %%
print('--------------MEMBER OPERATOR \'LEN()\' USING FOR LIST-------------------')

computer_list =['monitor','mouse','keyborad','CPU']

print('Length of the computer list =', len(computer_list))


# %%
print('--------------MEMBER OPERATOR \'CONCATENATION\' USING FOR LIST-------------------')

computer_list =['monitor','mouse','keyborad','CPU']
extra_item = ['webcam']

new_computer_list = computer_list + extra_item

print(new_computer_list)

 # %%

print('--------------MEMBER OPERATOR \'INDEX()\' USING FOR LIST-------------------')

computer_list =['monitor','mouse','keyborad','CPU']
extra_item = ['webcam']

new_computer_list = computer_list + extra_item

print('AFTER CONCATENATION =',new_computer_list) 

print('Find the index of the item in sequence type by using index() = ', new_computer_list.index('monitor'))



 # %%

print('--------------MEMBER OPERATOR \'s * n or n * s\' USING FOR LIST-------------------')
print()
print('''Note that items in the sequence s are not copied; they are referenced multiple times.''')
empty_list = [[]] * 3
print('''empty_list = [[]] * 3''')
print('Result of empty_list = ',empty_list)

empty_list[0].append(3)
print('EMPTY_LIST with append = ',empty_list)

# %%
print('--------------MEMBER OPERATOR \'append(x)\' USING FOR LIST-------------------')
item_list = [1,2,3,4]

item_list[len(item_list):len(item_list)] = [5,6,7]

print('Append item using len() = ', item_list)

item_list_2 = [1,2,3,4,5]
item_list_2.append(7)
print('Append item using append() in the print() and return NONE = ',item_list_2.append(7) )
print('Append item using append() = ',item_list_2 )


# %%
print('--------------MEMBER OPERATOR \'s[i:j] = t\' USING FOR LIST-------------------')

number_list =[1,2,3,5,7,12,4]
print('Define number_list BEFORE replacing using index/slicing =', number_list)
number_list[0] = 10
print('number_list AFTER using index to replace item ==> number_list[0] =10 =', number_list)
print('Slicing number_list[0:4] =', number_list[0:4])
number_list[0:4] = [18]
print('number_list AFTER using slicing to replace iterable object ==> number_list[0:4] = 18 is', a)


# %%
print('--------------MEMBER OPERATOR \' del s[i:j] \' USING FOR LIST-------------------')

number_list =[1,2,3,5,7,12,4]
print('number_list BEFORE deleting using slicing =', number_list)
print('The lenght or size of number_list BEFORE deleting using slicing =', len(number_list))
print('Slicing number_list[0:4] =', number_list[0:4])
del number_list[0:4]
print('del number_list[0:4] =', number_list[0:4])
print('The lenght or size of number_list AFTER deleting using slicing =', len(number_list))
print()
print("NOTE: CHANGING THE SIZE OF THE OBJECT THAT YOU'RE ITERATING OVER.")
print("IF YOU WANT TO REPLACE ITEMS WITH DIFFERENT ONES ==> IT IS NORMALLY OK")
print("HOWEVER, DELETING ITEMS FROM A LIST, OR ANY MUTABLE SEQUENCE TYPES, WHILE ITERATING FORWARS OVER IT WILL CAUSE PROBLEMS")

# %%
print('--------------MEMBER OPERATOR \' extend(t) \' USING FOR LIST-------------------')


computer_list =['monitor','mouse','keyborad','CPU']
extra_item = ['webcam']

computer_list_2 =['monitor','mouse','keyborad','CPU']
extra_item_2 = ['webcam']

computer_list_3 =['monitor','mouse','keyborad','CPU']
extra_item_3 = ['webcam']

computer_list = computer_list + extra_item
computer_list_2[len(computer_list_2):len(computer_list_2)] = extra_item_2
computer_list_3.extend(extra_item_3)
print('Using concatination: computer_list = computer_list + extra_item =',computer_list)
print('Using computer_list_2[len(computer_list_2):len(computer_list_2)] = extra_item_2 =',computer_list_2)
print('Using EXTEND(): computer_list_3.extend(extra_item_3) =', computer_list_3)


# %%
print('--------------MEMBER OPERATOR \' s.insert(i, x) \' USING FOR LIST-------------------')
computer_list =['monitor','mouse','keyborad','CPU']
print('Slicing computer[1:1] =',computer_list[1:1])
computer_list.insert(1,'Lamp')
print('Insert new item to the list based on index',computer_list)


# %%
print('--------------MEMBER OPERATOR \'s.remove(x)\' USING FOR LIST-------------------')
computer_list =['monitor','mouse','keyborad','CPU']
computer_list.remove('keyborad')
print("computer_list.remove('keyborad') is", computer_list)


# %%
print('--------------\'ENUMERATE FUNCTION)\'-------------------')
computer_list =['monitor','mouse','keyborad','CPU']

print(computer_list)

for part in computer_list:
    print('Item No. =', (computer_list.index(part)) +1 , ' is ', part)

# %%
computer_list =['monitor','mouse','keyborad','CPU']
print('This FOR LOOP from previous sample is not effieciency for counting of iterations')
print('==> Using enumerate()')
print('CREATE ENUMERATE OBJECT')
enum_computer_list_obj = enumerate(computer_list)
print("enum_computer_list_obj = enumerate(computer_list)")
print('Enum obj =', list(enum_computer_list_obj))
print('Using for loop to access enum object')
for element in enumerate(computer_list):
    print(element)

for count, element in enumerate(computer_list):
    print('count =', count , ' item is: ',element)

# %%
enum_from_list = enumerate(["a", "b", "c"])

for element in enum_from_list:
  print(element)

# %%
characters = ('a','b','c','d')
enum_chars = enumerate(characters)
print(enum_chars)
print(list(enum_chars))

for element in enum_chars:
   print(element)


# %%
print('--------------\'IMMUTABLE AND MUTABLE OBJECT\'-------------------')
print()
print('Immutable object is one whose value CANNOT be changed')
print('Immutable types are built into Python: INT, FLOAT, BOOL, STR, TURPLE, FROZENSET')
print('Example below:')

result = True
another_result = result
print('ID of result =',id(result))
print('ID of another_result =', id(another_result))

result = False
print('ID of FALSE result =',id(result))
print('ID of another_result =', id(another_result))

# %%
print('Mutable object is one whose value CAN be changed')
print('Mutable types are built into Python: LIST, DICT, SET, BYTEAARAY')
print('Example below:')

number_list = [1,2,3,4]
copy_number_list = number_list
print('ID of number_list =',id(number_list))
print('ID of copy_number_list =', id(copy_number_list))
print('NUMBER LIST =',number_list)
print('COPY NUMBER LIST =', copy_number_list)

number_list += [5,6,7]
print('ID of number_list after concatenation =',id(number_list))
print('ID of copy_number_list =', id(copy_number_list))
print('NUMBER LIST =',number_list)
print('COPY NUMBER LIST =', copy_number_list)


number_list.extend( [8,9,10])
print('EXTEND FUNCTION NUMBER LIST =',number_list)

# %%
print()
print("WE CAN CHANGE THE LIST VALUE BY ASSIGN NEW VALUE USING INDEX")
numbers = [1,2,3]
print('Define numbers =', numbers)
numbers[0]= 1000
print("NUMBER AFTER USING ASSIGN VALUE BY INDEX =",numbers)




# %%
print('--------------\'.SORT() METHOD\'-------------------')

print('SORT() method')
print('SORT() method is belong to LIST CLASS only and it mutates the object without creating a copy of the list')
print('==> SORTING WITHOUT CREATING NEW LIST OBJECT')
print()
number_list = [2,12,33,14,5,6]
another_number_list = number_list

print('Define number_list =',number_list)
print('ID of number_list =',id(number_list))

print('Define another_number_list =',another_number_list)
print('ID of another_number_list =',id(another_number_list))

print()

number_list.sort()
print('number_list after SORTED METHOD =',number_list)
print('ID of number_list after SORTED METHOD =',id(number_list))
print('another_number_list after SORTED METHOD =',another_number_list)
print('ID of another_number_list after SORTED METHOD =',id(another_number_list))

print()
print('SORT() method returns NONE if the list is assigned to variable')
number_list_2 = [2,12,33,14,5,6]

a = number_list_2.sort()

print('a =',a)

# %%
print('--------------\'SORTED() FUNCTION\'-------------------')
print('SORTED() function')
print('SORTED() function will take any iterable object')
print('SORTED() function returns a NEW LIST OBJECT and does not changing the original one')
print()
number_list = [2,12,33,14,5,6]
another_number_list = number_list

print('Define number list is =             ' ,number_list)
print('ID of number_list =',id(number_list))

print('Define another_number_list is =' ,another_number_list)
print('ID of another_number_list =',id(another_number_list))

print()

print('Using SORTED FUNCTION sorted(number_list) =',sorted(number_list))
print('ID of number_list  after SORTED FUNCTION  =',id(sorted(number_list)))
print('==> NEW OBJECT LIST IS CREATED\n')

print('number_list after SORTED FUNCTION   ',number_list)
print('ID of number_list  after SORTED FUNCTION =',id(number_list))

print('another_number_list after number_list SORTED FUNCTION is = ' ,another_number_list)
print('ID of another_number_list  after SORTED FUNCTION =',id(another_number_list))

print()
number_list += [3,7,8,10]
print('Number list after CONCAT is =' ,number_list)
print('another_number_list after CONCAT is =' ,another_number_list)

print('SORTED FUNCTION after CONCAT',sorted(number_list))
print('another_number_list after CONCAT number_list SORTED FUNCTION is =' ,another_number_list)



# %%
print('--------------\'FUNCTION SIGNATURES\'-------------------')
print('--------------\'print() FUNCTION\'-------------------')
print('''print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)''')
print()
#Define variable to test print()
name = "KHANG"
age = 30

print("Sample of print() star (*) objects")
print(name, age, "is learning Python", 2021)

print()
print("Using 'sep' key argument")
print("It is not usually not to put space either side of the equal sign when passing a key argument")
print(name, age, "is learning Python", 2021, sep=", ")

print()
print("The 'end' key argument is useful in for loop")
#%%
name_list = ['Khang', 'Ha', 'Daniel', 'Kat']


print("Because we only pass one object (name) in the print()")
print("Remember that the separator's only used between the values print when we pass more than one value object to the print")
print("==> The statement 'print(name, sep=", ", end=" ")' in the for loop below will not show separator")
print()

for name in name_list:
    print(name, sep=", ", end=" ")

print()
print("Instead, we can do the separator in the 'end' key argument")
for name in name_list:
    print(name, end=", ")
#%%
names = " ,".join(name_list)
print(names)


# %%
print('--------------\'.join() METHOD\'-------------------')

print()
print('''The join() method is a string method 
and returns a string in which the elements of sequence have been joined by str separator.''')

print()
print('''SYNTAX:
    string_name.join(iterable) ''')

print()
print('''PARAMETERS: The join() method takes iterable – objects capable of returning its members one at a time. 
Some examples are List, Tuple, String, Dictionary and Set

RRETURN VALUE: The join() method returns a string concatenated with the elements of iterable.

TYPE ERROR: If the iterable contains any non-string values, it raises a TypeError exception.''')    



# %%
print()
print('--------------\'.join() METHOD\'-------------------')
print()
flowers = [
    'Rose',
    'Lily',
    'Tulip',
    'Orchid',
    'Poppy',
    'Sunflower'
]

separator = " | "
output = separator.join(flowers)
print(output)

# %%
print('--------------\'.split() METHOD\'-------------------')
print()
print('''split() method in Python split a string into a list of strings after breaking the given string by the specified separator.

SYNTAX : str.split(separator, maxsplit)

PARAMETERS : \n
    SEPARATOR : This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.

    MAXSPLIT : It is a number, which tells us to split the string into maximum of provided number of times.
If it is not provided then the default is -1 that means there is no limit.

RETURN : Returns a list of strings after breaking the given string by the specified separator.''')
# %%

words = "Hello the world \n from the \t other side word"

print(words.split())

number = '1,232,545,232,888,999'

print(number.split(","))


# %%

generate_list = [
    '9', ' ',
    '2', '4', '6', ' ',
    '8', '8', '8', ' ',
    '9', '9', '9', ' ',
]

value = "".join(generate_list)
print(value)
print("ID of value after join =", id(value))
print()

create_value_list = value.split()
print("create_value_list = value.split()",create_value_list)
print("ID of create_value_list after split() =", id(create_value_list))

print()
print([int(val) for val in create_value_list])

print()
print((int(val) for val in create_value_list))

convert = (int(val) for val in create_value_list)
print(list(convert))

# %%
print('-------------------------------------------')
print('--------------\'TURPLE\'-------------------')
print()

print("Define Turple")
print()
number_turple = 1,2,3,4
print("number_turple = 1,2,3,4 =",number_turple)
print()
number_turple2 =(1,2,3,4)
print("number_turple2 = (1,2,3,4) =",number_turple2)
print()
number_turple3 = 1,
print("Using a trailing comma for a singleton tuple")
print("number_turple3 = 1, =",number_turple3)
print()
print("Using the tuple() built-in: tuple() or tuple(iterable)")


# %%
print('--------------TURPLE-------------------')

print('--------------TURPLE IS IMMUTABLE SEQUENCE-------------------')

computer_list ='monitor','mouse','keyborad','CPU'

print('ACCESS COMPUTER LIST BY INDEX TO GET THE FIRST ITEM IN THE LIST: ',computer_list[0])

print('ACCESS COMPUTER LIST BY SLICING TO GET THE FIRST 2 ITEMS IN THE LIST: ',computer_list[0:2])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE WHOLE LIST: ',computer_list[-1::-1])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE WHOLE LIST (ALTERNATIVE): ',computer_list[3::-1])

print('ACCESS COMPUTER LIST BY SLICING BY NEGATIVE INDEX TO BACKWARD THE LIST: ',computer_list[-2:-4:-1])

# %%
print('-------------- MORE EXAMPLE TURPLE-------------------')
#Define album metallica
metallica = "Ride the lightning", "Metallica", 1986
print()
print(metallica)
print()
print("Using index to access element in turple")
print()
print("First item in metallica =", metallica[0])
print("Second item in metallica =", metallica[1])
print("Third item in metallica =", metallica[2])
print()
print("TURPLE CANNOT BE CHANGED IN THE ELEMENT AFTER CREATING IT")
#print("ERROR WILL DISPLAY BELOW")
#metallica[0] = "Hello world"

# %%
print()
print("Create new object list from turple by using list() built-in function")

metallica_list = list(metallica)
print("Result =", metallica_list)

# %%
print('-------------- UNPACKING A TURPLE-------------------')

x,y = 1,2
print(x)
print(y)

# %%
data = 1,2,3 #data represents a turple
z,y,z = data
print("z,y,z = data")
print("The x, y, z variables on the left hand side look like turple but they are not")
print("They're 3 separate variables, that each variable gets data value from the data turple")
print("YOU CAN'T HAVE A TURPLE ON THE LEFT OF AN ASSIGNMENT")
print()
print('x =',x)
print('y =',y)
print('z =',z)
print()
# %%
print("We can unpack any sequence types BUT ERROR WILL OCCUR IF IT IS A MUTABLE OBJECT")
print("Example: Unpacking a list")
data_list = [1,2,3,4]

print("If we change value of the list BEFORE unpacking ==> it is NOT OK ==> ERROR")
data_list.append(10)

x,y,z,w = data_list
print('x =', x)
print('y =', y)
print('z =', z)
print('w =', w)

print("If we change value of the list AFTER unpacking ==> it is fine")
data_list.append(5)
print(data_list)

#%%
metallica = "Ride the lightning", "Metallica", 1986

title, artist, year = metallica

print(title)
print(artist)
print(year)


#%%
print('--------------NESTED TURPLE AND LIST-------------------')

albums = [("Future Nostalgia", "Dua Lipa", 2020),
          ("American Idiot", "Green Day", 2004),
          ("21st Century Breakdown", "Green Day", 2009),
          ("Ride the lightning", "Metallica", 1986),
          ("Origins","Imagine Dragons", 2018)
         ]

print()
print("Size of the albums list =", len(albums))

# for album in enumerate(albums):
#     print(album)

print()

for index, album in enumerate(albums):
    print("No.{0}: Album information: {1}".format(index,album))
    title,singer,year = album
    print("Title: ", title)
    print("Singer: ", singer)
    print("Year: ", year)


print('--------------NESTED TURPLE AND LIST SAMPLE 2-------------------')
# %%
from nested_data import albums
print(len(albums))
print()
for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))
    print()

# %%
from nested_data import albums
album = albums[2]
print(album)
print()
songs = album[3]
print(songs)
print()
song = songs[1]
print(song)
print()
print('Song title: ',song[1])
print()
print()

print(albums[2])
print(albums[2][3])
print(albums[2][3][1])
print(albums[2][3][1][1])

# %%
from nested_data import albums
album1 = albums[2][3][1][1]
print('Alternative way to get data in nested list turple: ', album1)


# %%
from nested_data import albums
for album in albums:
    print(album)

# %%
from nested_data import albums
for title, artist, year in albums:
    print(title)
    print(artist)
    print(year)
    print()

# %%
print('--------------FUNCTION-------------------')
print('''Python arguments are passed by assignment.
The behaviour is similar to pass by reference, 
when passing a mutable objects.
For immutable objects, the behaviour is closer to pass by value.''')
print()
print('''If we don't explicitly return a value,
Python will automatically return NONE''')
def print_result():
    numbers = [1,2,3,4]
    for number in numbers:
        print(number)
    return

print_result()


# %%
print('--------------FUNCTION SAMPLE 2 PALINDROME-------------------')
#This funtion returns true or false

def is_palindrome(word):

    backward = word[::-1]

    return backward == word


def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)            

def input_promt():

    return input("Please enter your string")    


text = input_promt()

print("The result to check palindrome is: ", is_palindrome(text.casefold()))
print()
print("The result to check sentence palindrome is: ", is_palindrome_sentence(text.casefold()))

print()
print()
a ="Mr. Owl ate my metal worm"
print(a[::-1]) 

string1 ="" 

for char in a:
    if char.isalnum():
        string1 += char

print(string1)       


# %%
print('--------------FUNCTION SAMPLE 3-------------------')

CHAR_E = 'e'
CHAR_O = 'o'

def sum_eo(number, string):

    list_number = []
    sum_number = 0

    if number < 0:
        return("Number must be greater than 0")

    if CHAR_E in string:
        for i in range(2,number,2):
            list_number.append(i)
        for number in list_number:
            sum_number += number
        return  sum_number
    elif CHAR_O in string:
        for i in range(1,number,2):
            list_number.append(i)
        for number in list_number:
            sum_number += number
        return  sum_number
    else:
        return -1    

print(sum_eo(10,'e'))
print(sum_eo(7,'o'))
print(sum_eo(10,'n'))

# %%
print('--------------FUNCTION *args-------------------')
print("*args represents unpackage tuple, then args without * is a tuple")
numbers = 0,1,2,3,4,5
print(numbers)
print(*numbers)
print( 0,1,2,3,4,5)
print()

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star('apple','flag')
# %%
print('--------------FUNCTION TYPE-------------------')
print("posisiton or keyword argument Must come first in the parameter list")
print("If we have a var-positional parameter then it must come AFTER any positional or keyword arguments")
print("Any parameters defined AFTER a var-positional parameter MUST be KEYWORD-ONLY (including VAR-KEYWORD")
print("VAR-KEYWORD argument appears last")

def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:.....{}, {}".format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keyword:..................{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)

