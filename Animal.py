classe1 = input()
classe2 = input()
classe3 = input()

if classe1 == "vertebrado":
    if classe2 == "ave":
        if classe3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:  # mamifero
        if classe3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:  # invertebrado
    if classe2 == "inseto":
        if classe3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:  # anelideo
        if classe3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
