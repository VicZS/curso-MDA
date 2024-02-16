#------Aqui definimos lo que son las interfaces de FlyBehavior y QuackBehavior------
class FlyBehavior:
    def fly(self):
        pass

class QuackBehavior:
    def quack(self):
        pass

#-----Aqui definimos las clases concretas para FlyBehavior (comportamiento de vuelo)-----
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Vuelo")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("No vuelo")

class FlyWithBalloon(FlyBehavior):
    def fly(self):
        print("Vuelo con globos")

#-----Aqui definimos las clases concretas para QuackBehavior (sonido que hacen)-----
class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class Squeak(QuackBehavior):
    def quack(self):
        print("Squeze")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("No hago ruido")

#-----Creamos la clase abstracta Duck------
class Duck:
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def swim(self):
        print("Splash!!!")

    def display(self):
        pass

    def performfly(self):
        self.fly_behavior.fly()

    def performQuack(self):
        self.quack_behavior.quack()
    
    def showDuck(self):
        print("𓅬\n")

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

#-----Creacion de las clases concretas de los patos-----

#Pato de verdad
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("Soy un Mallard Duck")
    

#Pato de verdad
class RedheadDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings(), Quack())

    def display(self):
        print("Soy un Redhead Duck")

#Pato de goma
class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Squeak())

    def display(self):
        print("Soy un Rubber Duck")

#Pato señuelo
class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithBalloon(), MuteQuack())

    def display(self):
        print("Soy un Decoy Duck")


#-----Main-----
if __name__ == "__main__":

    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()

    mallard_duck.display()
    mallard_duck.performfly()
    mallard_duck.performQuack()
    mallard_duck.showDuck()

    redhead_duck.display()
    redhead_duck.performfly()
    redhead_duck.performQuack()
    redhead_duck.showDuck()

    rubber_duck.display()
    rubber_duck.performfly()
    rubber_duck.performQuack()
    rubber_duck.showDuck()

    decoy_duck.display()
    decoy_duck.performfly()
    decoy_duck.performQuack()
    decoy_duck.showDuck()

    # Menú 
    print("--- Menú Patos ---")
    print("1. Cambiar vuelo")
    print("2. Cambiar sonido")
    print("3. Salir")
    choice = int(input("Ingrese el número de la opción deseada: "))

    if choice == 1:
        print("\nSeleccione el pato para cambiar el vuelo:")
        print("1. Mallard Duck")
        print("2. Redhead Duck")
        print("3. Rubber Duck")
        print("4. Decoy Duck")

        duck_choice = int(input("Ingrese el número del pato: "))
        selected_duck = [mallard_duck, redhead_duck, rubber_duck, decoy_duck][duck_choice - 1]

        print("\nSeleccione el vuelo al que desea cambiar:")
        print("1. Vuelo")
        print("2. No vuelo")
        print("3. Vuelo con globos")
        fly_choice = int(input("Ingrese el número de la opcion: "))
        selected_fly = [FlyWithWings(), FlyNoWay(), FlyWithBalloon()][fly_choice - 1]

        selected_duck.set_fly_behavior(selected_fly)
        print("\n------------------\n")

        mallard_duck.display()
        mallard_duck.performfly()
        mallard_duck.performQuack()
        mallard_duck.showDuck()

        redhead_duck.display()
        redhead_duck.performfly()
        redhead_duck.performQuack()
        redhead_duck.showDuck()

        rubber_duck.display()
        rubber_duck.performfly()
        rubber_duck.performQuack()
        rubber_duck.showDuck()

        decoy_duck.display()
        decoy_duck.performfly()
        decoy_duck.performQuack()
        decoy_duck.showDuck()        
        
    elif choice == 2:
        print("\nSeleccione el pato para cambiar el sonido:")
        print("1. Mallard Duck")
        print("2. Redhead Duck")
        print("3. Rubber Duck")
        print("4. Decoy Duck")

        duck_choice = int(input("Ingrese el número del pato: "))
        selected_duck = [mallard_duck, redhead_duck, rubber_duck, decoy_duck][duck_choice - 1]

        print("\nSeleccione el sonido al que desea cambiar:")
        print("1. Quack")
        print("2. Squeze")
        print("3. No hago ruido")
        quack_choice = int(input("Ingrese el número de la opcion: "))
        selected_quack = [Quack(), Squeak(), MuteQuack()][quack_choice - 1]

        selected_duck.set_quack_behavior(selected_quack)

        print("\n------------------\n")

        mallard_duck.display()
        mallard_duck.performfly()
        mallard_duck.performQuack()
        mallard_duck.showDuck()

        redhead_duck.display()
        redhead_duck.performfly()
        redhead_duck.performQuack()
        redhead_duck.showDuck()

        rubber_duck.display()
        rubber_duck.performfly()
        rubber_duck.performQuack()
        rubber_duck.showDuck()

        decoy_duck.display()
        decoy_duck.performfly()
        decoy_duck.performQuack()
        decoy_duck.showDuck()
    
    elif choice !=3:
        selected_duck = None