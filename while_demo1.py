ch = "Y"

name = input("Enter Your Name")
age = int(input("Enter Your Age"))
while ch == 'Y':
    print("Name", name)
    print("age", age)

    ch = input(" Do you want to continue Y/N")
    if ch == 'yes':
        continue
