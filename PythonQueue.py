names = []

for x in range(10):
    names.append(input("Enter Name: "))
print(names)

for x in range(len(names)):
    print(names.pop(0))
print(names)
