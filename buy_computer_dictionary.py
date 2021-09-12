#%%
available_parts = {"1":"PC",
                   "2":"Monitor",
                   "3":"Keyboard",
                   "4":"Mouse",
                   "5":"Mouse mat",
                   "6":"HDMI"
                   }

current_choice = None
computer_parts = []

while current_choice != "0":
    if current_choice in available_parts:
        choosen_part = available_parts[current_choice]
        if choosen_part in computer_parts:
            print(f"Removing {choosen_part}")
            computer_parts.remove(choosen_part)
        else:    
            print(f"Adding {choosen_part}")
            computer_parts.append(choosen_part)
        print(f"YOUR CURRENT LIST CONTAINS: {computer_parts}")    
    else:
        print("Please add options to the list")
        for key, value in available_parts.items():
            print(f"No. {key}: {value}")    
        print("0 to exist")
    current_choice = input("Please choose")    
# %%
available_parts = {"1":"PC",
                   "2":"Monitor",
                   "3":"Keyboard",
                   "4":"Mouse",
                   "5":"Mouse mat",
                   "6":"HDMI"
                   }

current_choice = None
computer_parts = {} #create empyy dict

while current_choice != "0":
    if current_choice in available_parts:
        choosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {choosen_part}")
            computer_parts.pop(current_choice)
        else:    
            print(f"Adding {choosen_part}")
            computer_parts[current_choice] = choosen_part
        print(f"YOUR CURRENT LIST CONTAINS: {computer_parts.values()}")    
    else:
        print("Please add options to the list")
        for key, value in available_parts.items():
            print(f"No. {key}: {value}")    
        print("0 to exist")
    current_choice = input("Please choose")    
# %%
