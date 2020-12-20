import numpy as np
import random
import math
from math import floor
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

"""
    Algorithme p-1 Pollard
    
    Algo de décomposition en produit de facteurs premiers 
    
    1) Principe:
    
    n entier tq p|n (n est divisible par p) avec n != p
    
    Petit Thrm Fermat : ( a^(p-1) - 1 )[p]     /// a^(p-1) congru 1 % p  
    avec a premier avec p 
    
    => Pour tout multiple M de p-1, 
    a^M - 1 [p] /// a^M - 1 congru 0 % p
    car a^[k(p-1)] - 1 = (a^p-1   - 1 )* Somme a^[i*(p-1)]  ou i allant de 0 à k-1
    
    
    
    Si p – 1 est B-superlisse pour un certain seuil B, 
    alors p – 1 divise le plus petit commun multiple des entiers de 1 à B.
    
    M = ppcm(1,..B)
    on a: a^M - 1[p]  Pour tout a premier p 
    
    
    Donc p | a^M - 1 
    
    Cas 1 : pgcd(n,a^M - 1)>=p
    Cas 2 : pgcd(n,a^M - 1) = n  #Cas ou il n'y a pas de facteur non trivial 

    
    
    3) Algo & Temps d'exécution
    
    Entrée : un entier composé
    Sortie : facteur non trivial de n ou echec
    
        1) Seuil de friabilité B
        2) Choisir a random dans (Z/nZ)* 
        3) Chaque nombre premier q <= B
        e = Partie Entier [log B / log q]
        a= a^(q^e) % n
        
        4) g = pgcd (a-1 , n)
        5) Si 1<g<n alors retourner g 
        6) Si g = 1 alors selectionner B plus grand & aller à l'étape 2 ou retourner echec
        7) Si g = n aller à l'étape 2 ou retourner echec
    

"""

#----------------------------------------------------------------------
#-------                    ALGO P-1 POLLARD                   --------    
#----------------------------------------------------------------------   

list_fact=[]

