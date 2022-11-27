a = int(input("enter First Number"))
b = int(input("enter Second Number"))
c = int(input("Enter Thrid number"))

if a>=b>=c or a>=c>=b:
    print("A is grater than all")
elif b>=a>=c or b>=c>=a:
    print("B Is greater than all")
elif c>=a>=b or c>=b>=a:
    print("c is greater than all")

a,b = 0,0
if (a == b):
        print(c)


A = 3-4+10
B=5*6
C = 7.0/2.0
D = "Hello" * 3
print ("Value are :", A, B, C, D)
print("Rajesh", *5)