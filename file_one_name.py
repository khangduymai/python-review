#%%
# Python module to execute
import file_two_main
# from file_two import function_three

# print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one in file_one is executed")

def function_two():
   print("Function two in file_one is executed")


print("File one __name__ is set to: {}" .format(__name__))



if __name__ == '__main__':
   print("File one executed when ran directly")
   function_two()
   # file_two.function_three()
   # function_three()
else:
   print("File one executed when imported")



# %%
