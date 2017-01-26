class Animal(object):
    population = 0

    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
        Animal.population += 1

    # Copy your sleep function here and modify it to work as a method
    def sleep(self):
        print "%s sleeps for 8 hours" % (self.name)

    # Copy your eat function here and modify it to work as a method
    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if food == self.favoriteFood:
            print "YUM! %s wants more %s" %(self.name, food)

    @classmethod
    def populationCount(cls):
        return cls.population


# Implement the Tiger class here as a subclass of Animal
# Hint: Implement the initializer method only
class Tiger(Animal):
    def __init__(self, name):
        super(Tiger, self).__init__(name, "meat")


# Implement the Bear class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Bear(Animal):
    def __init__(self, name):
        super(Bear, self).__init__(name, "fish")

    def sleep(self):
        print "%s hibernates for 4 months" % (self.name)

# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        super(Unicorn, self).__init__(name, "marshmallows")

    def sleep(self):
        print "%s sleeps in a cloud" % (self.name)


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        super(Giraffe, self).__init__(name, "leaves")

    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if food == self.favoriteFood:
            print "YUM! %s wants more %s" %(self.name, food)
        else:
            print "YUCK! %s spits out %s" % (self.name, food)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        super(Bee, self).__init__(name, "pollen")

    def sleep(self):
        print "%s never sleeps" % (self.name)

    def eat(self, food):
        print "%s eats %s" % (self.name, food)
        if food == self.favoriteFood:
            print "YUM! %s wants more %s" %(self.name, food)
        else:
            print "YUCK! %s spits out %s" % (self.name, food)


# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print "%s is feeding %s to %d of %d total animals" % (self.name, food, len(animals), Animal.populationCount())
        for index in range(len(animals)):
            animals[index].eat(food)
            animals[index].sleep()
