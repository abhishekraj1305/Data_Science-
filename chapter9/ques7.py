#WRP to remove given word from a list and strip it at same time 

# def rem(lst, word):
#     n = []
#     for i in lst:
#         if not(i == word):
#             n.append(i.strip(word))
#     return n

# lst = ["apple", "banana", "cherry", "date", "fig", "grape"]
# print(rem(lst, "banana"))

def rem(lst, word_to_remove):
    # Logic: "For every item in the list, strip its spaces, 
    # but ONLY if the item is not the word we want to delete."
    return [i.strip() for i in lst if i != word_to_remove]

# Test
fruits = [" apple ", "banana", "  cherry", "date ", " banana", " fig ", "grape"," Guava","  Watermelon "]
result = rem(fruits, "fig")

print(result)
# Output: ['apple', 'cherry', 'date', 'banana', 'grape', 'Guava', 'Watermelon']