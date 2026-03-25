
password = input("Enter password: ")

length_ok = len(password) >= 10
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "@#$%&!"


for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

if length_ok and has_upper and has_lower and has_digit and has_special:
    print("STRONG")
else:
    print("WEAK")