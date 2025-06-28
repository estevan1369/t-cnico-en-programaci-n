# ejercicio1
# pide numeros enteros y sumalos hasta que ingrese un 0 y muestra eñl total

# total=0
# num1=(int(input("ingrese un numero entero",)))

# while num1 !=0:
#     total+=num1
#     num1=(int(input("ingresa otro numero",)))
#     print(f"la suma toatl es:{total}")

#ejercicio2
#crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente

# contraseña=(input("ingrese la contraseña", ))
# clave="pytho123"
# while clave != "contraseña":
#     contra=(input("ingrese la contraseña", ))
#     print("¡contraseña incorrecta!")
#     contra=(input("ingrese la contraseña",))
#     print("¡acabas de iniciar zexion!")

#ejercicio3
#pide productos y guardalos en una lista. termina cuando el usuario escriba fin, y muestra toda la lista

# lista=[]
# producto=(input("ingresa un producto(y unado termine escribe 'fin' para salir): "))
# while producto.lower() !="fin":
#     lista.append(producto)
#     producto=(input("ingresa un producto(y unado termine escribe 'fin' para salir): "))
# print(f"tus compras son: {lista}")

# ejercicio4
#pide 10 numeros al usuario;utiliza while para contarulos y guarda los pares y los impares

# par=0
# impar=0
# contador=0
# while contador < 10:
#     numero=int(input(f"ingrese los numeros {contador + 1}:  "))
#     if numero %2==0:
#         par +=1
#     else:
#         impar+=1
#     contador+=1

# print(f"los impares son:{impar}")
# print(f"los pares son:{par}")

#ejericio5
#pide ingresar notas entre 0 y 5 hasta que escriba salir. guarda las notas en una lista y muestra el promedio

# lista=[]
# while True:
#     notas=float(input("ingresa una nota(o ingresa '0' para terminar): "))
#     if notas == 0: 
#         break
#     lista.append(notas)
# if lista:
#     pro =sum(lista)/ len (lista)
#     print(f"promedio de notas: {pro}")
# else:
#     print(f"no ingresaste ningun dato valido")

#ejercicio6
#pide un numero y realiza la tabla el  numero

# num=(int(input("ingresa un numero", )))
# contador=1
# while contador <=10:
#     result=num*contador
#     print(f"{num} * {contador} = {result}")
#     contador+=1

# ejercicio7
#el programa toiene un numero secreto, el usuario debe adivinar y el programa indicar si es mayor o menor.

# numS=17
# ad=int(input("ingrese el numero secreto si puredes", ))
# while ad != numS:
#     if ad < numS:
#         print("el numero es mayor")
#     else:
#         print("el numero es menor")
#     ad=int(input("ingrese el numero secreto ¿si puedes?", ))
# print("¡correcto!")

#ejercicio8
#rea una tupla, pide al usuario que adivine las frutas que estan dentro de la tupla

# tuplas= ("manzana","pera","uva","tomate")
# fruta=(input("ingrese una frupa:", ))

# while fruta not in tuplas:
#     print(f"la {fruta} no se encuentra en la lista")
#     fruta=(input("ingrese una frupa:", ))
# print(f"la {fruta} si se encuentra en la lista")

#ejercicio9
#crea un diccionario de 5 palabras que tengan su traduccion al ingles, y que al solicitar una palabra en español de la traduccion en ingles

# diccionario={
#     "leche": "milk",
#     "cafe": "coffi",
#     "agua": "water",
#     "ensalada": "salad",
#     "pollo": "chiken"
# }

# while True:
#     hola=input("estribe una palabra en español para traducir a igles: " )
#     if hola in diccionario:
#         print(f"la palabra {hola} si se encuentra en el diccionario {diccionario [hola]}")
#     else:
#         print(f"la palabra {hola} no se encuentra en el diccionario")

#ejercicio10
#haz un menu dentro de un while para que el usuario elija si sumar restar multiplicar dividir o salir,luego realiza la operacion
# print("\n.menu \n 1.suma \n2.resta \n 3.multiplicacion \n 4.division \n 5.salir")

# num1=(float(input("ingrese el primer numero: ")))
# num2=(float(input("ngrese el segundo numero: ")))
# while True:
#     opcion=(int(input("elige una de las 5 opciones(o oprime salir para finalizar): ")))
   
#     if opcion == 1:
#         result=num1+num2
#     elif opcion == 2:
#         result=num1-num2
#     elif opcion ==3:
#         result=num1*num2
#     elif opcion == 4: 
#         result=num1/num2
#     elif opcion == 5:
#         break
#     else:
#         print("opcion no valida")
#     print(f"{result}")

#ejercicio11
#ingresa nombre y edades, detente cuando el usuario escriba salir en nombre y finaliza mostrando el diccionaeio

# diccionario={
   
# }
# while True:
#     nombre=(input("ingrese su nombre(o ponga salir para finalizar): "))
#     if nombre.lower()=="salir":
#         break
#     edad=(int(input(f"ingrese la edad de {nombre}: ")))
#     diccionario[nombre] = edad
#     print(f"{diccionario}")

#ejercicio12
#crea una lista de 5 colores, y utiliza el bucle para que el usuario escriba colores hasta encontrar los que se encuentran el la lista 

lista=["rojo", "morado", "negro"]
colores=(input("ingrese un color hasta encontrar el corecto: "))
while colores not in lista:
    print(f"la {colores} no se encuentra en la lista")
    colores=(input("ingrese un color:", ))
print(f"la {colores} si se encuentra en la lista")





        
        
        
    




