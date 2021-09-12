#%%
from contents import recipes

def my_deepcopy(d : dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash an AttributError if the values are not lists or dictinaries.


    Parameters
    ----------
    d : dict
        The dictionary to copy

    Returns
    -------
    dict
        A copy of `d`, with the values being copies of the original values

    """
    new_dict = {}

    for key, value in d.items():
        #print(key,value)
        new_value= value.copy()
        new_dict[key] = new_value
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])  
print(recipes["Butter chicken"]["ginger"])      
# %%
