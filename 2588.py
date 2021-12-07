a = input()
a=int(a)
b = input()
b=str(b)

for x in range(len(b)):
    print(a * int(b[2 - x]))

print(a * int(b))