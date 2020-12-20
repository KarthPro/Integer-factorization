import numpy as np
from random import randint
import time 
"""
    Principe Mathématiques
    
    n=pq nombre entier composé, p facteur non trivial inconnu
    L'Algo va donc déterminer ce facteur non trivial
    On se place sur l'ensemble Z/nZ à Z/nZ 
    
    x0 appartient à Z/nZ choisi de façon aléatoire (np.random)

"""

"""
 Algorithme Rho Pollard
 entrée : un entier n composé, qui n est une puissance d'un nombre premier
 sortie : un facteur non trivial de n, ou alors une erreur
"""

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



def g(x,n):
    return ( ((x*x)+1)%n)
#%%
#----------------------------------------------------------------------
#-------                    ALGO RHO POLLARD                   --------    
#----------------------------------------------------------------------    


list_factor=[]

def Pollard_Rhos(n,count):
    x=2
    y=2
    d=1
    i=0
    
    # Pas de Facteur Premier pour 1 
    if (n == 1): 
        count+=1 # n == 1
        #print("No Prime divisor for 1")
        list_factor.append(n)
        count+=1 # list_factor.append(n)
        return list_factor,count
    
    while(d==1):
        count+=1 #while(d==1):
        x=g(x,n)
        y=g(g(y,n),n)
        d=np.gcd(abs(x-y),n)
        
        i=i+1
        
        #print("Itération : "+str(i))
        #print("x = "+str(x))
        #print("y = "+str(y))
        #print("pgcd("+str(abs(x-y))+","+str(n)+")= "+str(d))
        #print("")
        
    count+=1 #    if(d!=n):
    if(d!=n):
        res=NombrePremier(d)
        count+=res[1] + 1 # nombrePremier(n) + if(res[0]):
        if(res[0]):
            list_factor.append(d)
            count=+1+1 #i list_factor.append(d)
            
        else:
            other_fact=n//d
            res=NombrePremier(other_fact)
            count+=res[1] + 1 # nombrePremier(n) +       if(res[0]):
            if(res[0]):
                list_factor.append(other_fact)
                count+=1 #    list_factor.append(other_fact)
            else:
                return Pollard_Rhos(other_fact,count)
        
        res=NombrePremier(n//d)
        count+=res[1] # nombrePremier(n) 
        if(n%d==0  and res[0]==True):
            count+=1+1+1+1 #        if(n%d==0  and res[0]==True):
            list_factor.append(n//d)
            count+=1 #  list_factor.append(n//d)
        
        # Facteur restant par exemple 11*11*13 on a fait 11*143 il faut verifier que 143 est encore divisible
        elif(n%d==0  and res[0]!=True):
            count+=1+1+1+1+1+1+1 #   elif(n%d==0  and res[0]!=True):  + if(n%d==0  and res[0]==True): 
            return Pollard_Rhos(n//d,count)
   
        #print("Liste des facteurs : "+str(list_factor))
        return list_factor,count
     
    #d==n     
    else:
        res=NombrePremier(n)
        count+=res[1]+1 # nombrePremier(n) +  if(res[0]):
        if(res[0]):
            list_factor.append(n)
        else:
         #   print("Erreur ! ")
            return list_factor,count
        
        #print("Seul facteur : "+str(n))
        return list_factor,count

#%%
def Pollard_Rhos_Chrono(n):
    time1=time.time() 
    resultat=Pollard_Rhos(n,0)
    time2=time.time() 
    time3=time2-time1
    return resultat,time3

n=146182562237

print(str(146182562237))
print(str(Pollard_Rhos_Chrono(146182562237)))   

# Validé
"""
print("--------------------------------------------------------")
print("--              ALGORITHME RHO POLLARD                --")
print("--------------------------------------------------------")
print("")
n=146182562237
print("Test Algo RhoPollard")
print("Valeur n : "+str(n))
resultat=Pollard_Rhos(n,0)
print("Decomposition en Facteur Premier : "+str(resultat[0]))
print("Compteur : "+str(resultat[1]))

print("")

print("--------------------------------------------------------")
print("--            FIN ALGORITHME RHO POLLARD              --")
print("--------------------------------------------------------")
"""