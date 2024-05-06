#L'idée d'un décorateur est de modifier le comportement d'une fonction. 
#C'est une fonction qui prend une fonction en paramètre et renvoie une fonction en retour.

def decorator(func):
    def wrapper():
        print("Before the function is called !")
        func()
        print("After the function is called!")
    return wrapper

def say_hello():
    print("Hello!")

say_hello()
#say_hello_modified = decorator(say_hello)
#say_hello_modified()

#print(say_hello_modified)

say_hello = decorator(say_hello)
say_hello()

# @ revient à appeler le decorator
@decorator
def say_hello():
    print("Hello!")

#il y a moyen de créer une fonction qui accepte autant d'arguments qu'on veut => *args

def decorator(func):
    def wrapper(*args, **kwargs):
        #keywords arguments, par exemple (name="Bastien"), on peut les donner dans n'importe quel ordre et on n'est pas obligé de les préciser
        print("Before the function is called !")
        func(*args)
        print("After the function is called!")
    return wrapper

def test(a, b, c):
    print(f"{a}, {b}, {c}")

data = [4, 5, 6]
test(data[0], data[1], data[2])
# ça revient à la même chose que la ligne suivante
test(*data)

test(1, 2, 3)


def test(*args):
    print(args)

data = [4, 5, 6]

test(1, 2, 3, 4, 5, 6, 7, "Hello", "Top")
# Grâce à *args, il met tout dans un tuple.

def do_multiples(number=2):
    def inner(func):
        def wrapper(*args, **kwargs):
            for i in range(number):
                func(*args, **kwargs)
        return wrapper
    return inner

@do_multiples(number=5)
def countdown(n):
    for i in range(n, -1, -1):
            print(i)

countdown(5)

# ----- Debug example -----

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Retunr value: {result}")
        return result
    return wrapper

@debug
def testing(word):
    print(word)
    return 6

testing("allo")



