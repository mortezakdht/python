# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:14:11 2020

@author: Morteza Kazem Dehdashti
"""


from Cart import Attaque,Born,Parade,Botte,Pioche
from Joueur import Joueur

class Jeu :
    """
    Init : Creer les joueur 
    """
    def __init__(self, names) :
       # self.joueurs_name=names
        self.joueurs=[]
        self.gng=0
        self.att=Attaque()
        self.scoremax =0
        self.userGng =""
        for i in range(len(names)) :
            my_cards = ['FeuVert']
            for j in range (5):
                p=Pioche()
                my_cards.append(p.piocher())
           # print(self.joueurs_name[i] , my_cards) 
            self.joueurs.append(Joueur(my_cards,names[i]))
    """
    ShowAllUsers : Afficher tous les joueur avec ses scores 
    """        
    def ShowAllUsers(self) :
        for i in range(len(self.joueurs)):
            print("joueur",self.joueurs[i].name ,"(",self.joueurs[i].score,"km ,", 
                  self.joueurs[i].lastcartinMemo,")")
    """
    DemarerLeJeu : Cette method est pour commencer le jeu et controller les tour de joueur 
    """
    def demarerLeJeu(self) :       
        print("+-------------------------+")
        print("|-------jeu commence------|")
        print("+-------------------------+")
        i=0
        while self.gng<1000 :
           print("+++++++++++++++ score gangent :", self.scoremax)  
           # show joueurs carts
           p=Pioche()
           c=p.piocher()
           self.jeuTour(i,c)
           print("=========>Next Tour: ")
           i+=1
           if i == len(self.joueurs):
              i=0          
        return self.userGng

    """
       jeuTour : Cette method analyse le jeu de joueur en cas de validite donne le tour au prochain joueur
    """ 
    def jeuTour (self, indexUser,cartpiocher):
        sc=0
        ls=0
        print("+======Memos of others======+")
        for k in range(len(self.joueurs)):
            if k == indexUser :
               print( indexUser ," ***IS YOUR TURN *** :",self.joueurs[k].name, "and Your MEMO = " +self.joueurs[k].lastcartinMemo)
            if k !=indexUser :
               print(k," : adversaire ",self.joueurs[k].name, "has (",self.joueurs[k].score,"km," ,self.joueurs[k].lastcartinMemo,")") 

            print("Volant:", self.joueurs[k].safeContreAccidane, "Increvable:", self.joueurs[k].safeContreCrevaison, "Camion_Critere:", self.joueurs[k].safeContrePanneE, "Periorite:", self.joueurs[k].safeContreFeuVertLimit) 
            print("")
        print("+============================+") 
        print(self.joueurs[indexUser].name, "score: ",self.joueurs[indexUser].score)
        print("|=>")
        
        choosedCart,place,typecart=self.joueurs[indexUser].playTurn(cartpiocher)
        if self.validate(place,choosedCart,typecart,indexUser) :
            cc=choosedCart
            self.joueurs[indexUser].mycarts.remove(choosedCart)  
            if typecart == "Born":
               ls=self.calculateScore(cc,typecart,indexUser) 
               sc=self.getscoregng(ls,indexUser)
               self.gng=sc
            if typecart =="Botte":
               #self.joueurs[indexUser].mycarts.remove(choosedCart)4
               print("********************You can play one more time::")
               p=Pioche()
               self.jeuTour(indexUser,p.piocher()) #jeu again
          
        else :
            print("your cart is not validate please jeu again")
            self.joueurs[indexUser].mycarts.remove(cartpiocher)
            self.jeuTour(indexUser,cartpiocher)
    """
      validate : Verifier le cart jouer avec les regles de jeu
      en prennant la cart jouee , le type de cart , l'endroit de cart(quel memo cart)
    """         
    def validate(self,place,cart,typecart,user):
        memocor=self.joueurs[place].lastcartinMemo
        memotype= False
        if memocor=="AccidanteDeLaRoue" or memocor=="PanneEssance"  or memocor== "Crevaison" or memocor=="LimitationDeVitess" or memocor=="FeuRouge":
            memotype=True #type of memocart
        if type(place)!=int or place>len(self.joueurs):
            print("you should enter valid place")
            return False
        else:     
            print("====>",typecart,",",memocor , "," , memotype)
            #################MYSELF
            if place == user:
                print("play en myselffff")
                if typecart == "Attaque" :
                    print("your cant play attaque on your self")
                    return False
                #if cart=="FeuVert" :
                    #self.joueurs[user].updateMemo(cart)
                    #return True
                    #or(typecart=="Born" and len(self.joueurs[user].memoCarts)>0)
                if (typecart =="Born" and memocor =="FeuVert" )or (typecart=="Born" and memocor == "periorite") or(typecart=="Born" and len(self.joueurs[user].memoCarts)>0):                    
                   # n=Born()
                   # self.joueurs[user].updatesafecart(n.returnscore(cart)) 
                    if memotype == False :  
                        self.joueurs[user].updateMemo(cart)
                        return True
                    else :
                        print("You Should first remove your attaque")
                        return False
                if typecart =="Parade" and memotype ==True : #if lastmemo cart type =attaque
                    if cart == "Reparation" and memocor == "Crevaison" :
                        self.joueurs[user].updateMemo(cart)
                        return True
                    if cart == "Essance" and memocor == "PanneEssance" :
                        self.joueurs[user].updateMemo(cart)
                        return True
                    if cart == "RoueDuSecour" and memocor == "AccidanteDeLaRoue":
                        self.joueurs[user].updateMemo(cart)
                        return True
                    if cart == "FindeLimitationVitess" and memocor == "LimitationDeVitess":
                        self.joueurs[user].updateMemo(cart)
                        return True 
                    if cart == "FeuVert" and memocor =="FeuRouge" :
                        print("=======feu verttt")
                        self.joueurs[user].updateMemo(cart)
                        return True 
                    else:
                       return False
                if typecart =="Botte" and memotype != "Attaque":
                        self.joueurs[user].updateMemo(cart)
                        if cart == "Volant" :
                            self.joueurs[user].safeContreAccidane = True
                            return True 
                        if cart == "Increvable":
                            self.joueurs[user].safeContreCrevaison = True
                            return True 
                        if cart == "CamionCritere":
                            self.joueurs[user].safeContrePanneE = True
                            return True                             
                        if cart == "periorite" : 
                            self.joueurs[user].safeContreFeuVertLimit = True
                            return True                             
                        return True 
                else :
                    print("Error,you can do such game for your self")
                    return False
            if place == -1 :
                print("you throw out ", cart)
                #self.joueurs[user].mycarts.remove(cart)
                return True
            else:
                print("play on adversaireeee", self.joueurs[place].name)
                if typecart == "Attaque" and (memocor =="FeuVert" or memocor =="periorite" or len(self.joueurs[place].memoCarts)>0):
                    #print("I M HEREEEEEEEEEEEEE")
                    if cart == "AccidanteDeLaRoue" and self.joueurs[place].safeContreAccidane==False :
                        self.joueurs[place].updateMemo(cart)
                        return True
                    if cart == "PanneEssance" and self.joueurs[place].safeContrePanneE==False:
                        print("PanneEssanece")
                        self.joueurs[place].updateMemo(cart)
                        return True
                    if cart == "Crevaison" and self.joueurs[place].safeContreCrevaison==False:
                        print("CREVASION")
                        self.joueurs[place].updateMemo(cart)
                        return True
                    if (cart == "LimitationDeVitess" or cart =="FeuRouge") and self.joueurs[place].safeContreFeuVertLimit==False :
                        print("FEU ROUGE")
                        self.joueurs[place].updateMemo(cart)
                        return True                                                
                    
                if cart =="LimitationDeVitess" and memocor != "FeuVert" and self.joueurs[place].safeContreFeuVertLimit==False :
                    self.joueurs[place].updateMemo(cart)
                    return True
                else:
                    print("Error,you cant play such game for your advairesair")
                    return False
    """
      calculateScore : prends le score de joueur et mets dans la variable de dernier score obtenu
    """                  
    def calculateScore(self,cart,typecart,user):
        b=Born()
        score=b.returnscore(cart)
        #print("====>score: ",score)
        lastscore=self.joueurs[user].updatescore(score)
        print(lastscore)
        return lastscore
    """
      getscoregng :  trouver le score max 
    """  
    def getscoregng(self,ls,user):          
        if self.scoremax<ls :
            self.scoremax=ls
            self.userGng=self.joueurs[user].name
        return self.scoremax   
"""
   class principal : commencer le jeu on prennant le nombre des joueurs et leurs nom , et afficher le gagnant 
  """            
class principal:
    def __init__(self):
        print("+------------------------------------+")
        print("|Binvenue dan le jeu du 1000 bornes! |") 
        print("+------------------------------------+")
        self.jnumb=int(input("combien de joueurs? "),10)
        if self.jnumb>6 :
            print("Max player number is 6")
        else:    
            self.names= list()
            for i in range(self.jnumb):
                n=input("veuillez saisir le nom de joueur =")
                self.names.append(n)
            print("------------------")    
            self.jeu=Jeu(self.names)
            self.jeu.ShowAllUsers()
            gg=self.jeu.demarerLeJeu()
            print("**************************************")
            print("************JEU FINISH****************")
            print("THE Winner is :",gg, "win")
        

p=principal()
          