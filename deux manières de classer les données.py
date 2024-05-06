#deux manières de classer les données d'un tableur

users_dict = {"id": [42, 1],  "username": ["bko", "admin"], 
    "email": ["mail1", "mail2"]}

users_list = [ {"id" }]

users_dict["username"][0] = "bko"
#users_list[0] ["id"] = "bko"

print(users_dict.values())

scores = {"a":4, "b":6, "c":3}
print(max(scores.values()))

for name, score in scores.items():
    print(f"{name} has {score} point")

squares = [x * x for x in range(100)]
#print(squares)

even_squares = [x * x for x in range(100) if x % 2 == 0]
print(even_squares)


from random import randint
rnd = [randint(0,100) for i in range(100)]
print(rnd)

# du python idiomatique, typique de python

names = ["Cori", "Graham", "Ian", "Kathleen", "Cameron"]
# long_names = [name for name in names] dans ce cas, print(names) serait identique à print(long_names)
long_names = [name for name in names if len(name) >=5]
print(long_names)

keys = ["first", "second", "third"]
scores = {k: 0 for k in keys}
# pour faire une compréhension de dict

