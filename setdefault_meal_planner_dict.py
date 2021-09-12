
#%%
from contents import pantry, recipes

# dict comprehensive
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
shopping_list = {}

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add a tuple containing `item` and `amount` into type `data` dict

    Parameters
    ----------
    data : list
        
    item : str
        
    amount : int
        
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


for index, key in enumerate(recipes):
    #print(index, key)
    display_dict[str(index + 1)] = key

#print(display_dict)

while True:
    #Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print('-------------------------')
    for key, value in display_dict.items():
        print(f'{key} - {value}')  

    choice = input(">:")

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice] 
        print(f"You have selected {selected_item}")  
        print('Checking ingredients... ... ...')
        print('... ... ... ... ... ... !!! !!!')   
        ingredients = recipes[selected_item]
        # for each_ingredient in ingredients:
        #     print(each_ingredient)
        print(ingredients)
        print()
        # for food_item in ingredients:
        #     if food_item in pantry:
        #         print(f"\t{food_item} - OK")
        #     else:
        #         print(f"\t You don't have a necessary ingredient: {food_item}")    
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} - OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for each_item in shopping_list.items():
    print(each_item)                     

    
# %%
