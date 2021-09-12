
#%%
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = farm_animals | wild_animals
print(all_animals_2)


# %%
from prescription_data import adverse_interactions

med_to_watch = set()

for interaction in adverse_interactions:
    med_to_watch = med_to_watch.union(interaction)

print(sorted(med_to_watch))    


# %%
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

things_that_bite = snakes.union(spiders)
# things_that_bite = snakes | spiders
things_that_sting = scorpions | vespas
# things_that_sting = scorpions.union(vespas)

arachnids = scorpions | spiders
# arachnids = scorpions.union(spiders)
