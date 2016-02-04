# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:58:50 2016

@author: raj
"""
from sys import exit
import sys
def start():
    plr=''    
    plr1='' 
    plr2=''    
    turn=0
    winner=False
    R={'R1':{'A1':'A1','B1':'B1','C1':'C1'},'R2':{'A2':'A2','B2':'B2','C2':'C2'},'R3':{'A3':'A3','B3':'B3','C3':'C3'}}
    print ("Welcome to the Tic Toe Game")
    raw_input("Press Enter to continue...")
    print('')
    printBoard(R)
 #   chooseMarker()
    plr= chooseMarker()
    plr1=plr[0]
    plr2=plr[1]
    
    while (winner==False):
        
            R1=play1(R,plr1)
            R=R1
            printBoard(R)
            winner=checkWin(R,plr1,plr2)
            turn+=1
            if (turn<=4 and winner==False):            
                R2=play2(R,plr2)
                R=R2
                printBoard(R)
                winner=checkWin(R,plr1,plr2)
                #turn+=1
            elif (winner==False):
                print 'Game is Tie !'
                winner = True
                #return winner
            #return False
 #           return winner 
         

        
    
def printBoard(R):
    # print R['R1']['A1'],'|',R['R1']['B1'],'|',R['R1']['C1'])
 #    print ("%s|%s|%s", % (str(R['R1']['A1']),str(R['R1']['B1']),str(R['R1']['C1']))
     print('')
     print ('{} | {} | {}'.format(str(R['R1']['A1']),str(R['R1']['B1']),str(R['R1']['C1'])))
     print ('------------')
     #print ('A2''|''B2''|''C2')
     print ('{} | {} | {} '.format(str(R['R2']['A2']),str(R['R2']['B2']),str(R['R2']['C2'])))
     print ('------------')
    # print ('A3''|''B2''|''C3')
     print ('{} | {} | {}'.format(str(R['R3']['A3']),str(R['R3']['B3']),str(R['R3']['C3'])))
     
def chooseMarker():
    inp=''
    #play1=''
    #play2=''
    print('')    
    print("Player 1 : Choose your Marker - x or o")
    input1=raw_input(inp)
    
    input1=str(input1)
    if input1=='x':
        play1='x'
        play2='o'
    elif input1 =='o':    
        play1='o'
        play2='x'
    else:
        print("invalid input: Restart Game")
        exit
    print("Player 1: Your marker is %s"%play1)    
    print("Player 2: Your Marker is %s"%play2)  
    raw_input("Press Enter to continue...")
    return play1 , play2 
    
def play1(R,plr1):
   
    print('')   
    print ("Player 1 : Choose position")
    x=raw_input()
    if x[-1]=='1':
        if (R['R1'][x]!='o' and R['R1'][x]!='x'):
            R['R1'][x]=plr1
        else:
            print("Invalid Input1")
    elif x[-1]=='2':
        if (R['R2'][x]!='o' and R['R2'][x]!='x'):
            R['R2'][x]=plr1
        else:
            print("Invalid Input2")
    elif x[-1]=='3':
        if (R['R3'][x]!='o' and R['R3'][x]!='x'):
            R['R3'][x]=plr1
        else:
            print("Invalid Input3")
    else:
        print("Invalid Input")
    #print (R)
    return R 

def play2(R,plr2):
    print('')
    print ("Player 2 : Choose position")
    x=raw_input()
    if x[-1]=='1':
        if (R['R1'][x]!='o' and R['R1'][x]!='x'):
            R['R1'][x]=plr2
        else:
            print("Invalid Input1")
    elif x[-1]=='2':
        if (R['R2'][x]!='o' and R['R2'][x]!='x'):
            R['R2'][x]=plr2
        else:
            print("Invalid Input2")
    elif x[-1]=='3':
        if (R['R3'][x]!='o' and R['R3'][x]!='x'):
            R['R3'][x]=plr2
        else:
            print("Invalid Input3")
    else:
        print("Invalid Input")
   # print (R)
    return R 
    
def checkWin(R,play1,play2):
    if (R['R1']['A1']==R['R2']['A2']==R['R3']['A3']):
        if R['R1']['A1'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")
        return True        
    elif (R['R1']['B1']==R['R2']['B2']==R['R3']['B3']): 
        if R['R1']['B1'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")
    elif (R['R1']['C1']==R['R2']['C2']==R['R3']['C3']): 
        if R['R1']['C1'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")    
    elif (R['R1']['A1']==R['R1']['B1']==R['R1']['C1']): 
        if R['R1']['C1'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")   
    elif (R['R2']['A2']==R['R2']['B2']==R['R2']['C2']): 
        if R['R2']['C2'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")   
    elif (R['R3']['A3']==R['R3']['B3']==R['R3']['C3']): 
        if R['R3']['C3'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")
    elif (R['R1']['A1']==R['R2']['B2']==R['R3']['C3']): 
        if R['R1']['A1'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")   
    elif (R['R1']['C1']==R['R2']['B2']==R['R3']['A3']): 
        if R['R2']['C2'] == play1:
            print("Winner is PLayer 1")
        else: 
            print ("Winner is Player 2")   
    else:
        return False                  
#    else:
#        print("The game is a TIE!")
        #return False
 #   else:
        #return True
        
def main(argv):
    replay=''    
    start()
    replay=raw_input("Do you like to play again?Press y/n..")
    while replay=='y':
        start()
     
    print("Thanks for playing!")
    
    
if __name__ == "__main__":
    main(sys.argv)
    