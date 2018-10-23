scale = float(input("Enter a magnitude of the earthquake: "))
if scale >= 8.0:
    print("Most structures fall")
elif scale >= 7.0:
    print("Many buildings destroyed")
elif scale >= 6.0:
    print("Many buildings considerably damaged, some collapse")
elif scale >= 4.5:
    print("Damage to poorly constructed buildings")
elif scale <= 4.5:
    print("No destruction of buildings")
