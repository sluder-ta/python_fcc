## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name


## Perosn is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? something to do with inheritance?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a Object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a Pet(satan is-a Cat)
mary.pet = satan

## Frank is-a Employee, Frank has-a Salary
frank = Employee("Frank", 120000)

## Frank is-a Employee, is-a Person, Frank has-a Pet(rover is-a Dog)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Fish
crouse = Salmon()

## harry is-a Fish
harry = Halibut()