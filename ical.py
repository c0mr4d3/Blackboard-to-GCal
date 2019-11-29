# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:26:37 2019

@author : Siddharth
"""

import time
from converter import makecsv
from login import blackboardlogin
from csvToEvent import addEvents

def main():
    blackboardlogin()
    time.sleep(3)
    makecsv()
    addEvents()
    
    
if __name__=="__main__" :
    main()
    
        
    
    
