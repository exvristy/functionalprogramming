from abc import ABC, abstractmethod

class CoffeeShop:
  def _init_(self):
    self.americano = False
    self.latte = False
    self.toppings = []
    self.primary = []
  
  def _str_(self):
    string = ""
    if self.americano:
      string += "Iced Americano \n"
    if self.latte:
      string += "Vanilla Latte \n"
    if self.primary:
      string += "ingredients :\n"
    for item in self.primary:
      string += "- " + str(item) + "\n"
    if self.toppings:
      string += "\nToppings added :\n"
    for item in self.toppings:
      string += "- " + str(item) + "\n"
    return string
  
class espresso:
  def _str_(self):
    return "Espresso"

class water:
  def _str_(self):
    return "Water"

class milk:
  def _str_(self):
    return "Milk"

class simplesyrup:
  def _str_(self):
    return "Simple Syrup"

class vanilla:
  def _str_(self):
    return "Vanilla Syrup"

class ice:
  def _str_(self):
    return "Ice"

class CoffeeMaker(ABC):
  @abstractmethod
  def reset(self):
    pass
  
  @abstractmethod
  def coffee_maker(self):
    pass

class iced_americano(CoffeeMaker):
  def _init_(self):
    self.coffee = CoffeeShop()
  def reset(self):
    self.coffee = CoffeeShop()
  def get_product(self):
    return self.coffee
  def coffee_maker(self):
     self.coffee.americano = True
     self.coffee.primary.append (espresso())
     self.coffee.primary.append (water())
     self.coffee.primary.append (ice())
     self.coffee.toppings.append (simplesyrup())

class vanilla_latte(CoffeeMaker):
  def _init_(self):
    self.coffee = CoffeeShop()
  def reset(self):
    self.coffee = CoffeeShop()
  def get_product(self):
    return self.coffee
  def coffee_maker(self):
     self.coffee.latte = True
     self.coffee.primary.append (espresso())
     self.coffee.primary.append (milk())
     self.coffee.primary.append (ice())
     self.coffee.toppings.append (vanilla())

barista = iced_americano()
barista.coffee_maker()
print(barista.get_product())

barista = vanilla_latte()
barista.coffee_maker()
print(barista.get_product())
