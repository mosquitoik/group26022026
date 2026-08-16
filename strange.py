def foo():
    print(1111)


foo()

print(foo)

print(type(foo))

foo.data = {"name": "alex"}
print(foo.__dict__)