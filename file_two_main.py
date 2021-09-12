
#%%
# Python module to import

def function_three():
   print("Function three in file_two is executed")


def function_four():
   print("Function four in file_two is executed")


# print("File two __name__ is set to: {}" .format(__name__))   


if __name__ == "__main__":
    print("File two __name__ is set to: {}" .format(__name__))    
    print("File 2 executed when ran directly")
else:
    print("File 2 executed when imported")
# %%
