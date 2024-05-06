from random import randint

participants = {"alice": [1, 1], "bob": [1, "x"]}

total_succes_alice = 0
total_succes_bob = 0

def monthy_etape1(): 
    prix = randint(1, 3)
    return prix

porte_fermee = monthy_etape1()

def monthy_etape3():
    porte_ouverte = 0
    if porte_fermee == 1:
        porte_ouverte = randint(2, 3) 
        if porte_ouverte == 2:
            participants["bob"[2]] = 3
        else:
            participants["bob"[2]] = 2
    elif porte_fermee == 2:
        porte_ouverte = 3 
        participants["bob"[2]] = 2
    else:
        porte_ouverte = 2 
        participants["bob"[2]] = 3
    return porte_ouverte

porte_ouverte_etape3 = monthy_etape3()

def victoires_alice():
    victoires_alice = 0
    if porte_fermee == 1:
        victoires_alice =+ 1
    else: 
        victoires_alice =+ 0
    return victoires_alice
    
def victoires_bob():
    victoires_bob = 0
    if porte_fermee == 2 and participants["bob"[2]] == 2:
        victoires_bob =+ 1
    elif porte_fermee == 3 and participants["bob"[2]] == 3:
        victoires_bob =+ 1
    else:
        victoires_bob =+ 0
    return victoires_bob

wins_alice = victoires_alice()
wins_bob = victoires_bob()

total_succes_alice = []
total_succes_bob = []

for _ in range(1000):
    monthy_etape1()
    porte_fermee = monthy_etape1()
    monthy_etape3()
    porte_ouverte_etape3 = monthy_etape3()
    victoires_alice()
    wins_alice = victoires_alice()
    if wins_alice == 1:
        total_succes_alice.append("1")
    victoires_bob
    wins_bob = victoires_bob()
    if wins_bob == 1:
        total_succes_bob.append("1")

print(f"Sur 1000 parties, Alice a gagné {len(total_succes_alice)} fois.")
print(f"Sur 1000 parties, Bob a gagné {len(total_succes_bob)} fois.")

taux_succes_alice = len(total_succes_alice) / 1000
taux_succes_bob = len(total_succes_bob) / 1000

print(f"Le taux de réussite d'Alice est de {taux_succes_alice}.")
print(f"Le taux de réussite de Bob est de {taux_succes_bob}.")

