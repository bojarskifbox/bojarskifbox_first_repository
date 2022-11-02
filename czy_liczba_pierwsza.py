import math
#  działa sprawnie do liczb 15-cyfrowych
a = int(input("podaj liczbę"))
c = []
d = a % 2
e = round(math.sqrt(a))


x = range(1, e+1)
for b in x:
    if a % b == 0:
        c.append(b)
print(c)

if len(c)==1:
    print("pierwsza")
else:
    print("złożona")
