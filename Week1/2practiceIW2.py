import math
x = float(input("A:"))
y = float(input("B:"))
H =  math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(math.exp(x) + math.exp(-x))) / (math.pow((math.exp(-x) + math.exp(x)),3) * math.pow((math.sin(4 * y) + math.cos(2 * y) - 2),2))
print(H)
