Ej = int(input("Escoge un ejercicio "))

while Ej > 5:
    Ej = int(input("Solo hay 5 ejercicios, escoge otro ejercicio "))

if Ej == 1:

# 1- Codifica un programa que solicite un número por teclado e que saque un mensaxe que diga “É un número positivo”, sempre que cumpra esa condición.

 n = (float("Di un numero "))
 if n>0:
    print("Tu numero es positivo")
 else:
    print("Tu numero es negativo")

elif Ej == 2:
# 2- Escribe un programa no que se tecleen dous números. Se o primeiro é maior ou igual que o segundo,visualizaremos a resta. En calquera caso visualizaremos a suma.
 numero1= int(input("Di un numero "))
 numero2= int(input("Di otro numero "))

 if numero1>=numero2:
     print(numero1, "-", numero2, "=", numero1 - numero2)
 else:
     print(numero2, "+", numero1, "=", numero2 + numero1)

elif Ej == 3:
# 3- Codificar o programa que o teclear un número por teclado, mostre por consola o signo “ + “ se o número é positivo, o signo “ –“ se é negativo e “ 0 “ se é cero.

 numero = int(input("Di un numero "))
 if numero>0:
    print("Tu numero es positivo")
 elif numero<0:
    print("Tu numero es negativo")
 elif numero == 0:
    print("Tu numero es zero")


#elif Ej == 4:
# 4- Coñecidos, o nome e o peso de dúas persoas, o programa escribirá por consola os datos da persoa que pesa máis e a diferenza de peso entre elas.


elif Ej == 5:
# 5- Dados 3 números que se supoñen distintos, indicar cal é o maior.

 x = int(input("Di un numero "))

 y = int(input("Di un numero diferente "))

 while x==y:
    y = int(input("ERROR los numeros no son iguales, di otro numero "))

 else:
    z = int(input("Di un tercer numero distinto "))

 while x==z or y==z:
    z = int(input("ERROR los numeros no son iguales, di otro numero "))

 else:

    if x>y>z:
        print(x,  " > ",  z,  " > ",  y)
    elif z>x>y:
        print(z,  " > ",  x,  " > ",  y)
    elif y>z>x:
        print(y,  " > ", z,  " > ",  x)
    elif x>y>z:
        print(x,  " > ",  z,  " > ",  y)
    elif y>x>z:
        print(y,  " > ",  x,  ">",  z)
    elif z>y>x:
        print(z,  " > ",  y,  " > ",  x)

