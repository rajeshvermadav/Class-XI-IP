 #Identity operators
a = 'Rajesh'
b = 'Rashi'

print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

print(a is b)
print(a is not b)
if (a is not b):
	print("Line 2 - a and b have same identity")
else:
	print("Line 2 - a and b do not have same identity")
