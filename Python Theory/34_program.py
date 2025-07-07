
def rem(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l = ["Prince", "Rahul", "Shubham", "Sidharth"]

print(rem(l, "th"))