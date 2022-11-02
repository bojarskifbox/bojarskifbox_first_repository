


gra = True
licznik = 0
koniec = False
while gra:
    przycisk = input("enter = start / wpisz: -koniec- by wyjść")
    if przycisk == "koniec":
        gra = False
    while gra:
        from pickle import FALSE
        import random
        liczba = random.randint(1,1000)
        # print(liczba)
        break
    while gra:
        x = int(input("zagadnij liczbę między 1 a 1000"))
        if x == liczba:
            print("wygrałeś")
            licznik+=1
            break
        elif x < liczba:
            print("daj większą")
        elif x > liczba:
            print("daj mniejszą")
    print("wygrałeś", licznik, "razy")
    end = input("Jeszcze raz? tak/nie")
    if end == "tak":
        continue
    elif end == "nie":
        gra = False
    else:
        gra = False
print("KONIEC - Twój wynik to:", licznik)
