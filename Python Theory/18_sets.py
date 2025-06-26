e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 
print(s)
#mutable datatype


s = {1, 5, 32, 54,5, 5, 5, "Prince"}

print(s, type(s))
s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))



s = {8, 7, 12, "Harry", [1,2]} # set only allow immutable Datatype
s[4][0] = 9



# Allocation order is random in set

# Hashing:
# Sets use a hash table for storage.
# When an element is added to a set, Python calculates its hash value, which determines where the element is stored internally.

# Unordered Nature:
# Because of hashing, sets do not guarantee any specific order of elements.
# The order of elements might appear random when you print a set, and it may change across different runs.

# Uniqueness:
# Sets only allow unique elements. Duplicate values are automatically discarded.
