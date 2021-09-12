#%%

available_parts = ["PC",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "Mouse mat",
                   "HDMI"]

current_choice = "-"
computer_parts = []

#valid_choice = [str(i) for i in range(1,len(available_parts)+1)]
valid_choice = []
for i in range(1, len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)

while current_choice != '0':
    if current_choice in valid_choice:
        
        index= int(current_choice) -1
        choosen_part = available_parts[index]
        
        
        if choosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(choosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(choosen_part)    
        
        print("Your currnet computer parts:",computer_parts)
                                               
        # if current_choice == '1':
        #     computer_parts.append("PC")
        # if current_choice == '2':
        #     computer_parts.append("Monitor")
        # if current_choice == '3':
        #     computer_parts.append("Keyboard")
        # if current_choice == '4':
        #     computer_parts.append("Mouse")
        # if current_choice == '5':
        #     computer_parts.append("Mourse mat")
        # if current_choice == '6':
        #     computer_parts.append("HDMI")
        
    else:
        print("Please choose the options below:")
        # total_available_parts = len(available_parts)
        # for i in range(total_available_parts):
        #     print(i, available_parts[i])
        
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) +1,part))
        for number, part in enumerate(available_parts):
             print("{0}: {1}".format(number+1,part))
                
        
    current_choice = input("Please choose option")    

if current_choice == '0':
    print('''Thanks for shopping with us
Below are your items:''')
    print(computer_parts)

# %%
# #sample emumarate with sequence string
# for index, char in enumerate("abcdef"):
#     print("{0}: {1}".format(index, char))

# %%
