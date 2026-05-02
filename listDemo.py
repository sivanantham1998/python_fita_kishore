# a=["html","css","js","jquery","react","r","python","sql","bootstrap","typescript"]
a=[2,4,5,18,20.8,True,8j,"kishore"]
print(a)
print(type(a))

print(a[3])
print(a[-1])
print(type(a[-2]))
print(len(a))

print(a[0:3])
a[0]="hi"
print(a)

# append
a.append("python")
print(a)
# insert
a.insert(1,"hello")
print(a)
# extend
a.extend([100,200,300])
print(a)

# pop
a.pop()
print(a)
a.pop(2)
print(a)

# remove
a.remove("python")
print(a)


for j in a:
    print(j)
    