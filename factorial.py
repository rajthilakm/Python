# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:21:43 2016

@author: raj
"""
import sys


def getInput():
    inputs=0
    inputs = raw_input('Enter a positve integer:')
    return inputs
    
def createSequence():
    y=[]
    x=int(getInput())
  #  print(type(x))
    for i in range(1,x+1):
      y.append(i)
    print 'The Orginal sequence is: %s '% y
    return y   
    
def computeFactorial(x):
    fact=1
    for i in x:
        fact= fact*i
#    return fact 
    print "The number of possible sequences are : %s"%fact
    
def printSequence(x,y):
    
    

            
        
        
def main(argv):
  # seq=[]
   #seq=createSequence()
   #computeFactorial(seq)
   seq=createSequence()
   fact=computeFactorial(seq)
   printSequence(seq,fact)

if __name__ == "__main__":
    main(sys.argv)