def p_1_Pollard(n,B,count):
   
    # pas de diviseur premier 1
    if (n == 1): 
        count+=1 # if (n == 1): 
        print("No Prime divisor for 1")
        list_fact.append(n)
        count+=1 # list_fact.append(n)
        return list_fact,count
    
    # 1) Choisir Seuil de Friabilité (dans les paramètres))
    
    BoundOk=False
    RandomOk=False
    
    while(BoundOk==False):
        count+=1 #  while(BoundOk==False):
        
        # 1)
        print("Bound value B : "+str(B))
        

        # Reinitialisation
        RandomOk=False
        
        
        ## Condition d'arrêt B < sqrt(N)
        count+=1 #  if(B> (np.sqrt(n)*100)):
        if(B> (np.sqrt(n)*100)):
            print("Algorithme terminé ! B > sqrt(n)")
            return -1
       
 
        if(B<2):
            count+=1
            print("B Trop bas, Erreur !")
            return list_fact,count
        

        # 2) define M = product(q^floor( log(B)/log(q)) )
        M=1
        for q in range(2,B+1):
            if(NombrePremier(q)[1]==True):
                M= M*(q**(floor(math.log(B)//math.log(q))) )

        while(RandomOk==False):           
            count+=1 #  while(BoundOk==False):
            
            # 3) randomly pick a coprime to n (fix a=2 if n is odd (impair))
         
            a=random.randint(2,n-1) # random number between 1 & n
            print("Random number a is : "+str(a))
                
            # 4) compute g = gcd(a^M − 1, n) 
            g=np.gcd( (a^M) - 1,n)
            print("gcd is : "+str(g))
            print("")
            
            
            # 5) 
            count+=1+1 #  if(g!=1 and g!=n):
            if(g!=1 and g!=n):
                RandomOk=True
                BoundOk=True
                print("Facteur Non Trivial : "+str(g))
                count+=NombrePremier(g)[1]+1 # if(NombrePremier(g)[0]==True):
                if(NombrePremier(g)[0]==True):
                    list_fact.append(g)
                    count+=1 # list_fact.append(g)
                    print("Current List Fact is : "+str(list_fact))
                    
                else:
                    other_factor=n//g
                    count+=NombrePremier(other_factor)[1]+1 # if(NombrePremier(other_factor)[0]==True):
                    if(NombrePremier(other_factor)[0]==True):
                        list_fact.append(other_factor)
                        count+=1 # list_fact.append(other_factor)
                        print("Current List Fact is : "+str(list_fact))
                    else:
                        return p_1_Pollard(other_factor,B,count)
                   
                count+=1+1+1+NombrePremier(n//g)[1] # if(n%g==0  and NombrePremier(n//g)[0]==True):
                if(n%g==0 and NombrePremier(n//g)[0]==True):
                    list_fact.append(n//g)
                    count+=1 # list_fact.append(n//g)
                    print("Current List Fact is : "+str(list_fact))
                
                # Facteur restant par exemple 11*11*13 on a fait 11*143 il faut verifier que 143 est encore divisible
                elif(n%g==0 and NombrePremier(n//g)[0]!=True):
                    count+=1+1+1+NombrePremier(n//g)[1] # if(n%g==0  and NombrePremier(n//g)[0]==True):
                    print("Reccurence !")
                    print("")
                    return p_1_Pollard(n//g,B,count)
                
                print("Les facteurs sont : "+str(list_fact))

                return list_fact,count
                        
            count+=1 #  if(g==1):
            if(g==1):
                
                # Choisir un B plus grand
                count+=1 #  if(B<=np.sqrt(n)*pow(10,len(str(n)))):
                if(B<=np.sqrt(n)*pow(10,len(str(n)))):
                    RandomOk=True
                    B=B+(len(str(n))//pow(10,len(str(n))))  # len(str(n)) longueur du chiffre n 
                                                        # Par exemple 12405 : len(n) = 5
                
                # Error
                else:
                    print("Erreur g==1 !")
                    return list_fact,count
            
            count+=1 # if(g==n):
            if(g==n):
                
                count+=NombrePremier(g)[1]+1 # if(NombrePremier(g)[0]==True):
                if(NombrePremier(g)[0]==True):
                    list_fact.append(g)
                    count+=1 # list_fact.append(g)
                    print("Listes des facteurs actuels: "+str(list_fact))
                
                # Error
                else:
                    if(B<=np.sqrt(n)*pow(10,len(str(n)))):
                         RandomOk=True
                         B=B+(len(str(n))//pow(10,len(str(n))))
                    else:  
                        print("Failure ! ")
                            
                    print("Les Facteurs sont : "+str(n))
                #return list_fact,count

#%%
B=10

def P1Pollard_Chrono(n,B):
    time1=time.time() 
    resultat=p_1_Pollard(n,B,0)
    time2=time.time() 
    time3=time2-time1
    return resultat,time3

n=146182562237
#n=2*2*2*5
#n=4217*4217*4217

print(str(2 * 5 * 7))
print(str(P1Pollard_Chrono(146182562237,B)))  
             
#----------------------------------------------------------------------
#-------                FIN ALGO P-1 POLLARD                   --------    
#---------------------------------------------------------------------- 
                
"""

print("")
print("--------------------------------------------------------")
print("--              ALGORITHME P-1 POLLARD                --")
print("--------------------------------------------------------")
print("")


print("Algorithm p-1 Pollard")
n=146182562237
print("Valeur n : "+str(n))
resultat=p_1_Pollard(n,0)
print("Decomposition en Facteur Premier : "+str(resultat[0]))
print("Compteur : "+str(resultat[1]))

print("")
print("--------------------------------------------------------")
print("--            FIN ALGORITHME P-1 POLLARD              --")
print("--------------------------------------------------------")
"""

"""
Defaut de L'algorithme : lorsque les facteurs nombres premiers sont tres petits
il se peut qu'ils ne soient pas trouvés number Smooth


"""