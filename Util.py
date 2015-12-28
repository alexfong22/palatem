# -*- coding: utf-8 -*-
#   adapt()
#   name()
#   theid()
#   humanify()
#   fixa()
#   fixthe()

from Namearr10 import namearr
from Numbarr10 import numbarr
from Posterarr import posterarr


def humanify(inpuk):
    return fixthe(fixa(inpuk))

def fixthe(inpuk):
    rtitle = inpuk[::-1]
    count = 0
    replace = ", The ("[::-1]
    while rtitle.find(replace) != -1:
        rtitle = rtitle.replace(replace, "( ", 1)
        count += 1
    if count>= 1:
        return "The " + rtitle[::-1]
    else:
        return rtitle[::-1]
    
    
def fixa(inpuk):
    rtitle = inpuk[::-1]
    count = 0
    replace = ", A ("[::-1]
    while rtitle.find(replace) != -1:
        rtitle = rtitle.replace(replace, "( ", 1)
        count += 1
    if count>= 1:
        return "A " + rtitle[::-1]
    else:
        return rtitle[::-1]
        









def name(inpuk):
    try:
        return [namearr[str(inpuk)]]
    except:
        return ["~~~"]
        
        
def poster(inpuk):
    try:
        return [posterarr[str(inpuk)]]
    except:
        return [""]
        
def numb(inpuk):
    try:
        return [numbarr[str(inpuk)]]
    except:
        return ["~~~"]
    