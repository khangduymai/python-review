#%%
def fibonacci(n: int) -> int:
    """
    Return the `n`th Fibonacci number, for possitve `n`.

    """

    if 0 <= n <=1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

#%%
def is_palindrome(word: str) -> bool:
    """[summary]
        Check if a string is a palindrome.
        A palindrome is a string that reads the same forwards as backwards.

    Parameters
    ----------
    word : [String] The word to check

    Returns
    ----------
        True if `word` is a palindrome, False otherwise. 
    """
    return word[::-1].casefold() == word.casefold()

print(is_palindrome('madam'))   


# %%
def multiply(x: float, y: float) -> float:
    return x*y

print(multiply(11,2))    

# %%
def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """[summary]
        Print a string centered, with ** either side.

    Parameters
    ----------
    text : str
        The string to print, by default " "
    screen_width : int
        The overall width to print within
        (including the 4 spaces for the ** either side), by default 80

    Raises
    ------
    ValueError
        If the supplied string is too long to fit.
    """

    if len(text) > screen_width -4:
        raise ValueError("String {0} is larger than specified width {1}"
                        .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)      

banner_text("*")                          


#%%

def sum_numbers(*args) -> float:
    """
    Calculate the sum of all the numbers

    Returns
    -------
    float
        Return the sum 
    """

    result = 0

    for number in args:
        result += number
    
    return result    


sum_numbers(1,2,3)
# %%
