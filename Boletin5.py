from itertools import count
from operator import index
from random import triangular

from orca.punctuation_settings import left_single_quote

Ej = int(input("Escoge un ejercicio "))

#while Ej > 5:
#   Ej = int(input("Solo hay 5 ejercicios, escoge otro ejercicio "))

if Ej == 1:

  #Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20
 t = 9
 for i in range (10+1):
  t = t + 1
 print (t)

if Ej == 2:
 #Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

 F = float(input("Ingresa la temperatura en Fahrenheit: "))

 C = (F - 32) * 5/9

 print ("Temperatura en Celsius: ", C)


if Ej == 3:
#Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

 F = 0
 i = 0
 for i in range (12+1):
     C = (F - 32) * 5/9
     print ( F, "=", C)
     F = F+10

if Ej == 4:
#Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.

 num1 = int(input("Ingresa un numero: "))
 num2 = int(input("Ingresa un numero: "))

 i = num1
 for i in range (num1,num2+1):
     nump = i%2
     if nump == 0:
         print (i)

if Ej == 5:
#Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n. É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:

 numero = int(input("Ingresa un numero: "))

 def triangular(numero):
     for i in range (1, numero + 1):
        i = numero*(numero+1)/2
     return i
 print (triangular(numero))


if Ej == 6:
#Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.

 cantidad = int(input("¿Cuántos valores quieres ingresar? "))

 for orden in range(1, cantidad + 1):
    numero = int(input("Introduce el valor: "))

    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print("número: ", numero, " -> factorial = ", factorial)


if Ej == 7:
#Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

 for i in range(7):
  for num in range(i,7):
      print (i,"|", num,)


if Ej == 8:
#Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números de 0 a n.

 n = int(input("Introduce un numero: "))

 for i in range(n +1):
    for num in range(i, n +1):
        print(i, "|", num, )

if Ej == 9:
#Calcula a cantidade de números negativos, positivos e ceros que hai nun grupo de 10 números enteiros.

 lista = []
 neg = 0
 pos = 0
 cero = 0

 for i in range(0,10):
     n = int(input("Introduce un numero: "))
     lista.append(n)

 for n in lista:
  if n > 0:
   neg = neg + 1
  elif n < 0:
   pos = pos + 1
  else:
   cero = cero + 1

 print("Positivos:", pos)
 print("Negativos:", neg)
 print("Ceros:", cero)

if Ej == 10:
#Deseña un programa que calcule o área dun rectángulo cuxa base e altura pides por teclado. Asegúrate que estes valores sexan positivos, para eso valida os datos.

 altura = int(input("Introduce el altura: "))

 base = int(input("Introduce la base: "))

 if altura and base <0:
     print("Un valor o ambos son invalidos, pon numeros positivos")
 else:
  area = base * altura
  print("El area es: ", area)