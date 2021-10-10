#%%
from OOP_enemy_main_inheritance import Enemy, Troll, Vampyre

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)
print("Monster got damage")
random_monster.take_damage(4)
print(random_monster)
print("Monster got damage")
random_monster.take_damage(8)
print(random_monster)
print("Monster died")
random_monster.take_damage(9)
print(random_monster)

print()
print('----------------------------------------------')
print('''CASE1: When the Troll class has no __init__, 
it uses default Enemy class''')
print()

# ugly_troll = Troll()
# print("Ugly troll - {}".format(ugly_troll))
# another_troll = Troll('trojan', 18, 1)
# print("Another troll - {}".format(another_troll))
# brother = Enemy("Uza", 23)
# print("Brother troll - {}".format(brother))
# print()
# print('----------------------------------------------')
# print()

print()
print('----------------------------------------------')
print('''CASE2: When the Troll class has defined __init__ with parameter name''')
print()


ugly_troll = Troll('Puggy')
print("Ugly troll - {}".format(ugly_troll))
another_troll = Troll('trojan')
print("Another troll - {}".format(another_troll))
brother = Enemy("Uza")
print("Brother troll using Enemy class - {}".format(brother))
brother_1 = Troll("Uza")
print("Brother troll using Troll class - {}".format(brother_1))
print()


print()
print('----------------------------------------------')
print('''Starting Troll subclass method''')
print()

ugly_troll.grunt()
another_troll.grunt()
brother_1.grunt()
print()

another_troll.take_damage(18)
print("Another troll got damaged:", another_troll)
another_troll.take_damage(30)
print("Another troll got damaged:", another_troll)

print()
print('----------------------------------------------')
print('''Creating Vampyre object''')
print()

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print("Vampyre got damaged:", vamp)
print()

while vamp.alive:
    vamp.take_damage(1)

# %%

