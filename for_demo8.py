x = [21,22,23,24,25,26]
c_even = 0
c_odd = 0
for n in x:
    x = input("Enter a series of number")

    if n%2 == 0:
        c_even = c_even+1
    else:
        c_odd = c_odd+1

print("No of Even:", c_even)
print("No of Odd:", c_odd)
