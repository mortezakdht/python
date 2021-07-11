# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:13:27 2020

@author: Morteza Kazem Dehdasht

"""
import random
from abc import ABC,ABCMeta, abstractmethod
class Cart (ABC) :
    __metaclass__ = ABCMeta
    @ abstractmethod
    def __init__(self):pass
      #  self.n = 106   
    @ abstractmethod    
    def getCount(self,cart):
        return self.n
    @ abstractmethod 
    def deleteCart(self,cart):pass
    def allcarts():pass 
    
   
   
class Born(Cart):
    def __init__(self):
        self.bornDict={'Escargot=>25KM':10 ,'Canard=>50km':10,'Papillon=>75km':10,'lievre=>100km':12,'Hirondell=>200km':4}
        self.n=super().__init__()
    def checkexistance(self,cart):
        return (cart in self.bornDict)
    def getCount(self,cart):
        return  self.bornDict.get(cart)
    def updateCart(self,cart):
        self.bornDict[cart]-=1
    def deleteCart(self,cart) :
        self.bornDict[cart]-=1
    def allcarts(self):
        return self.bornDict
    def allcartsList(self):
        listAllbornCart=list()
        for key, value in self.bornDict.items():
            for i in range (value):
                listAllbornCart.append(key)
        return listAllbornCart
    def returnscore (self,cart):
        if cart == 'Escargot' or cart=='Escargot=>25KM' :
            return 25
        if cart == 'Canard' or cart =='Canard=>50km':
            return 50
        if cart == 'Papillon' or cart== 'Papillon=>75km':
            return 75
        if cart =='lievre' or cart == 'lievre=>100km':
            return 100
        if cart =='Hirondell' or cart == 'Hirondell=>200km':
            return 200


class Botte(Cart):
    def __init__(self):
        self.botteDict={'Volant':1 ,'CamionCritere':1,'Increvable':1,'periorite':1}
        self.n=super().__init__()
    def checkexistance(self,cart):
        return (cart in self.botteDict)
    def getCount(self,cart):
       return  self.botteDict.get(cart)
    def updateCart(self,cart):
        self.botteDict[cart]-=1
    def deleteCart(self,cart) :
        self.botteDict[cart]-=1
    def allcarts(self):
        return self.botteDict
    def allcartsList(self):
        listAllbotteCart=list()
        for key, value in self.botteDict.items():
            for i in range (value):
                listAllbotteCart.append(key)
        return listAllbotteCart 



class Parade(Cart):
    def __init__(self):
        self.paradeDict={'Reparation':6 ,'Essance':6,'RoueDuSecour':6,'FindeLimitationVitess':6,'FeuVert':14}
        self.n=super().__init__()
    def checkexistance(self,cart):
        return (cart in self.paradeDict)
    def getCount(self,cart):
       return  self.paradeDict.get(cart)
    def updateCart(self,cart):
        self.paradeDict[cart]-=1
    def deleteCart(self,cart) :
        self.paradeDict[cart]-=1
    def allcarts(self):
        return self.paradeDict
    def allcartsList(self):
        listAllParadeCart=list()
        for key, value in self.paradeDict.items():
            for i in range (value):
                listAllParadeCart.append(key)
        return listAllParadeCart 



class Attaque(Cart):        
    def __init__(self):
        self.attaqueDict={'AccidanteDeLaRoue':3 ,'PanneEssance':3,'Crevaison':3,'LimitationDeVitess':4,'FeuRouge':5}
        self.n=super().__init__()
    def checkexistance(self,cart):
        return (cart in self.attaqueDict)
    def getCount(self,cart):
       return  self.attaqueDict.get(cart)
    def updateCart(self,cart):
        self.attaqueDict[cart]-=1
    def deleteCart(self,cart) :
        self.attaqueDict[cart]-=1
    def allcarts(self):
        return self.attaqueDict
    def allcartsList(self):
        listAllAttaqueCart=list()
        for key, value in self.attaqueDict.items():
            for i in range (value):
                listAllAttaqueCart.append(key)
        return listAllAttaqueCart 
    """
    Pioche : Class de pioch pour melanger et choisir une cart par hazard
    """     

class Pioche:
    def __init__(self):
       #getallCarts
        self.a=Attaque()
        aAll=self.a.allcartsList()
        self.p=Parade()
        pAll=self.p.allcartsList()
        self.b=Botte()
        bAll=self.b.allcartsList()
        self.born=Born()
        bornAll=self.born.allcartsList()
        AllCarts=list(aAll)
        AllCarts.extend(pAll)
        AllCarts.extend(bAll)
        AllCarts.extend(bornAll)
      #  print(AllCarts)
        self.carts=AllCarts
    def melange(self):
        random.shuffle(self.carts)
    def piocher(self):
        choicecart=random.choice(self.carts)
        #print("avantdelete")
        if self.a.checkexistance(choicecart):
            #print("attaque")
            self.a.deleteCart(choicecart)
        if self.p.checkexistance(choicecart):
            #print("parade")
            self.p.deleteCart(choicecart)
        if self.b.checkexistance(choicecart):
            #print("botte")
            self.b.deleteCart(choicecart)
        if self.born.checkexistance(choicecart):
            
            self.born.deleteCart(choicecart)  
        return choicecart
        
