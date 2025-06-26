marks = {
    "Prince": 100,
    "Shubham": 56,
    "Rahul": 23,
    0: "Prince"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Prince": 99, "Renuka": 100})
print(marks)

# print(marks.get("Prince2")) # return None
# print(marks["Prince2"]) # Returns an error