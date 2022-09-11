import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = (b**2) - (4*a*c)

if d > 0:
    answ1 = (-b-math.sqrt(d))/(2*a)
    answ2 = (-b+math.sqrt(d))/(2*a)

    print('The answers are ', answ1,'and', answ2)
elif d == 0:
    print('The answer is', (-b)/(2*a))
else:
    print("No answer")
