num = eval(input("Enter a list:"))
num.sort()
print("Sorted in ascending order",num)
num.sort(reverse = True)
print("Sortd list in descending order:",num)


number = list(input("Enter list:"))
number.sort()
print("Sorted list in ascending order:",number)
number.sort(reverse = True)
print(" sorted list in descending order:",number)


adict= {'Bhavana':1,'Richard':2,'FIROZA':10,'aRSHNOOR':20}
temp = 0
for value in adict.values():
    temp = temp+value
print(temp)
