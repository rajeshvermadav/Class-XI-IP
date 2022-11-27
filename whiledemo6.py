
c_odd = 0
c_even = 0

while True:
    n = input("Enter a sequence of number [Type END or end to exit]:")
    if n == "END" or n == 'end':
        break
    n = int(n)
    if n%2 == 0:
        c_even = c_even+1
    else:
        c_odd = c_odd+1
print("Number of Even", c_even)
print("Number of odd", c_odd)


