age = 18
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)  # Output: Eligible



age = 20
is_student = False

if age >= 18 and not is_student:
    print("Eligible for full-time job.")
