import string
import random

special = '!@#$%^&*'

password = []

# d = int(input("ile duzych?"))
# m = int(input("ile malych?"))
# c = int(input("ile cyfr?"))
# s = int(input("ile symboli?"))

for l in range(2):
    duza = random.choice(string.ascii_uppercase)
    password.append(duza)

for l in range(5):
    mala = random.choice(string.ascii_lowercase)
    password.append(mala)

for l in range(2):
    cyfra = random.choice(string.digits)
    password.append(cyfra)

for l in range(1):
    symbol = random.choice(special)
    password.append(symbol)

random.shuffle(password)

print(" ".join(password))