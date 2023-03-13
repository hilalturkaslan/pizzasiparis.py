import datetime
#datetime is imported to use time
import csv
#csv file imported to create table
import pandas as pd
#Pandas is imported to display the csv file as a table


kullanici = []

#csv file
orderss = pd.read_csv("orders_database.csv",delimiter=";")

print(orderss.head(10))


#pizza types are defined in the pizza class
class pizzalar():
    def __init__(self,klasik,margarita,türkpizza,sadepizza):
        super().__init__()
    
    def __init__(self,fiyat,aciklama):
        self.__fiyat = fiyat
        self.__aciklama = aciklama
        print('{} mevcut pizza türleri :'.format(self.pizzalar)
            
            
     
    class klasik():
        def __init__(self,fiyat,aciklama):
            self.fiyat=fiyat
            self.aciklama()
        print('{} mevcut pizza türüdür :'.format(self.klasik)
    
    class margarita():
        def __init__(self,fiyat,aciklama):
            self.fiyat=fiyat
            self.aciklama()
        print('{} mevcut pizza türüdür :'.format(self.margarita)
    
     class türkpizza():
         def __init__(self,fiyat,aciklama):
             self.fiyat=fiyat
             self.aciklama()
         print('{} mevcut pizza türüdür :'.format(self.türkpizza)

    class sadepizza():
        def __init__(self,fiyat,aciklama):
            self.fiyat=fiyat
            self.aciklama()
        print('{} mevcut pizza türüdür :'.format(self.sadepizza)
              
#subclass of pizza class all information of subclass superclass is used    
class pizza(pizzalar):
    pass

#pizza sauces are defined in the sauces class
class soslar():
    def __init__(self,zeytin,mantar,keci_peyniri,et,sogan,misir):
        super().__init__(zeytin,mantar,keci_peyniri,et,sogan,misir)
        
     def __init__(self,fiyat,aciklama):
         self.__fiyat = fiyat
         self.__aciklama = aciklama
         print('{} mevcut pizza soslari :'.format(self.soslar)
    
class zeytin():
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.zeytin)
        
class mantar():
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.mantar)
        
class keci_peyniri():
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.keci_peyniri)
        
class et():
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.et)
        
class sogan():
    def __init__(self,fiyat,aciklama):
       self.fiyat=fiyat
       self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.sogan)
       
class misir():
    def __init__(self,fiyat,aciklama):
        self.fiyat=fiyat
        self.aciklama()
    print('{} mevcut pizza sosu :'.format(self.misir)

#description use get function          
def get_description(cls):
    return aciklama
    
#cost use get function    
def get_cost(cls):
    return fiyat


#the menu is defined       
@classmethod 
class menu():
    def menu(self,pizzalar,soslar):
        self.pizzalar = pizzalar
        self.soslar = soslar

@classmethod
def menu_goruntule(self):
    print('{} mevcut pizza türleri :'.format(self.pizzalar))
    print('{} mevcut pizza sosları :'.format(self.soslar))
    for menu in self.menu:
        print(menu)

#price creation        
def secilen_pizza():
    topFiyat="((pizza+sos))"
    return topFiyat
    print(topFiyat)

#information of interest to the user is defined
def kullanici(self,kullanici_adi,
         kullanici_kimlik,kullanici_kredikart,kredikart_sifre):
    
    self.kullanici_adi = kullanici_adi
    self.kullanici_kimlik = kullanici_kimlik
    self.kullanici_kredikart = kullanici_kredikart
    self.kredikart_sifre = kredikart_sifre

#User information has been added.
def kullanici_ekle(self,kullanici_adi,
         kullanici_kimlik,kullanici_kredikart,kredikart_sifre):
   
    self.kullanici.append(self.kullanici_adi)
    self.kullanici_kimlik.append(self.kullanici_kimlik)
    self.kullanici_kredikart.append(self.kullanici_kredikart)
    self.kredikart_sifre.append(self.kredikart_sifre)
    
#main function created      
def main(self,sos,pizza,kullanici_pizza,kullanici_adi,
         kullanici_kimlik,kullanici_kredikart,kredikart_sifre):
    
    self.kullanici_pizza = kullanici_pizza
    self.kullanici_adi = kullanici_adi
    self.kullanici_kimlik = kullanici_kimlik
    self.kullanici_kredikart = kullanici_kredikart
    self.kredikart_sifre = kredikart_sifre
    
    
    print(main.__dict__)
    

#information shown
    def bilgileri_goster(self):
        print("kullanici_pizza",self.kullanici_pizza,
              "kullanici_adi",self.kullanici_adi,
              "kullanici_kimlik",
              self.kullanici_kimlik,"kullanici_kredikarti",
              self.kullanici_kredikarti,
              "kredikart_sifre",self.kredikart_sifre)




