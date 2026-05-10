try:
    a=open("bill.txt","x")
    a.close()
except Exception as e:
    print(e)
    b=open("bill.txt","w")
    name=input("enter the cust_name:")
    b.write(f"Customer name {name}")
    b.close()
    