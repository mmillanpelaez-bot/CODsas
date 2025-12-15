#Indica cuantos caracteres tendra la contraseña
from random import randint, shuffle

caracteres = randint(6,12)

letras = randint(1,caracteres)

mayusculas = randint(1,letras)

simbolos = randint(1,caracteres)

numeros = randint(1,caracteres)

lmayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lminusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Ncontra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

Scontra = ['!','"','·','$','%','&','/','(',')','=','?','¿','¡','^','*','+','-','_','.',',',';',':','<','>','@','#','~','{','}','[',']','|']


while letras + simbolos + numeros != caracteres:

    caracteres = randint(6, 12)

    letras = randint(1, caracteres)

    mayusculas = randint(1, letras)

    simbolos = randint(1, caracteres)

    numeros = randint(1, caracteres)


sim = 0
Ssim = []
for sim in range (simbolos):
   shuffle(Scontra)
   Ssim.append(Scontra[0])
   sim = sim + 1


num = 0
lnum = []
for num in range (numeros):
   shuffle(Ncontra)
   lnum.append(Ncontra[0])
   num = num + 1


Lmay = 0
L = []
for Lmay in range (mayusculas):
   shuffle(lmayus)
   L.append(lmayus[0])
   Lmay = Lmay + 1

lmin = 0
l = []
for lmin in range(letras - mayusculas):
    shuffle(lminusculas)
    l.append(lminusculas[0])
    lmin = lmin + 1


contraseña = l + L + lnum + Ssim

shuffle(contraseña)

print(contraseña)
