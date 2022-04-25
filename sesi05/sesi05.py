#Ini Function
def nama_fungsi(paremeter):
    pass


#Ini class
# class Dog:
#     pass


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):  #constructor
        #instance attribute
        self.name = name
        self.age = age

    def description(self):  #instance method
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self, sound='Yap'):
        # return f"{self.name} says {sound}"
        return super().speak(sound)


class Bulldog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def speak(self, sound='Woof'):
        # return f"{self.name} says {sound}"
        return super().speak(sound)


dog1 = Dachshund('miles', 2)
dog2 = Bulldog('broni', 1, 30)

print(dog1.name)
print(dog2.description())

print(dog1.speak())
print(dog2.speak())

dogs = [Dog('lily', 2), Dog('dogo', 3), Bulldog('blek', 4, 26)]
for i in dogs:
    # print(i.__dict__)
    #print(vars(i))
    # for a in i.__dict__:
    #     print(getattr(i, f"{a}"))
    #print(a)
    for a in vars(i):
        print(f'{a} = {getattr(i, f"{a}")}')