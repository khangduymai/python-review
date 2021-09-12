
#%%
class  Kettle(object):

    # Attributes are created inside the class

    # Creating class attributes

    power_source = "ELECTRICITY"

    # __init__ to create instance attributes
    # The __init__ method is used to initialize an instance
    # make and price in the below example are instance attributes (instance variable)
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

kenwood = Kettle("Kenwood", 8.99)

print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print("Assign new value price for kenwood: ", kenwood.price)
print()

hamilton = Kettle("Hamilton", 10.99)

print("Model: {} = {}, Model: {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Model: {0.make} = {0.price}, Model: {1.make} = {1.price}".format(kenwood,hamilton))
print()

# Atributes can be dynamically created by arbitrary new attributes for existing instances of a class. 
# We do this by joining an arbitrary name to the instance name, separated by a dot "."
# Creating new instance attribute from existing instance
print("Dynamically create arbitrary new attributes for existing instances of a class")
kenwood.power = 15
print("kenwood.power =", kenwood.power)
print()

# Checking the result of class attribute (class variable)
print("The power source of {} is {}".format(kenwood.make, kenwood.power_source))
print("The power source of {} is {}".format(hamilton.make, hamilton.power_source))
print("The power source of {} is {}".format(Kettle, Kettle.power_source))
print()

print("The list of attributes of object: {} is {}".format(kenwood, kenwood.__dict__))
print("The list of attributes of object: {} is {}".format(hamilton, hamilton.__dict__))
print("The list of attributes of object: {} is {}".format(Kettle, Kettle.__dict__))
print()

#%%
print("Switch to atomic power")
Kettle.power_source = "ATOMIC"
print("Class Kettle changed its class attribute to: ", Kettle.power_source)
print("The power source of {} is {}".format(Kettle, Kettle.power_source))


kenwood.power_source = "GAS (Change the instance variable from existing instance)"
print("The power source of {} is {}".format(kenwood.make, kenwood.power_source))

print("The power source of {} is {}".format(hamilton.make, hamilton.power_source))



#%%
print('''
1) Class: template for creating objects. All objects created using the same
class will have the same characteristics.
2) Object: an instance of the calss.
3) Instantiate: create an instance of a class.
4) Method: a function defined in a class.
5) Attribute: a variable bound to an instace of a class
''')

# %%
# Every object in python has an attribute which is denoted by __dict__
print('''A special attribute of every module is __dict__.
FORMAT: object.__dict__''')
print()
print("Defining object atributes using __dict__")
print(kenwood.__dict__)
print()
print(Kettle.__dict__)
print()
print(dir())

# %%

class Robot():
    pass



print("Attributes can be bound to class names as well")
Robot.brand = 'Kuka'

x = Robot()
print(x.brand)
print()

# create new instance attribute for x object
x.brand = "Thales"
print('Brand of Robot object: ',Robot.brand)
print('Brand of x object: ',x.brand)
print("x.__dict__ ", x.__dict__)
print()

# create new object y
y = Robot()
print('Brand of y object: ', y.brand)
# Checking y's attributes
print("y.__dict__ ", y.__dict__)



