import csv
import datetime
import time
import re

#menu.txt adlı bir dosya oluşturuyoruz.
menu = open("menu.txt","w") 
menu.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: Türk Pizza\n4: Sade Pizza\n* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n* Teşekkür ederiz!")
menu.close()

