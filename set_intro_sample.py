#%%

choice = "-"

while choice != '0':
    #if choice in "12345":
    if choice in set("12345"):
        print(f"you choose {choice}")
    else:
        print("Plesase choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input('>>:')    
# %%
