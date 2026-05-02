# print(True+True)
# print(True+False)
# print(False+False)
# print(False+True)


# if False:
#     print('this is true statement')
#     print("Another true statement")
# else:
#     print('this is false statement')
#     print("Another false statement")


# positive or negative or zero

#elif statement

a=0
if a>0:   #0>0 is true
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

# nested if statement

age=20
weight=45
if age>=18:   # 20>=18 is true
    print("Eligible")
    if weight >=50: # 55>=50 is true
        print("Donote blood")
    else:
        print("Not Eligible for blood donation")
else:
    print("Not Eligible")
    if True:
        print("Else part fine")
    else:
        print("Else part not fine")


mark=76
match mark:
    case _ if mark>=90:
        print("Grade A")
    case _:
        print("Grade B")


if (mark>=90) and (mark<=100):   # 85>=90 false 85<=100 true     false and true
    print("Grade A")
elif (mark>=80) and (mark<90):   # 85>=80 true 85<90 true     true and true
    print("Grade B")
elif(mark>=70) and (mark<80):
    print("Grade C")
else:
    print("Grade Fail")

a=200
b=100

if(a>b):  #(20>10)
    # print("a is greather than b")
    print(f"a is {a} and b is {b} so a is greathar than b")
else:
    print(f"a is {a} and b is {b} so b is greathar than a")



year=1996

if year%4==0 and  year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not a leap year")