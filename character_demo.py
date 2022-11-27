#program to display indivual character

name = input("Enter any name")
print("Lenght of the string is :", len(name))
print("Location or memmory address of the Character :",len(name)-1)
print("Character is :", name[len(name)-6])

print("Substring is :",name[1])
print("Substring is :",name[-1])
print("Substring is :",name[::1])
print("Reverse string:", name[::-1])
