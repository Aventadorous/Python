#Task1
x1 = []
N = int(input("Enter the number for array:"))
x1 = [ int(input()) for i in range(N) ]
x1.reverse()
print(x1)
print(max(x1))
temp1 = 0
for i in x1:
    temp1 += i
average = sum / len(x1)
for i in range(len(x1)):
    if x1[i] == 0:
        x1[i] = average
print(x1)

#Task2
x2 = []
first = []
second = []
N2 = int(input("Enter the number for array:"))
x2 = [ int(input()) for i in range(N2) ]
print('Min:', min(x2))
for i in range (len(x2)):
    if x2[i] >= 0:
        first.append(x2[i])
    else:
        second.append(x2[i])
print(first)
print(second)

#Task3
n3 = int(input("Enter the number"))
D = [ int(input()) for i in range(n3)]
sum3 = 0
for i in range(1,n3,2):
    sum3 += D[i]
print(D)
print(sum3)

x3= [20,12,63,51,14,16,82,36]
print(x3)
for i in range(8):
    if x3[i] < 15:
        x3[i] = x3[i] * 2
print(x3)

#Task4
n4= int(input("Enter the number:"))
x4= [ int(input()) for i in range(n)]
max = x4[0]
max_index = 0
for i in range(len(x4)):
    if x4[i] > max:
        max = x4[i]
        max_index = i
print(max_index + 1)

a4 = [4,9,7,1,8,2,5,3,6]
b4 = []
for i in range(len(a4)):
    if a4[i] % 2 == 1:
        b4.append(a4[i])

if len(b4) == 0:
    print("no such numbers")
else:
    b4.sort()
    print(b4[::-1])


#Task5
x5 = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(x5)):
    print(x5[i],-x5[i])

x5 = [1,1,3,4,5,3,3,9,9,9]
y5 = []
for i in range(len(y5)):
    if y5[i] not in y5:
        y5.append(x5[i])
print(y5)

#Task6
x6 = [ int(input()) for i in range(10)]
sum = 0
for i in range(len(x6)):
    if x6[i] > 5:
        sum += x6[i]


#Task9
n9 = int(input())
x9 = [ int(input()) for i in range(n)]
print(min(x9, key=abs))
print(x9[::-1])

a9 = [1,2,3,4,5,6,7,8,9,10]
b9 = [10,9,8,7,6,5,4,3,2,1]
print(a9)
print(b9)
a,b = b,a
print(a9)
print(b9)

#Task11
n = int(input())
a = [ int(input()) for i in range(n)]
max = 1
for i in range(len(a)):
    if a[i] > max and a[i] % 2 == 0:
        max = a[i]
print(max)

n = int(input())
a = [ int(input()) for i in range(n)]
b = []
for i in range(len(a)):
    if a[i] < 10 and a[i] % 2 == 0:
        b.append(a[i])
    if i == len(a) - 1 and len(b) == 0:
        print("no such numbers")
b.sort()
print(b)

#Task 13
a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [10,20,14,25,17,11,12,13]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)

#Task 14
a = [1,-200,3,4,5,600,7,8,9]
max = a[0]
max_index = 0
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i
a[min_index] = max
a[max_index] = min
print(a)

n = int(input())
a = [ int(input()) for i in range(n)]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] > mean:
        a[i] = 1
print(a)

#Task 15
a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1])

