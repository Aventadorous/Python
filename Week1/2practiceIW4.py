import math
a = int(input("a: "))
b = int(input("b: "))
c = math.sqrt(a**2 + b**2)

S = a + b + c
P = (a * b) / 2

print('Area:', '%.2f' % S)
print('Perimeter:', '%.2f' % P)
