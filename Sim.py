# -*- coding: utf-8 -*-
critics2 = {
"ind2":{1196:4,260:4,79132:5,608:5,1:1,5:3},
"ind":{1196:5,260:4,608:5,1:1},
"Birdlaw":{1200:4.3,79132:5,608:4,296:5,318:5,1196:5,260:5,3578:5,56782:5,58559:4,72308:5,1089:5,6874:5,1214:4.7,1213:4.2,1221:3,70286:4.5,1198:3,1690:0.5,858:4.9,99114:4,135887:1,2710:4.1,1968:5,1:1},
"1": {1196:2,260:4,79132:2,648: 5.0, 597: 4.0, 592: 3.0, 589: 3.0, 588: 4.0, 539: 3.0, 515: 5.0, 509: 4.0, 508: 5.0, 500: 3.0, 480: 5.0, 457: 4.0, 454: 4.0, 434: 3.0, 380: 4.0, 377: 3.0, 367: 4.0, 364: 4.0, 357: 4.0, 356: 5.0, 350: 4.0, 349: 4.0, 344: 3.0, 329: 4.0, 318: 5.0, 316: 3.0, 300: 5.0, 296: 5.0, 292: 4.0, 288: 5.0, 266: 3.0, 265: 5.0, 253: 3.0, 208: 3.0, 185: 3.0, 165: 4.0, 161: 4.0, 160: 3.0, 153: 3.0, 150: 4.0, 62: 4.0, 50: 4.0, 47: 3.0, 34: 4.0, 32: 4.0, 10: 3.0, 2: 3},
"2": {1196:2,260:4,79132:2,595: 5.0, 593: 5.0, 590: 4.0, 588: 4.0, 553: 5.0, 457: 5.0, 454: 5.0, 434: 4.0, 432: 4.0, 420: 5.0, 410: 3.0, 367: 5.0, 364: 5.0, 349: 4.0, 344: 4.0, 339: 4.0, 337: 4.0, 329: 3.0, 318: 5.0, 317: 5.0, 300: 4.0, 293: 3.0, 288: 1.0, 282: 4.0, 266: 4.0, 253: 4.0, 252: 3.0, 236: 4.0, 231: 3.0, 225: 3.0, 208: 3.0, 196: 2.0, 186: 3.0, 185: 3.0, 173: 2.0, 165: 2.0, 161: 4.0, 160: 3.0, 153: 3.0, 150: 4.0, 95: 3.0, 47: 2.0, 39: 3.0, 34: 5.0, 21: 3.0, 19: 4.0, 17: 5.0, 11: 3.0, 2: 3},
"3": {1196:2,260:4,79132:5,8865: 3.5, 8641: 2.0, 7361: 4.0, 6744: 4.0, 4621: 3.0, 4025: 2.5, 3897: 3.5, 3508: 4.0, 2791: 4.0, 2640: 2.5, 2420: 4.0, 2406: 4.0, 2134: 4.5, 2054: 3.0, 2012: 4.0, 1485: 3.0, 1380: 5.0, 1288: 4.5, 1270: 5.0, 1259: 4.0, 919: 5.0, 832: 3.5, 502: 3.5, 466: 3.0, 432: 3.0, 370: 4.0, 260: 5.0, 172: 2},
"4": {1196:4,260:4,79132:2,69757: 3.5, 8636: 3.0, 8169: 3.0, 3112: 4.0, 3101: 4.0, 2890: 4.5, 2699: 4.0, 2572: 3.5, 2353: 4.0, 1639: 4.0, 1500: 3.5, 1302: 5.0, 1278: 3.5, 1252: 5.0, 1242: 5.0, 805: 4.0, 555: 4.0, 435: 2.0, 370: 3.0, 318: 5.0, 315: 3.0, 172: 3.0, 163: 3},
}

import time
start_time = time.time()


from Critics10m import critics
from Util import name
from Namearr10 import namearr

def intl(set1,set2):
        keys_a = set(set1)
        keys_b = set(set2)
        intersection = keys_a & keys_b # '&' operator is used for set intersection
        return len(intersection)

def unl(set1,set2):
        keys_a = set(set1)
        keys_b = set(set2)
        intersection = keys_a | keys_b # '|' operator is used for set union
        return len(intersection)

def unle(set1,set2,set3,set4): #union extended
        keys_a = set(set1)
        keys_b = set(set2)
        keys_c = set(set3)
        keys_d = set(set4)
        intersection = keys_a | keys_b | keys_c | keys_d # '|' operator is used for set union
        return len(intersection)







