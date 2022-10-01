class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if(self.num2 != 0 ):
            return self.num1 / self.num2
        else:
            return "Dude, you can't divide number to zero :/"



calculator = Calculator(10, 5)


print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.divide())


print("   ")
print("   ")

number1 = float(input("Enter the any number: "))
number2 = float(input("Enter the second any number: "))

calculator1 = Calculator(number1, number2)

print("   ")
print("   ")

print(calculator1.add())
print(calculator1.subtract())
print(calculator1.multiply())
print(calculator1.divide())
