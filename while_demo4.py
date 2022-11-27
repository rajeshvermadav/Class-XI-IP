# List Demo
l = ['a','e','i','o','u']
print(type(l))
print(l[0])
print(l[-3])
c = [1,2,3]
d = [4.5,5.5]
v = ['Devansh','Raman','Rashi','Simran','Vanshika']
print(v[2])
print(v[1])
print(v>l)
x = l+v+c+d
print(x)
print(v*3)
for z in l:
    print(z, end='    '"\n")
for a in v:
    print("\n",a, sep='  ')
