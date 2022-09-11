#Task1
Name = input("Your last name, first name?")
Age = int(input("How old are you?"))
Phone = input("Your phone number?")

print("Your name is", Name)
print("Your age", Age)
print("Your phone number", Phone)
print(" ")
print(" ")

#Task2
import math
Shape = int(input("1)Circle.   2)Rectangle.   3)Triangle."))
Area = 0
if Shape == 1:
    Radius = float(input("Input the radius of circle"))
    print("Area equal to", math.pi*(Radius**2))
elif Shape == 2:
    Length = float(input("Input the length of Rectangle"))
    Base = float(input("Input the base of Rectangle"))
    print("Area equal to", Length * Base)
elif Shape == 3:
    Height = float(input("Input the height of Triangle"))
    BaseTri = float(input("Input the base of Triangle"))
    print("Area equal to", (Height * BaseTri) / 2)
else:
    print("Bruh, write numbers what I gived for you :/")

print(" ")
print(" ")


#Task3
Number = float(input("Enter the number:"))
Number1 = (Number*100 - (Number*100 % 100))/ 100
Number2 = (Number - Number1)*100
Number3 = (Number2 + Number1/100)
print('%f' %Number3)
print(" ")
print(" ")

#Task4
A = float(input("Enter the number:"))
Y = (A**2)/3 + ((A**2)+4)/6 + (math.sqrt(A**2+4))/4 + math.sqrt((A**2+4)**3)/4
print(Y)
print(" ")
print(" ")

#Task5
PlanNum = float(input("Enter the planned number:"))
Answ = ((PlanNum*5)+8)/2
print(Answ)
print(" ")
print(" ")

#Task2.1
FirstNum = float(input("First number:"))
Operation = int(input("Operation:1)'+'   2)'-'   3)'*'   4)'/' "))
SecondNum = float(input("Second number:"))
if Operation == 1:
    print(FirstNum + SecondNum)
elif Operation == 2:
    print(FirstNum - SecondNum)
elif Operation == 3:
    print(FirstNum * SecondNum)
elif Operation == 4:
    if SecondNum == 0:
        print("Never number divided by zero :3")
    else:
        print(FirstNum / SecondNum)
else:
    print("Bruh, please choose only 4 numbers what i was gived for you :/")

    print(" ")
    print(" ")


#Task2.3
Num = 14
if(Num>10 and Num!=12 and Num<=15 or Num==18):
    print("True")
    print(" ")
    print(" ")


#Task2.4
Temp = 33
while Temp != 67:
    Temp += 1
    if Temp % 2 == 0:
      print(Temp)


print(" ")
print(" ")

#Task2.5
Srevnenie1 = 10
Srevnenie2 = 10
while Srevnenie1!=Srevnenie2:
    print("Nothing")
while True:
    if Srevnenie1==Srevnenie2:
        print("First interation")
        break


    print(" ")
print(" ")

    
#Task2.6.1
var = 0
while var != 100:
   var += 1
   if var < 50 or var >= 100:
     print(var)


print(" ")
print(" ")


#Task2.6.2
var2 = 100
x = 0
for i in range(var2):
    x += 1
    if x < 50 or x >= 100:
      print(x)
    
    


#Task2.7
def printing(letter,number):
    print(letter * number)
word = str(input("Enter the word "))
number = int(input("Enter the number "))
word = tuple(word)
for letters in word:
    printing(letters , number)
      

      
    
    
              
