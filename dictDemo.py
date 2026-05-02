a={
    "name":"siva",
    "age":29,
    "location":"erode",
    "friends":["arun","boopathy","kishore"]
}
print(a)
print(type(a))

print(a.get("age"))

print(a.keys())
print(a.values())

print(a.items())

a["email"]="[EMAIL_ADDRESS]"
print(a)
a["name"]="kishore"
print(a)

a.pop("name")
print(a)

print(a.get("friends"))