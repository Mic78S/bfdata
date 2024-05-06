# tirer un numéro au hasard entre 1 et 3, puis tirer un numéro au hasard entre et 1 et 2, garder ces deux numéros en mémoire dans des variables
# alice choisit le numéro 1 et le numéro 1
# bob choisit le le numéro 1 et le numéro 2

#step 1 : tirer un numéro au hasard entre 1 et 3, puis le stocker en mémoire
#step 2 : le numéro de la variable alice est le 1, le numéro de la variable bob est le 1
    # comparer les valeurs de ces variables aux valeurs des variables alice et bob, 
    # pour chaque ==, victoires_alice += 1 et victoires_bob += 1
#step 3 : tirer un numéro au hasard entre 1 et 3, puis le stocker en mémoire
#step 4 : le numéro de la variable alice est le 1, le numéro de la variable bob est le 2
    # comparer les valeurs de ces variables aux valeurs des variables alice et bob, 
    # pour chaque ==, victoires_alice += 1 ou victoires_bob += 1
#step 5 : boucle for in range(1000)



# step1: les portes ont deux attributs possibles ouverte/ fermée et prix/rien
# tirer un nombre au hasard entre 1 et 3 qui désigne la porte dont l'attribut est prix, puis le stocker en mémoire
# les trois portes ont l'attribut fermé
# step2: Alice choisit une porte et Bob choisit une porte
# step3: une des trois portes a l'attribut est ouverte, elle est différente des choix de Bob et d'Alice et de celle tirée au hasard
# step4: Bob change de porte
# step5: comparer les choix d'Alice et de Bob au nombre tiré au hasard. Celui qui correspond gagne la partie.
# step5: boucle for in range(1000) sur les succès accumulés de Bob et d'Alice. Comparer les deux.

from random import randint

victoires_alice = 0
victoires_bob = 0


for i in range(1000):
    def portes_step1_alice():
        number = randint(1, 3)
        if number == 1:
            result =+ 1
        else:
            result = 0
        return result 
      
    victoires_alice = victoires_alice + portes_step1_alice()

    def portes_step1_bob():
        number = randint(1, 3)
        if number == 1:
          result =+ 1
        else:
            result = 0
        return result     
   
    victoires_bob = victoires_bob + portes_step1_bob()

    def portes_step2_alice():
        number = randint(1, 2)
        if number == 1:
          result =+ 1
        else:
            result = 0
        return result  

    victoires_alice = victoires_alice + portes_step2_alice() 

    def portes_step2_bob():
        number = randint(1, 2)
        if number == 2:
            result =+ 1
        else:
            result = 0
        return result  
   
    victoires_bob = victoires_bob + portes_step2_bob() 

print(victoires_alice)
print(victoires_bob)

success_rate_alice = victoires_alice / 1000
success_rate_bob = victoires_bob / 1000

print(f"Le taux de succès d'Alice est de {success_rate_alice}")
print(f"Le taux de succès de Bob est de {success_rate_bob}")


    
    




