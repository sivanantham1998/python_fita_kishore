# arithmetic operators +,-,*,/,%,**,//
a=8
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) #2**3=8   2*2*2
print(a//b)
print(a%b)
# assignment operators =,+=,-=,*=,/=
a=20
a+=5   #a=a+5
print(a)
a-=20   #a=25-20
print(a)
a*=2
print(a)
a/=5
print(a)

# comparsion operators ==,!=,>,<,>=,<=
a=2
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators and,or,not
print(True and False)
print(True or False)
print(not False)

#bitwise operators
a=2
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)

#membership operator in,not in
a="kishore"
print("s" in a)
print("h" not in a)

#identity operator is,is not

print(a is "kishore")
print(a is not "siva")

#ternary operator

a=10

ans= "adult" if a>=18 else "child"
print(ans)

# operator precedence

print((2*3)+2)