class Animal: #defines the parent class Animal
    def __init__(self, name: str): #init constructor initializes the animal object
        self._name = name #stores the animal's name as an attribute

    @property #allows eat to be accessed like an attribute
    def eat(self): #defines the eat method
        pass #serves as "placeholder" for the child classes because each animal eats different things and makes different sounds

    @property #allows make_sound to be accessed like an attribute
    def make_sound(self): #defines the make_sound method
        pass #serves as "placeholder" for the child classes because each animal eats different things and makes different sounds

class Lion(Animal): #creates lion child class that inherits from Animal parent class
    def __init__(self, name): #init constructor initializes the lion object
        super().__init__(name) #calls the parent class constructor to initialize the name property

    @property #allows make_sound to be accessed like an attribute
    def make_sound(self): #overrides the make_sound method from the parent class
        return (f"{self._name} roars loudly!") #returns the lion's unique sound and name

    @property #allows eat to be accessed like an attribute
    def eat(self): #overrides the eat method from the parent class
        return (f"{self._name} eats fresh meat.") #returns the what the lion eats and its name
    
class Elephant(Animal): #creates elephant child class that inherits from Animal parent class
    def __init__(self, name): #init constructor initializes the elephant object
        super().__init__(name) #calls the parent class constructor to initialize the name property

    @property #allows make_sound to be accessed like an attribute
    def make_sound(self): #overrides the make_sound method from the parent class
        return (f"{self._name} trumpets!") #returns the elephant's unique sound and name
    
    @property #allows eat to be accessed like an attribute
    def eat(self): #overrides the eat method from the parent class
        return (f"{self._name} eats grass and fruits.") #returns the what the elephant eats and its name

class Monkey(Animal): #creates monkey child class that inherits from Animal parent class
    def __init__(self, name): #init constructor initializes the monkey object
        super().__init__(name) #calls the parent class constructor to initialize the name property

    @property #allows make_sound to be accessed like an attribute
    def make_sound(self): #overrides the make_sound method from the parent class
        return (f"{self._name} chatters!") #returns the monkey's unique sound and name
  
    @property #allows eat to be accessed like an attribute
    def eat(self): #overrides the eat method from the parent class
        return (f"{self._name} eats bananas.") #returns the what the monkey eats and its name

lion = Lion("Simba") #creates a Lion object with the name Simba
elephant = Elephant("Dumbo") #creates an Elephant object with the name Dumbo
monkey = Monkey("George") #creates a Monkey object with the name George

print(lion.make_sound) #prints the lion's sound
print(lion.eat) #prints what the lion eats
print("-------") #prints a dividor

print(elephant.make_sound) #prints the elephant's sound
print(elephant.eat) #prints what the elephant eats
print("-------") #prints a dividor

print(monkey.make_sound) #prints the monkey's sound
print(monkey.eat) #prints what the monkey eats
print("-------") #prints a dividor