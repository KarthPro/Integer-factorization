import numpy as np
from math import floor
import numpy as np
from random import randint
import time 
#%%
# Test pour savoir si le nombre premier ou non 
def NombrePremier(p):
    if(p == 2):
        return True,1

    if(p == 1 or p%2==0):
        return False,2

    return Rabin_Miller(p, 50,2)

# Rabin Millier Test Nombre Premier
def Rabin_Miller(p, iterations,count):
    r=0
    s=p-1
    p=int(p)
    
    Premier=True
    count+=1
    while(s%2==0):
        count+=1 
        r+= 1
        s=int(s// 2)

    for i in range(0,iterations):
        a = randint(2,p-1)
        x = pow(a, s, p)
        
        count+=3
        if(x==1 or x==(p-1)):
            continue
        
        for j in range(r-1):
            x = pow(x,2,p)
            count+=1
            if(x==p-1):
                break
        else:
            Premier=False
            
    return Premier,count
#%%

liste_ANaif=[]


def Algo_Naif_Rec(nb,count):
    res=NombrePremier(nb)
    count+=res[1] # nombrePremier(n)
    if(res[0]):        
        liste_ANaif.append(nb)
        count+=1  # if(res[0]):   
        return liste_ANaif,count
    else:
        count+=1  # if(res[0]):   
        for k in range(2,floor(np.sqrt(nb))+1):
        		
            res=NombrePremier(k)
            count+=1+res[1]  # if(res[0]):  + nombrePremier(n)
            if(res[0]):          
                # Si il est divisible, on ajoute k nombre premier dans 
                # la liste de la decomposition
                count+=1 # n%k==0
                if(nb%k==0):
                    liste_ANaif.append(k)
                    count+=1 # liste_ANaif.append(k)
                    return Algo_Naif_Rec(nb//k,count)
        return liste_ANaif,count

#%%
def AlgoNaif_Chrono(n):
    time1=time.time() 
    resultat=Algo_Naif_Rec(n,0)
    time2=time.time() 
    time3=time2-time1
    return resultat,time3

nbPremier=2*3*5*7*11*2*2*5

n=146182562237
n=1000
print(str(146182562237))
print(str(AlgoNaif_Chrono(146182562237)))
#t=146182562237  Trop Long pour l'algorithme Naif



"""
print("")
print("--------------------------------------------------------")
print("--                 DEBUT ALGORITHM NAIF                 --")
print("--------------------------------------------------------")
print("")
print("")
print("")
print("Test Algo Naif")
print("Valeur t : "+str(nbPremier))
resultat=Algo_Naif_Rec(nbPremier,0)
print("Decomposition en Facteur Premier : "+str(resultat[0]))
print("Compteur : "+str(resultat[1]))
print("")
print("--------------------------------------------------------")
print("--                 FIN ALGORITHM NAIF                 --")
print("--------------------------------------------------------")
print("")
print("")
"""

