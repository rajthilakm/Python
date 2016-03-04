# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:57:38 2016

@author: raj
"""
import random 
class Bank(object):
    
    def __init__(self,balance=1000):
        self.balance=balance
        
    def addCash(self):
        while True:
            try:
                addcash=int(raw_input("Please enter amount to add in multiples of 10: "))         
            except ValueError:
                print("Enter Valid amount..Please try again")
                continue
            
            if addcash >1 and addcash%10==0:
                self.balance=self.balance+ addcash
                break
            else:
                print("Enter Valid amount.. Plese try again!")
                continue            
        return self.balance
        
        
    def withdraw(self,bet=10):
        
        self.balance=self.balance-bet
        return self.balance
        
    def deposit(self,bet=10):    
        
        self.balance =self.balance+bet
        return self.balance
                
class CardPack(object):
    
     def __init__(self,card=''):
         self.card=card
      
     def shuffle(self):
         self.rank=['A','2','3','4','5','6','7','8','9','J','Q','K']*6
         self.shape=['Hearts','Spade','Clubs','Diamond']*6
         self.card=[random.choice(self.rank)] + [random.choice(self.shape)]
         return self.card
     

    # def cardValue(self):

def placeBet():
    bet=0
    pot=0
    bet=int(raw_input("Place bet in mulitples of $5"))
    pot=pot+bet
    print ("Pot value is: %d" %pot)
    return pot

def cardValue(card):
    value=0    
    temp=0
    if len(card)==0:
        return value
    else:  
        for i in range(len(card)):
            temp=card[i][0]
            if temp=='A':
                value=value+1
            elif temp=='K'or temp=='Q' or temp=='J':
                value=value+10
            else:
                value=value+int(temp)
        return value       
                
   


def gameStart():
    PlayerBalance=Bank()
    CardDeck=CardPack()
    playercard=[]
    dealercard=[]
    play=True
    pot=0
    
    print ("Welcome to Blackjack Game")
    print ("Black Jack pays 3 to 2")
    print ("Insurance pays 3 to 1")
    print ("Max Bet: $100" "\n" "Min Bet: $5")
    
    raw_input("Press Enter to Continue...")   

    while play==True:
        print("Your current balance is $%d.Do you want to add money?" %PlayerBalance.balance)
        ifAddCash=str(raw_input("Press y/n: "))
                    
        if ifAddCash =='Y'or ifAddCash=='y':
            PlayerBalance.addCash()
            continue
        else:
            print("")
            print("Your current Balance :$%d" %PlayerBalance.balance)
            print("")
            #placeBet()
            pot=placeBet()
            playercard.append(CardDeck.shuffle())
            dealercard.append(CardDeck.shuffle())
            playercard.append(CardDeck.shuffle())
            dealercard.append(CardDeck.shuffle())
            
            #playercard=CardDeck.hit()
            #playercard=playercard.hit()
            #ealercard=CardDeck.hitDealer()
            #dealercard=dealercard.hit()
            
            print("Player cards are:")
            print(playercard)
            print("Dealercards are:")
            print(dealercard[0])
            raw_input("press enter to reveal dealer cards")
            print(dealercard)
            x=cardValue(playercard)
            y=cardValue(dealercard)
            if x>y:
                print("Player Wins!")
            else:
                print("Dealer Wins!")
            play=False   
            

            
             