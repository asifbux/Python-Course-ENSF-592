class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, newName=''):
        self.name = newName

    def get_age(self):
        return self.age

    def set_age(self, newAge):
        self.age = newAge

    def __str__(self):
        return 'Animal: ' + str(self.get_name()) + ' ' + str(self.get_age())


dog = Animal(3)
print(dog)

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
         return "Cat: " + str(self.get_name()) + ' ' + str(self.get_age())
        #"Cat: " + str(Animal.get_name(self)) + ' ' + str(Animal.get_age(self))

jelly = Cat(1)
jelly.set_name('Neo')
jelly.speak()
print(jelly)

class Rabbit(Animal):
    tag = 0
    def __init__(self, age):
        Animal.__init__(self, age)
        Rabbit.tag += 1
    def speak(self):
        print('meep')
    def __str__(self):
         return "Rabbit: " + str(self.get_name()) + ' ' + str(self.get_age()) + ' Tag: ' + str(Rabbit.tag)

peter = Rabbit(3)
peter.set_name('Peter')
print(peter)

atom = Rabbit(5)
atom.set_name('atom')
print(atom)

''' to access Animals Str'''
print(Animal.__str__(jelly))

print('Person Example-------------')

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name) # dont forget to pass self here
        self.friends = []
    def get_friends(self):
        return self.friends
    def set_friends(self, fname):
        return self.friends.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, ' is ', diff, ' years older than ', other.name)
        else:
            print(self.name, ' is ', -diff, ' years younger than ', other.name)
    def __str__(self):
        return 'Person: ' + str(self.name) + ' ' + str(self.age)

derek = Person('Derek', 35)
john = Person('John', 55)
derek.speak()
derek.age_diff(john)
# or
Person.age_diff(john, derek)
# this would not work age_diff(derek, john)
print(john)
