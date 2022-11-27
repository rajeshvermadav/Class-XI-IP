# Example Membership operator

a = 10
b = 'Raman'
lst = [1, 2, 3, 4, 5,'Raman' ]

print(a in lst)
print( b in lst)
if(a in lst ):
	print ("Line 1 - a is available in the given list")
else:
	print ("Line 1 - a is not available in the given list")

if(b not in lst ):
	print ("Line 2 - b is not available in the given list")
else:
	print ("Line 2 - b is available in the given list")
