def a():
    print("function started")
    
    print("function ended")

a()

# parameters,arguments,global variable,local variable,return statement,default parameter

z=100
def add(x,y):
    c=1000
    print("x value is",x)
    print("y value is",y)
    return x+y+z+c
    print("hello welcome")

add(4,6)
add(10,199)
add(89,-89)
print(z)

# after return
print(add(4,6))

def sub(x=60,y=10):
    print("inside sub")
    return x-y

print(sub(30,15))
print(sub())



# multiple arguments
def sample(**args):
    print(args)

sample(name="siva",age=29,location="chennai",mobileno=9090909090)

# lambda function

mul=lambda g,h:g*h
print(mul(4,5))
print(mul(10,1000))