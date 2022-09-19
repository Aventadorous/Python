#Task1
Words = input("Введите текст:")
Var = 0
Words = Words.split()
for words in Words:
if words[0] == "е" or words[0] == "Е":
    Var += 1
print(Var)

#Task2
import re
Words2 = input("Enter the text:")
print('{}, replaces: {}'.format(re.sub(r':', '%', Words2), Words2.count(':')))

#Task3
Words3 = input("Enter the text:")
print('{} deleted: {}'.format(re.sub(r'.', ' ', Words3), Words3.count('.')))

#Task4
Words4 = input("Enter the text:")
print('text:{}, replaced: {}'.format(re.sub(r'a', 'o', Words4), Words4.count('a')))
result = len(Words4.split())
print("Words number:", str(result))

#Task5
Words5 = input("Enter the text:")
print(Words5.lower())

#Task6
Words6 = input("Enter the text:")
print('Text:{} deleted: {}'.format(re.sub(r'a', ' ', Words6), Words6.count('a')))

#Task7
Words7 = input("Enter the text:")
s1 = Words7[:len(Words7)//2]
s2 = Words7[len(Words7)//2:]
print('Text:{}'.format(re.sub(r'n', '*', s1))+s2)

#Task8
Words8 = input("Enter the text:")
s8 = str.partition(Words8, '.' )
print(s8[0])
answ8 = s8[0]
result8 = len(answ8.split())
print("Words number:", str(result8))

#Task9
Words9 = input("Enter the text:")
SubWord = input("Enter the word:")
count = Words9.count(SubWord)
print("The count is:", count)

#Task10
Words10 = input("Enter the text:")
print(Words10.title())


#Task12
Words12 = input("Enter the text:")
result12 = len(Words12.split())
print("Words number:", str(result12))
var12 = 0
while var12 != result12:
    message = Words12.split()
    if(message[var12].endswith('I') or message[var12].endswith('i')):
        print(message[var12])
    var12+=1



#Task13
Words13 = input("Enter the text:")
s13 = str.partition(Words13, '(' )
temp13 = str.partition(s13[2], ')')
print(str(temp13[0]))

#Task14
Words14 = input("Enter the text:")
result14 = len(Words14.split())
var14 = 0
while var14 != result14:
    message14 = Words14.split()
    if(message14[var14].startswith('a') and message14[var14].endswith('i')):
        print(message14[var14])
    var14+=1



#Task15
Words15 = input("Enter the text:")
count = Words15.count('t')
print("The count is:", count)


