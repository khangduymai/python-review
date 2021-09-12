
#%%
from my_deepcopy import my_deepcopy
import copy

original = {
    "khang" : ["Khang", ["data engineer", "biker"]],
    "J-P" : ["Roberts", ["software engineer", "teacher"]],
}


copy1_deepcopy = copy.deepcopy(original)
copy2_mydeepcopy = my_deepcopy(original)


original["khang"].append("Vietnam")
original["J-P"].append("UK")

original["khang"][1].append("Adventurer")
original["J-P"][1].append("biker")

print("Original:", original)
print()
print("copy1_deepcopy:", copy1_deepcopy )
print()
print("copy2_mydeepcopy:", copy2_mydeepcopy )
# %%
