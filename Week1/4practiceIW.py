n = float(input("Enter the price of 1kg sweets"))
x = int(input("How many kg do you need?"))
for i in range(x+1):
    print("For", i, 'kg, price is', n*i)
    
