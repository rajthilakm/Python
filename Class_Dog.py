# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:06:25 2016

@author: raj
"""



class Circle(object):
    
    pi= 3.14
    
    def __init__(self,radius=1):
        self.radius=radius
        
    def area(self):
        return self.radius**2*Circle.pi        
    
    def perimeter(self):
        return self.radius*2*Circle.pi
        

class Animal(object): 
    def __init__(self):
        print ("Animal Created")
     
    def whoAmI(self):
        print "Animal"
        
    def eat(self):
        print "Eating"
        
    def sit(self):
        print "sitting"
        

class Dog(Animal):
    
    #Class Obeject Atributes
    species='mammal'
    
    def __init__(self):
        Animal.__init__(self)
        print ("Dog Created")
            
    def whoAmI(self):
        print "Dog"
        
    def bark(self):
        print "woof!"
        
            