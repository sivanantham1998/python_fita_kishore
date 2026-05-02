print(__name__)
__name__="sample"
print(__name__)

import mathoperation as math_demo
import math
import random
print("addition",math_demo.add_mod(40,60))
print("decrement",math_demo.decrement(100,60))
print("PI value is",math.pi)
print("square root",math.sqrt(9))
print("ceil value is",math.ceil(3.14159))
print("floor value is",math.floor(3.14159))
print("factorial value is",math.factorial(5))

print("random integer",random.randint(1,10))
print("random float",random.random())
print("random choice",random.choice([1,2,3,4,5]))
print("random sample",random.sample([1,2,3,4,5],3))



import requests

url="https://www.w3schools.com/PYTHON/python_modules.asp"

res=requests.get(url)

print(res)