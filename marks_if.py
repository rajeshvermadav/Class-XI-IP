name = input("Enter Name of Student:")
mark1 = float(input("Enter Marks for Subject-1"))
mark2 = float(input("Enter Marks for Subject-2"))
mark3 = float(input("Enter Marks for Subject-3"))
total = mark1 + mark2 + mark3
per = total/300*100
if per>=75:
    grade = A
elif per>=60 and per<75:
    grade = B
else:
    grade = C
print("Name :", name)
print("Total marks", total)
print("percentage:", per)
print("Grade:", grade)

