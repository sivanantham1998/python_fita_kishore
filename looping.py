user ="sivanantham"

for i in user:
    print(i,end=" ")


for i in range(len(user)):
    print(user[:i])


# start,stop,step

for i in range(2,21,3):
    print(i)
else:
    print("Loop Completed")


for _ in range(5):
    print(_)

for i in range(4):
    pass

# nested loop

for i in range(10):
    print("i value is",i,end=" ")
    for j in range(i,10):
        print("j value is",j,end=" ")
    print("\n")



for i in range(1,101):
    if i%2==0:
        print(i,end=" ")
        

for i in range(1,11):
    if i==6:
        # break
        continue
    print(i)


#factorial of a number

n=5
fact=1
for i in range(1,n+1):
    fact=fact*i

print("factorial value",fact)

# while loop

a=1

while a<=5:
    print("a is",a)
    a=a+1


b=5
while b>=0:
    print("b is",b)
    b=b-1

for i in range(5,0,-1):
    print(i,end=" ")



star="*"
for i in range(5):
    print(star*i)



print("1*2=2")
print("2*2=4")
print("3*2=6")
print("4*2=8")
print("5*2=10")

