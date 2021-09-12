#%%
"""
for i in range(1, 13):
    print("No. {0:4} squared is {1:4} and cubed is {2:4}"
          .format(i, i**2, i**3))
    if i == 9:
        print("this is the test with i = {0}".format(i))
        continue
print("OUT OF LOOP")   
"""
# %%
"""
name = input("what's your name?")
age = int(input("How old are you, {0}?".format(name)))

if age >= 18:
    print("you're old enough to vote")
else:
    print("please wait until you are 18")
    """
# %%
"""
correctAnswer = 5

print("please choose a number from 1 to 10:")
inputAnswer = int(input())
while inputAnswer != correctAnswer:
    if inputAnswer < correctAnswer:
        print("please guess higher")
        inputAnswer = int(input("Please input again"))
    else:
        print("Please guess lower")
        inputAnswer = int(input("Please input again"))
print(f"your correct answer is {inputAnswer}")

# %%
tree1 = "treeVerryTall"
tree2 = "treeShort"

if tree1 > tree2:
    print(tree1)
else:
    print(tree2)
"""
# %%
"""
day = 'Monday'
temp = 30
isRaining = True

x = not isRaining
print(x)

if day == 'Monday' and temp > 27 and not isRaining:
    print("LET'S GO SWIMMING")
else:
    print("Bad day")
"""

"""
constants defined to be false: None and False.

zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

empty sequences and collections: '', (), [], {}, set(), range(0)

Operations and built-in functions that have a Boolean result 
always return 0 or False for false
and 1 or True for true, unless otherwise stated. 
(Important exception: the Boolean operations or and and always return one of 
their operands.)
"""
# %%
num1 = 10
num2= 20

x = int(input())
if num1 <= x < num2:
    print("correct")
else:
    print("fail")
    
x = int(input())
if num1 <= x  and x < num2:
    print("correct")
else:
    print("fail")         

# %%
