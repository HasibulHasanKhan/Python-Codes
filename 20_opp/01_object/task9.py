## Polymorphism :

#"Many Forms" 


## olymorphism with Inheritance (Method Overriding)

# When a child class overrides a parent method, it’s polymorphism in action. 

class Bird:
    def speak(self):
        return "Some generic bird sound."
    

class Parrot(Bird):
    def speak(self):
        return "Parront says Squawk!"
    

class Crow(Bird):
    def speak(self):
        return "Crow says Caw!"
    
birds = [Parrot(), Crow()]

for bird in birds:
    print(bird.speak())

## example : 



