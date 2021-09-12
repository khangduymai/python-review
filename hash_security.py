#%%
import hashlib

print("algorithms_guaranteed: ",sorted(hashlib.algorithms_guaranteed))
print()
print("algorithms_available: ",sorted(hashlib.algorithms_available))
# %%

python_program = """for i in range(10):
print(i)
"""

print(python_program)

# Begin to hash the message string
original_hash = hashlib.sha256(python_program.encode('utf8'))
print("Return hash object of the message: ",original_hash)
print("Convert hash object to hex:")
# Hexdigest() method produces a hexadecimal representation of the secure hash
print(f"SHA256: {original_hash.hexdigest()}")
print()
# Modifief the message string
python_program += "print('Code changed')"
print(python_program)
new_hash = hashlib.sha256(python_program.encode('utf8'))
print("Return hash object of the message: ",new_hash)
print("Convert hash object to hex:")
# Hexdigest() method produces a hexadecimal representation of the secure hash
print(f"SHA256: {new_hash.hexdigest()}")

print()
if new_hash.hexdigest() == original_hash.hexdigest:
    print("The code has not been modifed")
else:
    print("STOLEN PASS")    
#%%
# What is encode() doing? Check the code below to see how it work ==> convert string to computer code such Unicode 
for b in python_program.encode('utf8'):
    # print the value in bytes array because hashlib.sha256() and others understanding only bytes array NOT strings
    print(b, chr(b))


