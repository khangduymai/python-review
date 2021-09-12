import random
#%%
# for i in range(10):
#     print("i is now {}".format(i))
 # %%
# i = 0
# while i <= 10:
#     print("i is now {}".format(i))
#     i +=1
          
# %%
import random
highest = 10
lowest = 1
correctAnswer = random.randint(lowest,highest)

print(correctAnswer)

print(f"please choose a number from {lowest} to {highest}:")

inputAnswer = int(input())

    
while inputAnswer != correctAnswer:
    
    if inputAnswer == 0:
        break
    
    while inputAnswer < lowest or inputAnswer > highest:
        if inputAnswer == 0:
            break
        else:
            print("you are out of the range of the random number")
            inputAnswer = int(input("Please input again"))
    
    if inputAnswer < correctAnswer and inputAnswer != 0:
        print("please guess higher")
        inputAnswer = int(input("Please input again"))
    else:
        print("Please guess lower")
        inputAnswer = int(input("Please input again"))
        
if inputAnswer == 0:
    print("QUIT THE GAME")
else:            
    print(f"your correct answer is {inputAnswer}")

print()

# %%
print('--------------\'SECOND EXAMPLE OF WHILE LOOP\'-------------------')
choice = None
while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        print("Enter choice = None. Then EXIT")
        break
 
    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")



