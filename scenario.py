import numpy as np
import math 
import random

class Scenario:
    #def __init__(self):
        
    def diagonal(self, w, h):
        presence = np.zeros((w, h)) #np.random.randint(2, size=(self.width,self.height))
        bulbs = np.zeros((w, h))
        for i in range(w):
            presence [i,i] = 1
            bulbs [i,i] = random.choice([-1,0]) #-1 means out of order
        return presence, bulbs
    
    def random (self, w, h):
        presence = np.zeros((w, h)) #np.random.randint(2, size=(self.width,self.height))
        for i in range(math.floor(w/2)):
            x = random.randint(0,w-1)
            y = random.randint(0,h-1)
            presence [x,y] = 1
        return presence

