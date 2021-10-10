#%%
import player_getter_setter

khang = player_getter_setter.Player("Khang")

print(khang.name)
print("The number of lives at beginning:",khang.lives)
khang.lives -=1
print(khang)
print()

khang.level = 2
print(khang)

print()
khang.level += 5
print(khang)

print()
khang.level -= 3
print(khang)

print()
khang.score = 100
print(khang)

# %%
