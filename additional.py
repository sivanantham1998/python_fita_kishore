a=[
    {"name":"siva","age":24},
    {"name":"boopathy","age":26},
    {"name":"kishore","age":27},
    {"name":"arun","age":25},
    {"name":"muthu","age":26}
]
print(len(a))
for i in range(len(a)):
    print(a[i])

for i in a:
    print(f"name is {i.get('name')} and age is {i.get('age')}")


def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)


