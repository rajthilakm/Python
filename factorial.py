# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:21:43 2016

@author: raj
"""
import sys
from itertools import permutations as perm


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
    print "The number of possible sequences are : %s"%fact    
    return fact 
 
    
def printSequence(seq,fact):
    l=[]
#    for j in range(0,fact):
#        l=[]
#        for i in seq:
#            l.append(i)
#            l=l[0:i]+l[i:0]
#        print l    
    
    perm(seq)
    print (perm(seq))
    
                     
            
        
def main(argv):
  # seq=[]
   #seq=createSequence()
   #computeFactorial(seq)
   elements=createSequence()
   fact=computeFactorial(elements)
   printSequence(elements,fact)
   #all_perms(elements)

if __name__ == "__main__":
    main(sys.argv)
