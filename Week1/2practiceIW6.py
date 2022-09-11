import math
typ = int(input("Choose the shape:\n1.Triange\n2.Rectangle\n3.Circle\n"))
if typ == 1:
    a = int(input("base: "))
    h = int(input("height: "))
    print('Area', (a * h) / 2)
elif typ == 2:
    l = int(input("length: "))
    b = int(input("width: "))
    print('Area', l * b)
else:
    r = int(input("radius: "))
    print('Area', math.pi * r ** 2)   
