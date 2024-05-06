#pour dire que je veux qu'une variable n'accepte qu'un certain type

def double(a: int):
    return a * 2

result = double(5)
print(result)

#mais si je mets une valeur en chaînes de caractères, il va quand même l'accepter; il va juste me signaler que son type ne correspond pas à ce qui est attendu
# pour les gens qui nous liront, on peut même préciser (a: int) -> int:

def yell(message: str):
    if type(message) != str:
        print("C'est une erreur")
    print(message.upper())

# ci dessus, le upper va être suggéré par l'autocomplétion grâce au : str mais à nouveau ça ne change pas le fonctionnement du code

# avec pydantic, il y aurait peut-être moyen de forcer l