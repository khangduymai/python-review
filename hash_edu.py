#%%

data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy")
]


def simple_hash(s: str) -> int:
    """Simple hashing for educational purpose

    Parameters
    ----------
    s : str
        

    Returns
    -------
    int
        
    """
    basic_hash = ord(s[0])
    return basic_hash % 10


def get(k: str) -> str:
    """
    Return the value of a key or None if the key does not exist

    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None    




# for key, value in data:
#     # print(key)
#     # print(value)
#     h = simple_hash(key)
#     print(key, h)


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    #h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print()
print(keys)
print(values)
print()
value = get("lemon")
print(value)

#%%
list_test = ['a', 'b','']

if list_test[2]:
    print("true")
else:
    print("false")    

