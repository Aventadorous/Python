#Task1
n = int(input("Enter the number of array"))
a = [ int(input()) for i in range(n)]
a.reverse()
print(a)

#Task2
x2 = [12, 35, 9, 56, 24]
print("Current list: ", x2)
def change(x2):
    size = len(x2)
    temp = x2[0]
    x2[0] = x2[size - 1]
    x2[size - 1] = temp
     
    return x2
     
print("New list:     ",change(x2))

#Task3
def to_list(*arg):
    print ("List of elements: ", arg)


a=[1,2,3,4]
bb=['fsfdsf', 'fffff', 'aaa']
to_list(1, a, bb)


#Task4
list1 = [5, 11, 54, 8, 102, 67, 43]
 
list1.sort()
max_el=list1[-1]
n=len(list1)
value=max_el/n
print(value)

#Task5
list = [1,-5,3,-9,25,10]
def absolute_value(num):
    return abs(num)
list.sort(key = absolute_value)
list.reverse()

print("List in descending order: ", list)

#Task6
