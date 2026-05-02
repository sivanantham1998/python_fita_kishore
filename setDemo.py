a={3,5,6,"html","python","css"}
print(a)
print(type(a))
print(len(a))

# union
b={3,6,"js"}
print(a.union(b))
print(a|b)
#intersection
print(a.intersection(b))
print(a&b)

# difference
print(a.difference(b))
print(a-b)
#symmetric difference
print(a.symmetric_difference(b))
print(a^b)
# clear
a.clear()
print(a)

del a
print(a)