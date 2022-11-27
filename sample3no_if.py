#Program to input three numbers calculate sum of numbers and non duplicate numbers
s1 = s2 = 0

a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

s1 = a + b + c
if a != b and a != c:
    s2= s2 + a
print(a)
if b!= a and b != c:
   s2 = s2 + b
if c != a and c != b:
   s2 = s2 + c
print(" Numbers are : ",a,b,c)
print(" Sum of three numbers is:", s1)
print(" Sum of non - duplicate number is :", s2)






