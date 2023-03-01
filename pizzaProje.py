import csv
import datetime
import time
import re

#menu.txt adlı bir dosya oluşturuyoruz.
menu = open("menu.txt","w") 
menu.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: Türk Pizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")
menu.close()

menu = open("menu.txt","r")
print(menu.read())
menu.close()

class Pizza: #pizza adında üst sınıf (taban sınıf (base class) / super class) oluşturuyoruz.
    def __init__(self, fiyat, pizza_tabani, sos):
        self.fiyat = fiyat
        self.pizza_tabani = pizza_tabani
        self.sos = sos
    def get_description(self):
        pass
    def get_cost(self):
        pass
    def main(self):
        pass

class Klasik(Pizza): # Parantez içerisine Pizza sınıfının adını yazarak alt sınıf oluşturduk.
    def __init__(self, fiyat):
        self.fiyat = fiyat
        pass
class Margherita(Pizza):
    def __init__(self, fiyat):
        self.fiyat = fiyat
        pass
class Turk_pizzasi(Pizza):
    def __init__(self, fiyat):
        self.fiyat = fiyat
        pass
class Dominos_pizza(Pizza):
    def __init__(self, fiyat):
        self.fiyat = fiyat
        pass
class decorator:
    def __init__(self):
        pass
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(decorator):
    def __init__(self):
        pass

class Mantar(decorator):
    def __init__(self):
        pass

class Keci_peyniri(decorator):
    def __init__(self):
        pass

class Et(decorator):
    def __init__(self):
        pass

class Sogan(decorator):
    def __init__(self):
        pass

class Misir(decorator):
    def __init__(self):
        pass