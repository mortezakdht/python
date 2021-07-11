# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:13:55 2020

@author: Morteza Kazem Dehdashti
"""
from Cart import Attaque,Born,Parade,Botte,Pioche
class Joueur:
    """
    Init : Initialiser le joueur 
    """
    def __init__(self,carts,name):
        self.name=name
        self.mycarts=carts
        self.score=0
        self.memoCarts=[]
        self.memoCarts.append("FeuRouge")
        self.lastcartinMemo="FeuRouge"
        self.safeContreAccidane=False
        self.safeContreCrevaison=False
        self.safeContrePanneE=False
        self.safeContreFeuVertLimit=False
    """
    playTurn : Choisir un cart et un adversair 
    """    
    def playTurn(self,piochCart):
        self.mycarts.append(piochCart)
        for j in range (len(self.mycarts)):
            print(j,":",self.mycarts[j])
        value=int(input("please enter your favorite cart by its number between 0-6 : "),10)
        place=int(input("please enter the place(throw out -1):"),10)
        choosedCart= self.mycarts[value]
        typecart=self.getCartType(choosedCart) #get type of cart
        if self.checkvalidite(value,choosedCart,place,typecart) :
            return choosedCart,place,typecart
        else:
            print(" Error: your choosen cart or place is not ok!!")
            self.playTurn(piochCart)
        return self.sc,place
    """
    updateMemo : Mise a jour la Memo de joueur 
    """   
    def updateMemo(self,plyedcart):
        self.memoCarts.append(plyedcart)
        self.lastcartinMemo=plyedcart
        #self.mycarts.remove(plyedcart)
    """
    checkvalidite : Verifier les chiffre saisir par utilisateur soit correct 
    """        
    def checkvalidite(self,numvalue,value,memocible,typecart):  
        lastCartMemo =self.memoCarts[-1]
        if numvalue<0 or numvalue>7 or type(numvalue)!=int or type(memocible)!=int:
           return False
        return True
    """
    getCartType : Trouver le type de cart
    """
    def getCartType(self,chcart):
        boCart=Born()
        atCart=Attaque()
        botCart=Botte()
        parCart=Parade()
        #print(type(chcart))
        if boCart.checkexistance(chcart) :
            return 'Born'
        if atCart.checkexistance(chcart):
            return 'Attaque'
        if botCart.checkexistance(chcart):
            return 'Botte'
        if parCart.checkexistance(chcart):
            return 'Parade'
        else :
            return 'NotValide'
        
    #def updatesafecart(self,km):
     #   return 1
    """
    updatescore : mise a jour le score 
    """
    def updatescore(self,newscore):
         self.score=self.score+newscore
         return self.score
    """
    updatemycarts : mise a jour les carts dans la main de joueur 
    """ 
    def updatemycarts(self,plyedcart):
        print("delete cart =======",plyedcart)
        self.mycarts.remove(plyedcart)