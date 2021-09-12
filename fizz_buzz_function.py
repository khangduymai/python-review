#%%
def fizz_buzz(n: int) -> str:
    """
    Print FIZZ_BUZZ if the number is divisible by 3 and 5.\n
    Print FIZZ  if the number is divisible by 3.\n 
    Print BUZZ  if the number is divisible by 5.\n 
    Print the `n` number if not all the cases above

    Parameters
    ----------
    n : int

    """

    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"    

    if n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)           


for i in range(1,21):
    print(fizz_buzz(i))
# %%
