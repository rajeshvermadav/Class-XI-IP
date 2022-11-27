n=1
c_even = 0
c_odd = 0
#n = int(input("Enter a final range of Number"))
for x in range(n):
    if x%2 == 0:
        c_even = c_even+1
    else:
        c_odd = c_odd+1
print(x)
print("Total Even Numbers in a range", c_even)
print("Total odd Numbers in a range", c_odd)
