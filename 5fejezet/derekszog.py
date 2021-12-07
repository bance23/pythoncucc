def derekszogu_e(a,b,c):
    derekszog = False
    
    a = int(a)
    b = int(b)
    c = int(c)
    
    oldalak = [a,b,c]
    print(oldalak)

    oldalak.sort()
    print(oldalak)        
    
    oldalak[0] *= oldalak[0]
    oldalak[1] *= oldalak[1]
    oldalak[2] *= oldalak[2]
    print(oldalak)
    
    if(oldalak[0] + oldalak[1] == oldalak[2]):
        derekszog = True
        
    return derekszog

print(derekszogu_e(4,3,5))