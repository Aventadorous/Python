#Task1.1
import math
def area(shape):
    if(shape == 1):
        a = float(input("Enter the length of A:"))
        b = float(input("Enter the length of B:"))
        n = a * b
        print("Area:", n)

    elif(shape == 2):
        r = float(input("Enter the radius:"))
        n = math.pi * (r**2)
        print("Area:", n)
    elif(shape == 3):
        h = float(input("Enter the height:"))
        s = float(input("Enter the base:"))
        n = s * h / 2
        print("Area:", n)
    else:
        print("Bruh :/")

        
shape = int(input("1.Rectangle   2.Circle  3.Triangle"))
area(shape)

#Task1.2
def total(a, b, c):
    
    array1 = [ int(input("Array1:")) for i in range(a) ]
    array2 = [ int(input("Array2:")) for i in range(b) ]
    array3 = [ int(input("Array3:")) for i in range(c) ]
    
    sum1 = sum(array1)
    sum2 = sum(array2)
    sum3 = sum(array3)
    
    answ1 = sum1 / a
    answ2 = sum2 / b
    answ3 = sum3 / c
    
    print(" ")
    print(" ")
    
    
    print("Sum of Array1:", sum1)
    print("Sum of Array2:", sum2)
    print("Sum of Array3:", sum3)
    print(" ")
    print(" ")
    
    print("Average number of Array1 is ", answ1)
    print("Average number of Array2 is ", answ2)
    print("Average number of Array3 is ", answ3)

    
    
    
a = int(input("Enter the number for Array1:"))
b = int(input("Enter the number for Array2:"))
c = int(input("Enter the number for Array3:"))


if(a <= 15 or b <= 15 or c <= 15):
    total(a, b, c)
    
else:
    print("Not more 15 :(")




#Task 2.1
def area(a):
    return (math.sqrt(3) / 4) * a ** 2

a = int(input("Side hexagon: "))
print("Area hexagon is:", area(a)*6)





#Task 2.2
for i in range(3):
    a = int(input("first side: "))
    b = int(input("second side: "))
    print("area of recangle is:", rectangleArea(a,b))



#Task 3.1
def hypot(a,b):
    return math.sqrt(a**2 + b**2)

temp = []
for i in range(2):
        a = int(input("a: "))
        b = int(input("b: "))
        print("hypot of triangle is:",hypot(a,b))
        temp.append(hypot(a,b))

if temp[0] > temp [1]:
    print("hypotrnuses of first triangle is bigger")
elif temp[1] > temp[0]:
    print("hypotrnuses of second triangle is bigger")
else:
    print("hypotrnuses of both triangles are same")



#Task 3.2
def sortString(s):
    return ''.join(sorted(s))



#Task 4.1
def gcd(x,y):
    if (y == 0):
        return abs(x)
    else:
        return gcd(y, x % y)

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
print(math.trunc(a*d / gcd(a*d,b*c)), "/", math.trunc(b*c / gcd(a*d,b*c)))




#Task 4.2
def isInCircle(r,x,y):
    if r > hypotenuses(x,y):
        return True
    else:
        return False

a = int(input("a: "))
b = int(input("b: "))
r = int(input("r: "))

p1 = int(input("p1: "))
p2 = int(input("p2: "))
print(isInCircle(r,abs(p1) - abs(a),abs(p2) - abs(b)))
f1 = int(input("f1: "))
f2 = int(input("f2: "))
print(isInCircle(r,abs(f1) - abs(a),abs(f2) - abs(b)))
l1 = int(input("l1: "))
l2 = int(input("l2: "))
print(isInCircle(r,abs(l1) - abs(a),abs(l2) - abs(b)))





#Task 5.1
def lcm(z,y):
    if z > y:
        greater = z
    else:
        greater = y
    while True:
        if greater % z == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
a /= gcd(a,b)
b /= gcd(a,b)
c /= gcd(c,d)
d /= gcd(c,d)
b2 = lcm(b,d)
d2 = b2
a *= b2 / b
c *= d2 / d
print(a - c, "/", b2)




#Task 5.2
def allDiv(n):
    ans = []
    for i in range(1,n+1):
        if n % i == 0:
            ans.append(i)
    return ans
    
n = int(input("n: "))
print(allDiv(n))




#Task 6.1
a = int(input("a: "))
b = int(input("b: "))

print("gcd of a and b:",gcd(a,b))
print("lcm of a and b:",lcm(a,b))




