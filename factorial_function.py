
#%%

def factorial(n: int) -> int:
    """
     Return factorial number

     Parameters
     ----------
     n : int
         

     Returns
     -------
     int
         
    """
    result = 1
     
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2,n+1):
            result *= i

        return result


for i in range(0,35):
    print(i,factorial(i))



# %%
