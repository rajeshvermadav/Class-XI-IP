def contracting(l):
   x=0
   old_diff=abs(l[x]-l[x+1])
   for i in range(1,len(l)-1):
       diff=abs(l[i]-l[i+1])
       if diff<old_diff:
           old_diff=diff
       else:
           return False
   return True


def counthv(l):
   count = [0, 0]
   for i in range(1, len(l)-1):
       if l[i - 1] > l[i] < l[i + 1]:
           count[1] += 1
       elif l[i - 1] < l[i] > l[i + 1]:
           count[0] += 1
   return count
def rotate(m):
   # Initializing an empty nxn matrix, similar to the input dimension of m
  new_m = [[0 for a in range(len(m[0]))] for i in range(len(m))]
   # Transpose action of the matrix done below
  for i in range(len(m)):
       for j in range(len(m[i])):
        new_m[j][i]=m[i][j]
        for x in range(len(new_m)):
            new_m[x].reverse()
   # Printing the original matrix
            print(m)
   # Printing the output reversed matrix
        print(new_m)


def mystery(l):

 if l == []:
     return(l)
 else:
    return(mystery(l[1:])+l[:1])
print(mystery([22, 14, 19, 65, 82, 55]))

pairs = [ (x,y) for x in range(4,1,-1) for y in range(5,1,-1) if (x+y)%3 == 0 ]
print(pairs)

wickets = {"Tests":{"Kumble":[3,5,2,3],"Srinath":[4,4,1,0],"Prasad":[2,1,7,4]},"ODI":{"Kumble":[2,0],"Srinath":[1,2]}}
#wickets["ODI"]["Prasad"][0:] = [4,4]
#wickets["ODI"]["Prasad"].extend([4,4])
wickets["ODI"]["Prasad"] = [4,4]
#wickets["ODI"]["Prasad"] = wickets["ODI"]["Prasad"] + [4,4]
print(wickets)


hundreds = {}
hundreds["Tendulkar, international"] = 100
hundreds["Tendulkar"] = {"international":100}
hundreds[("Tendulkar","international")] = 100
#hundreds[["Tendulkar","international"]] = 100


def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)

lst = [1,2,4,5,8,7,5,]
def onehop(lst):
    data = lst
    data.sort(key=lambda tup: tup[0])  # Sorting all tuples in ascending order via first element
    ans = []  # Creating a blank List
    for ele in lst:  # Looping through all elements
        x, y = ele  # Storing Tuple value in x and y
        for ele1 in lst:  # For finding next hop for all destinations
            if ele != ele1:  # To check if it's not the same element in loop
                xx, yy = ele1  # Storing another tuple's value in xx, yy
                if y == xx and x != yy and (x, yy) not in ans:  # checking conditions for adding to ans.
                    # y == xx to check if second element of first tuple is equal to first element of second tuple.
                    # Only then Next Hop is possible
                    # x != y, so that we don't get tuples like (2,2), (3,3) etc.
                    # (x,yy) not in ans, is to ensure that one next hope isn't repeated twice.
                    ans.append((x, yy))  # Adding tuple to ans if all conditions satisfied.
    ans = sorted(ans, key=lambda tup: (tup[0], tup[1]))  # Sorting all tuples in ascending order via first element and second element.
    # ans.sort(key=lambda tup: tup[0])
    #return ans
    lst = [1, 2, 4, 5, 8, 7, 5]
    print(lst)