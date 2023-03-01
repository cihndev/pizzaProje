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

class Pizza:
    def __init__(self):
        pass
    def get_description(self):
        pass
    def get_cost(self):
        pass
    def main(self):
        pass

    class Klasik:
        def __init__(self, fiyat):
            self.fiyat = fiyat
            pass
    class Margherita:
        def __init__(self, fiyat):
            self.fiyat = fiyat
            pass
    class Turk_pizzasi:
        def __init__(self, fiyat):
            self.fiyat = fiyat
            pass
    class Dominos_pizza:
        def __init__(self, fiyat):
            self.fiyat = fiyat
            pass

    
class Sos:
    def __init__(self) -> None:
        pass