class Name:
    def __init__(self, first_name, last_name):
        self.first_name = str.capitalize(first_name)
        self.last_name = str.capitalize(last_name)

    def first_name_is(self):
        return self.first_name

    def last_name_is(self):
        return self.last_name


    def full_name(self):
        full_name = self.first_name + " " +  self.last_name
        return full_name

    def initials(self):
        return  self.first_name[0] + ". " + self.last_name[0] + "."

fName = input("Enter the your first name:")
lName = input("Enter the your last name:")

a1 = Name("john", "SMITH")
print(a1.first_name_is())
print(a1.last_name_is())
print(a1.full_name())
print(a1.initials())

print("   ")
print("   ")

a2 = Name("rASUL", "RAISkanov")
print(a2.first_name_is())
print(a2.last_name_is())
print(a2.full_name())
print(a2.initials())

print("   ")
print("   ")

a3 = Name(fName, lName)
print(a3.first_name_is())
print(a3.last_name_is())
print(a3.full_name())
print(a3.initials())