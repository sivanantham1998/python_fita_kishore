try:
    a=9/0
    print(a)
except NameError as e:
    print("enter valid input",e)
except ZeroDivisionError as e:
    print("division by zero",e)
except Exception as e:
    print("something went wrong",e)
finally:
    print("finally block")



def task(name,age):
    if age>=18:
        print("eligible")
    else:
        raise Exception("not eligible kindly quit the interview")
try:
    task("siva",17)
except Exception as e:
    print(e)
