# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:45:26 2016

@author: raj
"""
class Book(object):
    def __init__(self,title,author,pages):
        print ("A book has been created!")
        self.title=title
        self.author=author
        self.pages=pages
     
    def __str__(self):
        
        return "Title : %s , Author : %s , Pages : %s" %(self.title,  self.author, self.pages)
        


  
class Line(object):
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        self.distance= ((self.coor2[1]-self.coor1[1])**2+(self.coor1[0]-self.coor2[0])**2)**0.5
        return self.distance
    
    def slope(self):
        self.slope = float((self.coor2[1]-self.coor1[1]))/float((self.coor2[0]-self.coor1[0]))
        return self.slope
        
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def volume(self):
        
        self.volume= self.height*(self.radius**2)*3.14
        return self.volume
    
    def surface_area(self):
        self.surface_area=self.height*self.radius*2*3.14
        return self.surface_area