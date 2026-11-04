class Animal:
    def __init__(self, name: str):
        self._name = name

    @property
    def eat(self):
        pass

    @property
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def make_sound(self):
        return (f"{self._name} roars loudly!")

    @property
    def eat(self):
        return (f"{self._name} eats fresh meat.")
    
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def make_sound(self):
        return (f"{self._name} trumpets!")
    
    @property
    def eat(self):
        return (f"{self._name} eats grass and fruits.")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    @property
    def make_sound(self):
        return (f"{self._name} chatters!")
  
    @property
    def eat(self):
        return (f"{self._name} eats bananas.")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound)
print(lion.eat)
print("-------")

print(elephant.make_sound)
print(elephant.eat)
print("-------")

print(monkey.make_sound)
print(monkey.eat)
print("-------")
