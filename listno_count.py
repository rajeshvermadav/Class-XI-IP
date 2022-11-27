#
#nums = [1, 4, 6, 7, 4,1, 4, 6, 4, 7, 4]
#count = 0
#for num in nums:
  #  if num == 4:
    #  count = count + 1

  #return count

#print("Counted Number %d" %num)
#print("No of times:", count)

#print("Entered List",nums)
#print(list_count_4([1, 4, 6, 4, 7, 4]))

x= 4
y= 6
gcd = 1

if x % y == 0:
    #print(y)
    pass

for k in range(int(y / 2), 0, -1):
    if x % k == 0 and y % k == 0:
        gcd = k
        break
    #return gcd


print(x,y)
print(k)