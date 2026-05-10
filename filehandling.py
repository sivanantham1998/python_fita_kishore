import os
# open("filename","mode")
# mode: r,w,a,r+,w+,a+
a=open("filehandling.txt","r")
print(a.read())
a.close()
# remove filehandling
# open("mathoperaion/add.txt")
b=open("function.py","r")
print(b.read())
b.close()

# c=open("demo.txt","x")
# c.close()
# d=open("demo.csv","x")
# d.close()

e=open("demo.txt","w")
e.write("this is demo file\n iam from erode")
e.close()

x=open("demo.txt","a")
x.write("\nappending is working")
x.write("thanks for watch")
x.close()

f=open("demo.csv","w")
f.write("name,city,pincode,location\n")
f.write("fathima,chennai,600001,tamilnadu\n")
f.write("jamal,bangalore,600002,karnataka")
f.close()


g=open("demo.xlsx","w")
g.write("name,city,pincode,location\n")
g.write("fathima,chennai,600001,tamilnadu\n")
g.write("jamal,bangalore,600002,karnataka")
g.close()

os.remove("filehandling.txt")


