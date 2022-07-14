# class TV:
#     '''Thid class defines Tv type'''
#     def __init__(self,brand,model,cost):
#         self.brand = brand
#         self.model = model
#         self.cost = cost
#     def display(self):
#         print(self.brand)
#         print(self.model)
#         print(self.cost)
# mi = TV('MI','2016',12000)
# setattr(mi,'model','2018')
# mi.display()
# print(mi.__doc__)
# print(mi.__dict__)
# print(mi.__module__)

# class Ex:
#     count = 0
#     def __init__(self):
#         self.count = Ex.count + 1
#     def display(self):
#         return self.count
# ex1 = Ex()
# print(ex1.display())
# ex2 = Ex()
# print(ex2.display())
# ex3 = Ex()
# print(ex3.display())
# class Hero:
#     def __init__(self,name,hp,atk,defen):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.defen = defen
#     def attack(self,enemy):
#         damage = max(0,self.atk-enemy.defen)
#         enemy.defend(damage)
# class Enemy(object):
#     def __init__(self,hp,atk,defen,is_aggressive):
#         self.hp = hp
#         self.atk = atk
#         self.defen = defen
#         self.is_aggressive = is_aggressive
# class Animal(Enemy):
#     def __init__(self,hp,atk,defen):
#         Enemy.__init__(self,hp,atk,defen,False)
#     def defend(self,damage):
#         if self.hp < 10:
#             damage *= 1.15
#         if self.hp > 25:
#             damage *= 0.8
#         self.hp -= damage
#         print(self.hp)
# class Zombie(Enemy):
#     def __init__(self,hp,atk,defen):
#         Enemy.__init__(self,hp,atk,defen,False)
#     def defend(self,damage):
#         if self.hp > 5:
#             damage *= 0.7
#         self.hp -= damage
#         print(self.hp)
#
# hero1 = Hero("Rick", 30, 20, 40)
# animal1 = Animal(10,25,30)
# hero1.attack(animal1)

# class TV(object):
#     def __init__(self,color,tv_type,size,cost):
#         self.type = tv_type
#         self.color = color
#         self.size = size
#         self.base_cost = cost
#         self.__discount = 0
#
#     def set_discount(self,discount):
#         self.__discount = discount
#
#     def tv_price(self):
#         self.price = self.base_cost-((self.base_cost//100)*(self.__discount*100))
#         return self.price
#     def display(self):
#         return "Color:{} Type:{} Size:{} Price:{}".format(self.color,self.type,self.size,self.tv_price())
# class Cost:
#     def find_cost(self,brand,size,tv_type):
#         self.brand = brand
#         self.size = size
#         self.tv_type = tv_type
#         if self.brand == 'MI':
#             if self.size == 16:
#                 if self.tv_type == 'LCD':
#                     return 15000
#                 else:
#                     return 30000
#             else:
#                 if self.tv_type == 'LCD':
#                     return 17000
#                 else:
#                     return 34000
#         elif self.brand == "SAMSUNG":
#             if self.size == 16:
#                 if self.tv_type == 'LCD':
#                     return 17000
#                 else:
#                     return 18000
#             else:
#                 if self.tv_type == 'LCD':
#                     return 19000
#                 else:
#                     return 38000
# class Brand(TV,Cost):
#     def __init__(self,brand,color,tv_type,size):
#         self.brand = brand
#         self.cost = Cost.find_cost(self,brand,size,tv_type)
#         TV.__init__(self,color,tv_type,size,self.cost)
#
#     def display(self):
#         return "Brand:{} Color:{} Type:{} Size:{} Price:{}".format(self.brand,self.color,self.type,self.size,self.tv_price())
#
# if __name__ == '__main__':
#     mi = Brand('MI','Black','LCD',32)
#     mi.set_discount(0.09)
#     mi.tv_price()
#     print(mi.display())
#
#     samsung = Brand('SAMSUNG','Silver','LED',16)
#     samsung.set_discount(0.04)
#     print(samsung.display())

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def name(self):
        return self.name()
    def price(self):
        return self.price()
class ShoppingCart:
    def __init__(self):
        self.l = []
    def total(self):
        self.count = 0
        for i in self.l:
            self.count += i.price
        return self.count

    def __len__(self):
        return len(self.l)

    def add(self,item):
        self.item = item
        self.l.append(self.item)

cart = ShoppingCart()
phone = Item('phone',1000)
charger = Item('Charger',500)
print(cart.total())
print(len(cart))
cart.add(phone)
cart.add(charger)
print(cart.total())
print(len(cart))

