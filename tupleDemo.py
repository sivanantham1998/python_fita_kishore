a=(8,4,0,8.90,7.9,"html","css",False,7j,"html")
print(a)
print(type(a))
print(len(a))
print(a[5])
print(a[-4])
print(a[0:5])

print(a.count("html"))
a=list(a)
a.append(100)
a.extend([200,300,400])
print(a)
a=tuple(a)
print(a)

    