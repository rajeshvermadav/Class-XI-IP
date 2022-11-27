#demo Type conversion
num_int1 = 12
num_str1 = "45.50"
num_flo = 10.23

print("Data type of num_int:",type(num_int1))

print("Data type of num_str before Type Casting:",type(num_str1))
print("Data type of num_float",type(num_flo))


num_str1 = float(num_str1)

print("Data type of num_str after Type Casting:",type(num_str1))

num_sum = num_flo + num_str1

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
