for i in range(4):
    print(i)


## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)


# Table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")