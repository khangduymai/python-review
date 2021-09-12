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
print('--------------FUNCTION-------------------')

print('''Parameters are the definition it's the variables defined in the function definition itself''')
print('''Arguments are the actual values used when the function is called ''')


#%%

def changeme( my_list ):
   # "This changes a passed list into this function"
   my_list = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", my_list)
   return

my_list = [10,20,30]

changeme(my_list)

print(my_list)



# %%
print('--------------SCOPE IN FUNCTION-------------------')
print('--------------Local Scope Sample-------------------')
print('The local scope or function scope is a Python scope created at function calls')
x = 'global'

def f():

    x = 'Local variable in a simple function'
    print(x)

f()
print()
print('''Since you can’t access local names from statements that are outside the function, 
different functions can define objects with the same name. ''')


# %%
print('--------------SCOPE IN FUNCTION-------------------')
print('--------------Enclosing (or nonlocal) scope Sample-------------------')
print('''Enclosing (or nonlocal) scope is a special scope that only exists for nested functions.''')

# Enclosing function
def outer_func():

    var = 100 # nonlocal name or enclosing

    # enclosed function/nested function
    def inner_func():
       print(f"Printing var from inner_func(): {var}") 
    

    inner_func()
    print(f"Printing var from outer_func(): {var}")

print('''Names that you define in the enclosing Python scope are commonly known as nonlocal names.''')   
print()
outer_func() 

# Note: In a sense, inner_func() is a temporary function that comes to life only during the execution of its enclosing function, 
# outer_func(). Note that inner_func() is only visible to the code in outer_func().


# %%
print()
print('--------------Enclosing Scope Sample 2-------------------')
x = 'global'

def f():
    x = 'enclosing'


    def g():
        print(x)

    g()

f()

# %%
print()
print('--------------Enclosing Scope Sample 3-------------------')
x = 'global'

def f():
    x = 'enclosing'


    def g():
        x = 'LOCAL in inner function'
        print(x)

    g()

f()

# %%
print('--------------Enclosing Scope Sample 4-------------------')

# Enclosing function
def outer_func():

    var = 100 # nonlocal name or enclosing

    # enclosed function/nested function
    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        # All the names that you create in the enclosing scope are visible from inside inner_func(), 
        # except for those created after you call inner_func()

       
        print(f"Printing var from inner_func(): {another_var}")  
        # NameError: free variable 'another_var' referenced 
        # before assignment in enclosing scope     

    inner_func()
    another_var = 200
    print(f"Printing var from outer_func(): {var}")
    

print('''Names that you define in the enclosing Python scope are
 commonly known as nonlocal names.''')   
print()
outer_func() 



#%%
print('--------------SCOPE IN FUNCTION-------------------')
print('--------------Global Scope Sample-------------------')
# GLOBAL SCOPE
x = 'global'

def f():


    def g():
        print('Global scope sample: ',x)
    

    g()


f()


#%%
print('--------------Global Scope Sample 2 (ISSUE)-------------------')
print('''Whenever you assign a value to a name in Python, one of two things can happen:
    You create a new name
    You update an existing name''')
# GLOBAL SCOPE ISSUE
x = 'global'

def f():

    # UnboundLocalError: local variable 'x' referenced before assignment
    print('Global scope sample: ',x)  # type: ignore
    x = 'new value'
    print(x)

    


f()
# %%

print('--------------Global Scope Sample 3 (ISSUE)-------------------')
 # you can’t assign global names inside functions unless you explicitly declare them as global names
 # using a global statement

var = 100  # A global variable

def increment():
    # Try to update a global variable
    var = var + 1    # type: ignore

increment()     
# %%
print('--------------Global keyword Sample 4 (RESOLVED)-------------------')
 # you can’t assign global names inside functions unless you explicitly declare them as global names
 # using a global statement
 # to fix this issue, we will use global statement

var = 100  # A global variable

def increment():
    global  var
    var = var + 1  # Try to update a global variable
    return var


result = increment()
print(result)
result = increment()
print(result)   




# %%
import os

listing = os.walk('D:\Books')
for root, directories, files in listing:
    print(root)
    for d in directories:
        print(d)
    for file in files:
        print(file)



#%%
import os


def list_directories(s_path):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop, "Directory ", f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop, f)

    tab_stop = 0
    if(os.path.exists(s_path)):
        print("Directory listing of ", s_path)
        dir_list(s_path)
    else:
        print(s_path, " does not exist")



list_directories('D:\English Test')
# %%
import os

s_path = 'D:\English Test'
files = os.listdir(s_path)
print(files)

'''
The os.path.join() function constructs a pathname out of one or more partial pathnames. 
In this case, it simply concatenates strings. Calling the os.path.join() function 
will add an extra slash to the pathname before joining it to the filename.
'''

for f in files:
    print(os.path.join(s_path, f))


# %%
def spam1():

    def spam2():
        nonlocal x

        def spam3():
            nonlocal x
            x += " hello"
            z = "even more spam3 " + x
            print("In spam3(), locals are {}".format(locals()))
            return z


        x += "add new to spam2()"
        y = "more spam2 " # y must exist before spam3 is call
        y += spam3()      # DO NOT COMBINE THESE ASSIGNMENTS
        print("In spam2(), locals are {}".format(locals()))
        return y

    x = "Spam1 " # x must exist before spam2 is call
    x += spam2() # DO NOT COMBINE THESE ASSIGNMENTS
    print("In spam1(), locals are {}".format(locals()))
    return x

    
print(spam1())

# %%
