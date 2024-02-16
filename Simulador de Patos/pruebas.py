"""class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)

# Crear una instancia de la clase
objeto = MiClase("Ejemplo")

# Llamar al método saludar
objeto.saludar()"""

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

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()
    
    def showDuck(self):
        print("𓅬")

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



if __name__ == "__main__":
    # ... Código existente ...

    # Crear instancias de patos
    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()

    # Mostrar información inicial
    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    mallard_duck.showDuck()

    # Menú para cambiar comportamientos
    print("\n=== Menú para cambiar comportamientos ===")
    print("1. Cambiar comportamiento de vuelo")
    print("2. Cambiar comportamiento de sonido")
    print("3. Salir")

    choice = int(input("Ingrese el número de la opción deseada: "))

    while choice != 3:
        selected_duck = None

        if choice == 1:
            print("\nSeleccione el pato para cambiar el comportamiento de vuelo:")
            print("1. Mallard Duck")
            print("2. Redhead Duck")
            print("3. Rubber Duck")
            print("4. Decoy Duck")

            duck_choice = int(input("Ingrese el número del pato: "))
            selected_duck = [mallard_duck, redhead_duck, rubber_duck, decoy_duck][duck_choice - 1]

            new_fly_behavior = FlyNoWay()  # Cambiar a un comportamiento diferente si es necesario
            selected_duck.set_fly_behavior(new_fly_behavior)
            print("Comportamiento de vuelo cambiado para el", selected_duck.__class__.__name__)

        elif choice == 2:
            print("\nSeleccione el pato para cambiar el comportamiento de sonido:")
            print("1. Mallard Duck")
            print("2. Redhead Duck")
            print("3. Rubber Duck")
            print("4. Decoy Duck")

            duck_choice = int(input("Ingrese el número del pato: "))
            selected_duck = [mallard_duck, redhead_duck, rubber_duck, decoy_duck][duck_choice - 1]

            new_quack_behavior = MuteQuack()  # Cambiar a un comportamiento diferente si es necesario
            selected_duck.set_quack_behavior(new_quack_behavior)
            print("Comportamiento de sonido cambiado para el", selected_duck.__class__.__name__)

        # Mostrar información después del cambio
        selected_duck.display()
        selected_duck.perform_fly()
        selected_duck.perform_quack()
        selected_duck.showDuck()

        # Mostrar el menú nuevamente
        print("\n=== Menú para cambiar comportamientos ===")
        print("1. Cambiar comportamiento de vuelo")
        print("2. Cambiar comportamiento de sonido")
        print("3. Salir")
        choice = int(input("Ingrese el número de la opción deseada: "))

"""
#-----Main-----
if __name__ == "__main__":

    mallard_duck = MallardDuck()
    redhead_duck = RedheadDuck()
    rubber_duck = RubberDuck()
    decoy_duck = DecoyDuck()

    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()
    mallard_duck.showDuck()

    redhead_duck.display()
    redhead_duck.perform_fly()
    redhead_duck.perform_quack()
    redhead_duck.showDuck()

    rubber_duck.display()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()
    rubber_duck.showDuck()

    decoy_duck.display()
    decoy_duck.perform_fly()
    decoy_duck.perform_quack()
    decoy_duck.showDuck()

    # Menú 
    print("--- Menú Patos ---")
    print("1. Cambiar vuelo del Mallard Duck")
    print("2. Cambiar sonido del Mallard Duck")
    choice = int(input("Ingrese el número de la opción deseada: "))

    if choice == 1:
        new_fly_behavior = FlyNoWay()  # Cambiar a un comportamiento diferente si es necesario
        mallard_duck.set_fly_behavior(new_fly_behavior)
        print("Comportamiento de vuelo cambiado.")
    elif choice == 2:
        new_quack_behavior = MuteQuack()  # Cambiar a un comportamiento diferente si es necesario
        mallard_duck.set_quack_behavior(new_quack_behavior)
        print("Comportamiento de sonido cambiado.")

"""
