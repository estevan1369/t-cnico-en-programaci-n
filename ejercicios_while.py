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
numS=17
ad=int(input("ingrese el numero secreto ¿si puredes?", ))
while ad != numS:
    if ad < numS:
        print("el numero es mayor")
    else:
        print("el numero es menor")
    ad=int(input("ingrese el numero secreto ¿si puedes?", ))
print("¡correcto!")
