# 1049 - Animal
name1 = input()
name2 = input()
name3 = input()

if name1 == 'vertebrado':
    if name2 == 'ave':
        if name3 == 'carnivoro':
            print("aguia")
        elif name3 == 'onivoro':
            print("pomba")
    elif name2 == 'mamifero':
        if name3 == 'herbivoro':
            print("vaca")
        elif name3 == 'onivoro':
            print("homem")

elif name1 == 'invertebrado':
    if name2 == 'inseto':
        if name3 == 'hematofago':
            print("pulga")
        elif name3 == 'herbivoro':
            print("lagarta")
    elif name2 == 'anelideo':
        if name3 == 'hematofago':
            print("sanguessuga")
        elif name3 == 'onivoro':
            print("minhoca")
