###
# Name: Sook Mun Wong, Chelsea Parlett-Pelleriti
# Student ID: 2303539 & 2298930
# Email: sowong@chapman.edu & parlett@chapman.edu
# Course: CS510 Fall 2017
# Assignment: CW-06
###

import numpy as np
import pandas as pd
import abscplane
from abc import ABC, abstractmethod

class ArrayComplexPlane(abscplane.AbsComplexPlane):
    """complex planes"""
    
    def gen_plane(self):
        '''make it plane'''
        self.plane =  []
        #xs-----------------------------------------------------------------------------
        self.dx = (self.xmax-self.xmin)/(self.xlen-1)
        multi = np.array(list(range(0,self.xlen))*self.ylen)  #array with index + 1, ylen times
#         print(multi*2)
        multi = multi * self.dx #multiply by dx to get how much to add
        multi = self.xmin + multi
#         for i in range(0,self.xlen-1):
#             s += self.dx #increment based on length of dx
#             s = round(s,3)
#             xs.append(s)
        #ys-----------------------------------------------------------------------------
        self.dy = (self.ymax-self.ymin)/(self.ylen-1)
        vec_y = np.array(list(range(0,self.ylen)))
        vec_y = np.repeat(vec_y,self.xlen)
#         print(vec_y)
        vec_y =  (self.ymin + vec_y*self.dy)*1j
#         print(vec_y)
#         s = self.ymin
#         for i in range(0,self.ylen-1):
#             s += self.dy #increment based on length of dy
#             s = round(s,3)
#             ys.append(s*1j)
        
#         for i in range(0,self.xlen):
#             p = []
#             for k in range(0,self.ylen):
#                 p.append(xs[i]+ys[k])
#             self.plane.append(p)
        #together------------------------------------------------------------------------
        self.plane = multi + vec_y

        self.plane = pd.Series(self.plane, index = list(i for  i  in  range(0,len(self.c[2]))))###################################
        print(self.plane.reshape(self.xlen,self.ylen).transpose())
        return self.plane.reshape(self.xlen,self.ylen).transpose()

        
    def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        self.plane =  []
        self.fs = []
        print("init fx")
        self.plane = self.gen_plane()
        
#         # The implementation type of plane is up to the user
#         # fs should be a list of functions, initialized to be empty
#         #x's
#         self.dx = (self.xmax-self.xmin)/(self.xlen-1)
#         xs = [self.xmin]
#         s = self.xmin
#         for i in range(0,self.xlen-1):
#             s += self.dx #increment based on length of dx
#             s = round(s,3)
#             xs.append(s)
#         self.dy = (self.ymax-self.ymin)/(self.ylen-1)
#         yx = []
#         ys = [self.ymin*1j]
#         s = self.ymin
#         for i in range(0,self.ylen-1):
#             s += self.dy #increment based on length of dx
#             s = round(s,3)
#             ys.append(s*1j)
        
#         for i in range(0,self.xlen):
#             p = []
#             for k in range(0,self.ylen):
#                 p.append(xs[i]+ys[k])
#             self.plane.append(p)

        
    def apply(self,f):
        '''apply function to plane and then append it to list of functions'''
        self.fs.append(f)
#         for i in range(0,len(self.plane)):
#             for k in range(0,len(self.plane[i])):
#                 self.plane[i][k] = f(self.plane[i][k])
#         print("apply fx")
#         print(self.plane)
        self.changeplane(f)
        
    def changeplane(self,f):
        '''apply function to plane'''
        self.plane = f(self.plane)
#         for i in range(0,len(self.plane)):
#             for k in range(0,len(self.plane[i])):
#                 self.plane[i][k] = f(self.plane[i][k])
        print("apply fx")
        print(self.plane)
        
    def refresh(self):
        '''refresh plane with original numbers'''
        print("refresh fx")
        self.plane = self.gen_plane()
        
        
    def zoom(self,newxmin,newxmax,newxlen,newymin,newymax,newylen):
        '''refresh plane with new given numbers and do functions again'''
        print("zoom fx")
        self.xmin=newxmin #pass in new plane parameters 
        self.xmax=newxmax
        self.xlen=newxlen
        self.ymin=newxmin
        self.ymax=newxmax
        self.ylen=newxlen
        
        self.plane = self.gen_plane()
        for f in self.fs:
            self.changeplane(f)
        return self.plane
    

           

            
            
     