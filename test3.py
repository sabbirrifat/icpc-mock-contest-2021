x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x == y == z:
    print("Equilateral Triangle")
elif x == y or y== z or z==x :
    print("Isosceles Triangle")
else:
    print("Bad Triangle")