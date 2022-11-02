import sys

g1 = int(input("Gracz1_1=kamień, 2=papier, 3=nożyce"))
import random
g2 = int(random.randint(1,3))
if g1==1:
    print("KAMIEŃ")
elif g1==2:
    print("PAPIER")
elif g1==3:
    print("NOŻYCE")

if g2==1:
    print("KAMIEŃ")
elif g2==2:
    print("PAPIER")
elif g2==3:
    print("NOŻYCE")

if (g1==g2):
    print("REMIS")

elif(g1==1 and g2==2):
    print("WYGRYWA GRACZ: 2")
elif(g1==1 and g2==3):
    print("WYGRYWA GRACZ: 1")
elif(g1==2 and g2==1):
    print("WYGRYWA GRACZ: 1")
elif(g1==2 and g2==3):
    print("WYGRYWA GRACZ 2")
elif(g1==3 and g2==1):
    print("WYGRYWA GRACZ 2")
elif(g1==3 and g2==2):
    print("WYGRYWA GRACZ 1")