#Task 6.2
def triangleAreaSemiP(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
h = int(input("diagoal (A,C): "))
print(triangleAreaSemiP(a,b,h) + triangleAreaSemiP(c,d,h))




#Task 7.1
a = int(input("long base: "))
b = int(input("short base: "))
h = int(input("height: "))
t = int(input("leg: "))

print("Area:", triangleArea(a-b,h) + rectangleArea(b,h))




#Task 7.2
def decToOct(n):
    return '{:010o}'.format(n)

a = int(input())
print(decToOct(a))




#Task 8.1
def divByTheirD(n):
    ans = []
    for i in range(1,n+1):
        s = str(i)
        temp = True
        for j in s:
            if int(j) == 0:
                temp = False
            elif i % int(j) != 0:
                temp = False
        if temp:
            ans.append(i)
    return ans

n = int(input("n: "))
print(divByTheirD(n))





#Task 8.2
def swapFirstLast(a):
    a[0],a[len(a)-1] = a[len(a)-1],a[0]
    return a

m = int(input("length of array: "))
A = []
for i in range(m):
    n = int(input("element of array: "))
    A.append(n)

print(A)
print(swapFirstLast(A))






#Task 9.1
def sumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

n = int(input("N: "))
sub = sumOfDigits(n)
ans = 0
while n > 0:
    ans += 1
    n -= sub

print(ans)




#Task 9.2
def prdArr(n):
    prd = 1
    for i in n:
        prd *= i
    return prd

for i in range(3):
    a = random.sample(range(100), 15)
    print(a)
    print(prdArr(a))
    print(meanArr(a,sumArr(a)))





#Task 10.1
def digitsOf(n):
    ans = []
    s = str(n)
    for i in s:
        ans.append(int(i))
    return ans

N = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

ans = []
for i in range(100,N):
    dgts = digitsOf(i)
    if a in dgts:
        dgts.remove(a)
    if b in dgts:
        dgts.remove(b)
    if c in dgts:
        dgts.remove(c)
    if len(dgts) == 0:
        ans.append(i)
print(ans)





#Task 10.2
def revSeq(s):
    s = s.split()[::-1]
    ans = []
    for i in s:
        ans.append(i)
    return ' '.join(ans)

s = input("Enter str to reverse: ")
print(reveSeq(s))




#Task 11.1
def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

n = int(input("n: "))

for i in range(n,2*n):
    if isPrime(i) and isPrime(i+2):
        print(i,i+2)





#Task 11.2
def findMax(arr, n):
    max = -1
    x = 0
    y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max:
                max = arr[i][j]
                x = i
                y = j
    return x,y

arr1 = np.random.randint(100, size=(4, 4))
arr2 = np.random.randint(100, size=(4, 4))
print(arr1)
print(arr2)

max1 = findMax(arr1,4)
max2 = findMax(arr2,4)

arr1[max1[0]][max1[1]],arr2[max2[0]][max2[1]] =  arr2[max2[0]][max2[1]],arr1[max1[0]][max1[1]]
print(arr1)
print(arr2)





#Task 13.1
k = int(input("k: "))
for i in range(2,k):
    for j in range(k):
        if sumOfDigits(i)**j == i:
            print(i,j)
        elif sumOfDigits(i)*j > i:
            break






#Task 13.2
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input("coordinaties x1.x2" ).split())
y1, y2 = map(float,input("coordinaties y1, y2").split())
z1, z2 = map(float,input("coordinaties z1, z2" ).split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
n = 3
res = [tuple(map (float,input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])





    
#Task 14.1
import math
def countDiv(n):
    if n <= 0: return 0 
    if n == 1: return 1

    k = 2 
    for i in range(2, round(math.sqrt(n)) + 1): 
        if n % i == 0:
            k += 1 if i == n // i else 2
    return k

def maxDividersCountAtRange(m , n):
    if m > n : m, n = n, m 

    maxDivs = 0 
    numberWithMaxDivs = [] 
    for i in range(m, n): 
        d = countDiv(i)
        if d > maxDivs: 
            maxDivs = d
            numberWithMaxDivs = [] 
        if d == maxDivs:
            numberWithMaxDivs.append(i) 

    return maxDivs, numberWithMaxDivs

print(maxDividersCountAtRange(20,80))





#Task 14.2
import math
def dis(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
 
coordinates=['x','y','z','t']
arr=[]
print("enter the coordinates of the points:")
for i in range(4):
    b=[]
    print("the coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = dis(arr[i],arr[j])
        if flag or max_dist < dist:
            m1=i
            m2=j
            max_dist = dist 
            flag = False
 
print(f'Maximum distance between points {coordinates[m1]} ?? {coordinates[m2]}')
print(f' dis = {max_dist**0.5:.3f}')






#Task 15.1
def Palindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def count(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if Palindrome(i):
            print(i, end = " ")
if name == "main":
    count(1, 1000)






#Task 15.2
import math
def distance(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d
 
coordinates=['x','y','z','t']
arr=[]
print("coordinates of the points:")
for i in range(4):
    b=[]
    print("coordinates of the points:",coordinates[i])
    for j in range(3):
        b.append(int(input()))
    arr.append(b)
 
flag = True
for i in range(3):
    for j in range(i+1, 4):
        dist = distance(arr[i],arr[j])
        if flag or min_dist > dist:
            m1=i
            m2=j
            min_dist = dist 
            flag = False
 
print(f'Min distance between points {coordinates[m1]} ?? {coordinates[m2]}')
print(f' distance = {min_dist**0.5:.3f}')

    