#   0 = l1
#   1 = d1
#   2 = l2
#   3 = d2
def criticsim(prefs,critic1,critic2):
    l1 = set(dict((k, v) for k, v in prefs[str(critic1)].items() if v >= 4))   # 3 = meh  / is omitted
    d1 = set(dict((k, v) for k, v in prefs[str(critic1)].items() if v <= 2))
    l2 = set(dict((k, v) for k, v in prefs[str(critic2)].items() if v >= 4))
    d2 = set(dict((k, v) for k, v in prefs[str(critic2)].items() if v <= 2))
    ld = l1,d1,l2,d2
    likesp1 = ld[0]
    dislikesp1 = ld[1]
    likesp2 = ld[2]
    dislikesp2 = ld[3]
    nl = intl(likesp1,likesp2) # matching likes
    nd = intl(dislikesp1,dislikesp2) # matching dislikes

    
    nld = intl(likesp1,dislikesp2)  # conflicting likes/dislikes
    nld2 = intl(likesp2,dislikesp1) # conflicting likes/dislikes
    unlv = unle(likesp1,likesp2,dislikesp1,dislikesp2) # union = non-omitted set
    sm = float(float(nl+nd-nld-nld2) / float(unlv))
    return sm
    
    

def itemsim(prefs,itema,itemb):
    item1 = int(itema)
    item2 = int(itemb)
    bothrankedsimilar = 0
    bothrankeddifferent = 0
    bothranked = 0
    notmutuallyranked = 0
    for critic in prefs:
        if item1 and item2 in prefs[critic]:
            try:
            
                bothranked += 1
                it1 = prefs[critic][item1]
                it2 = prefs[critic][item2]
                if abs(it1-it2)==0:
                    bothrankedsimilar += 1
                if abs(it2-it1)>4:
                    bothrankeddifferent += 1
                
            
            except:
                notmutuallyranked += 1
    #print bothrankedpositive
    #print bothrankednegative
    #print bothrankeddifferent
    #print bothranked
    #print notmutuallyranked
    if bothranked == 0:
        return 0
    elif (bothrankedsimilar)>(50):
        if bothrankeddifferent<1111115:
            #print bothranked
            return float((bothrankedsimilar)-bothrankeddifferent)/bothranked





#print criticsim(critics,"ind","Birdlaw")
def similaritems(prefs,filmid,nl=5):
    count = 0
    ppx = []
    for title in namearr:
        count += 1
        ppx.append([itemsim(prefs,filmid,title),title])
        #if count % 1000 == 0:
        #        print count
    
    justids = []    
    recs = sorted(ppx,reverse=True)[:nl]
    for rec in recs:
        justids.append(int(rec[1]))
    return justids
    






def mgetsimilaritems(find,arraytofind,n=5):
    criticsrev = {}
    unsorted = []
    compoundstring = '{'
    for tilt in arraytofind:
        compoundstring += str(tilt) + ":5," 
    finstr = compoundstring + '}'
    mvl = eval(finstr)
    bvv = {"bvv":mvl}
    critclone = critics
    critclone.update(bvv)
    for critic in critclone:
        intersection = intl(bvv["bvv"],critclone[critic])
        if intersection >= 1:
            unsorted.append([intersection,critic]) 
    avv = sorted(unsorted)[::-1][1:401] # excludes first match which is bvv
    #print len(avv)
    for similar in avv:
        similcritic = similar[1]
        criticsrev.update(eval('{"'+str(similcritic)+'":'+str(str(critclone[similcritic]))+"}"))



    
    xl = similaritems(criticsrev,find,nl=n)
    if len(avv)<1:
        return ["Oops! not enough data"]
    else:
        
        return xl



def getsimilaritems(find,n=5):
    criticsrev = {}
    unsorted = []
    bvv = {"bvv":{find:5}}
    critclone = critics
    critclone.update(bvv)
    for critic in critclone:
        intersection = intl(bvv["bvv"],critclone[critic])
        if intersection >= 1:
            unsorted.append([intersection,critic]) 
    avv = sorted(unsorted)[::-1][1:401] # excludes first match which is bvv
    #print len(avv)
    for similar in avv:
        similcritic = similar[1]
        criticsrev.update(eval('{"'+str(similcritic)+'":'+str(str(critclone[similcritic]))+"}"))



    
    xl = similaritems(criticsrev,find,nl=n)
    if xl[0]==99912:
        return []
    else:
        
        return xl

#similarids = getsimilaritems(296,10)
#print similarids






