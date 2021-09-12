#%%
# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}


 
# Text string
text = "LAter in the course, you'll see how to use the collections Counter class."


# Your code goes here ...
text_lower = text.casefold()
alphabet_text = ""


for char in text_lower:
    if char.isalnum():
        alphabet_text += char

count = 1
for each_char in alphabet_text:
    if each_char in alphabet_text:
        word_count[each_char] = word_count.setdefault(each_char,0) + count

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)


# %%
