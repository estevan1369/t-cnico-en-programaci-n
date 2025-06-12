# sentencias
#ejempo 1
# a=2+3
# if a==4:
#     print("A es igual a cuatro")
# elif a==5:
#     print("A es igual a cinco")
# elif a==6:
#     rpint("A es igual a seis")
# else:
#     print("no se cumole la condicion") #DOCUMENTO

# ejempo 2
# creditobancario

# nombre=(input("ingtrese su nombre completo:", ))
# edad=(int(input("ingrese su edad:", )))
# credito=(float(input("ingrese su creditto:",))) # taller de condicionales

# if edad < 18:
#     print("no tiene permitido esto")
# elif edad >= 18:
#     print("si tiene permitido esto")
# elif credito >= 100:
#     print("puede crear su credito")
# else:
#     print("no se cumplen las condiciones")

#ejercicio 3
#entrada a un parque

# edad=int(input("ingrese su edad:", ))

# if edad == 0 and edad <= 4:
#     print("gratis")
# elif edad == 5 and edad <= 18:
#     print("5 euros")
# elif edad >= 18 and edad <=100:
#     print("18 euros")
# elif edad < 0:
#     print("no es una edad correcta\n")

# print ("se finaliza el programa ")

#ejercicio 4
#calculadora

# numero1=(float(input("ingrese el primer numero:", )))  #pido datos al usuario
# numero2=(float(input("ingrese el segundo numero:", )))

# print(f"ingresar numero correspondiente a la operacion")
# print(f"operacines:"\
#       "1:"\
#         "suma"\                                            #pido eljir la operacion
#             "2:resta"\
#                 "3:multiplicacion"\
#                     "4:division"\
#                         "5:exponente")

# operacion=(int(input("ingrese el numero de la operacion deseada:", )))
# suma=numero1+numero2
# resta=numero1-numero2
# multiplicacion=numero1*numero2                  #cree operuaciones
# division=numero1//numero2
# exponente=numero1**numero2


#                                               #deacuerdo a lo pedido se realiza la operacion

# if operacion ==1:
#     print(f"la suma de {numero1} y {numero2} es {suma}")
# elif operacion ==2:
#     print(f"la resta de {numero1} y {numero2} es {resta}")
# elif operacion ==3:
#     print(f"la multiplicacion de {numero1} y {numero2} es {multipliocacion}")
# elif operacion ==4:
#     print(f"la division de {numero1} y {numero2} es {division}")
# elif operacion ==5:
#     print(f"la exponente de {numero1} y {numero2} es {exponente}")
# else:
#     print("no ingresaste ningun numero")

#ejercicio 1
#verifica si un numero es positivo, negativo o cero

# numero=(int(input("ingrese un numero:",)))
# if numero== 0:
#     print("el numero es cero")
# elif numero > 0:
#     print("el numero es poditivo")
# elif numero < 0:
#     print("el numero es negativo")

#ejercicio 2
#calcula el mayor de dos numeros ingresados

# numero1=(int(input("ingrese el primer numero:", )))
# numero2=(int(input("ingurese el segundo numero:", )))
# if numero1 > numero2:
#      print(f"el numero {numero1} es mayor al {numero2}")
# elif numero2 > numero1:
#      print(f"el numero {numero2} es mayor al {numero1}")

# ejercicio 3
#determina si un numero es par o impar

# numero=(int(input("ingrese un numero:", )))
# if numero % 2 == 0:
#     print("el numero es par")                     # el signo % saca los residuos de las operaciones
# else:
#     print("el numero es impar")

#ejercicio 4
#dado un numero,verifica si esta entre 10 y 20

# numero1=(int(input("ingrese un numero:", )))
# if numero1 > 10 and numero1 > 20:
#     print(" el numero {numero1} no esta entre el 10 y 20")
# else:
#     print("el numero si esta estre el 10 y 20")

#ejercicio 5
#dado tres numeros encuentra el mayor utilizando condicionales

# numero1=(int(input("ingrese el primer numero:", )))
# numero2=(int(input("ingrese el segundo numero:", )))      #pedimos los datos
# numero3=(int(input("ingrese el tercer numero:", )))

# if numero1 >= numero2 and numero1 >= numero3:
#     mayor = numero1
# elif numero2 >= numero1 and numero2 >= numero3:     #comparamos usando condicionales
#     mayor = numero2
# else:
#     mayor = numero3

# print("el numero mayor es:", mayor)               #mostramos el resultado

# ejercicio 6
#calcula el precio final con un 10% de descuento si el total es mayor a 100

# compra=(int(input("ingrese el total de su compra:", )))
# descuento=compra*0.10
# total=compra-descuento
# if compra >= 100:
#     print(f"su compra supero 100 y tiene un descuento de {total}")
# else:
#     print(f"su compra tiene un total de {compra}")

#ejercicio 7
#verifica si una persona puede votar (mayor o igual a 18 años)

# edad=(int(input("ingrese su edad:",)))

# if edad < 18:
#      print("no tiene permitido votar")
# else:
#      print("si tiene permitido votar")

#ejercicio 8
# dado el precio y tipo de cliente (vip o normal) aplica un descuento del 20% solo al vip


# compra=(int(input("ingre el precio:", )))
# print("eres cliente vip ?"\
#       "ingresar"\
#         "si"\
#             "no")

# cliente=(input("que tipo de cliente eres:", )).upper()
# descuento=compra*0.20
# total=compra-descuento
# if cliente == "SI":
#     print(f"su compra tiene un descuento por ser vip {total}")
# elif cliente =="NO":
#     print(f"su compra tiene un total de {compra}")
# else:
#     print(" se produjo un error")

#ejercicio 9
#determina si un numero es multiplo de 5 y de 3 al mismo tiempo

# numero=(int(input("ingrese el numero:", )))

# if numero % 5 == 0 and numero % 3 == 0 :
#     print("el numero si es multiplo de 5 y 3 al mismo tiempo")
# else :
#     print("el numero no es multiplo de 5 y 3")

# ejercicio 10
#dado un numero revisa si es divisible entre dos numero dados

# numero1=(int(input("ingrese el primer numero:", )))
# numero2=(int(input("ingrese el segundo numero:", )))
# numero3=(int(input("ingrese el primer tercer:", )))

# if numero1 % numero2 == 0 and numero1 % numero3 == 0:
#     print("si es divisible")
# elif numero2 % numero1 == 0 and numero2 % numero3 == 0:
#     print("si es divisible 2")
# else:
#     print("es divisible entre el 3")

#ejercicio 11
#crea una lista con 5 numeros si el tercer numero es mayor que 10 muestra"mayor a 10" "menor igual a 10"

# numero=[2,3,4,5,6,]

# if numero[2] > 10:
#     print("mayor a 10")
# else:
#     print("menor o igual a 10")

#ejercicio 12
#verifica si el numeero 7 esta en la liata.si esta, muestra "esta en  la lista" so no, "no esta en la lista"

# numero=[3,5,7,9]
# if 7 in numero:
#     print("esta en la lista")
# else:
#     print("no esta en la lista")

#ejercicio 13
#suma los do primeros nunmeros, si la suma es mayor a 10 que muestre "suma alta" si no "suma baja"

# lista=[4,6,2,8]

# suma=[0]+[1]
# if suma > 10:
#     print("suma alta")
# else:
#     print("suma baja")

# ejercicio 14
#dada la lista,muestra el ultimo nombre.si es marta,muestra"nombre correcto" sino, "nombre diferente"

# nombres=["ana","luis","pedro","marta"]
# ultimo_nombre=nombres[-1]
# if ultimo_nombre == "marta":
#     print("nombre correcto")
# else:
#     print("nombre incorrecto")

# ejercicio 15
#crea una lista con tres colores.cambia el segundo color solo si es azul,y muestrala actualizada

# colores=["rojo","azul","amarillo"]
# if colores[1] == "azul":
#     colores[1] = "morado"
# print(f"lista actuallizada{colores}")

#ejercicio 16
#crea una tupla con valores. si el primero es mayor muestre "orden ascendente"

# tupla=[5,8,12,20]

# if tupla[0] < [3]:
#     print("orden descendente")
# else:
#     print("orden ascendente")

# #ejercicio 17
# #dada la tupla verifica si el segunado numero es mayor a 30

# tupla=[25,32,28]

# if tupla[1] > 30:
#     print("edad mayor")
# else :
#     print("edad menoir o igaul 30")

#ejercicio 18
#cambia de tupla a lista. cambia el sugundo numero a 10 soo si es 2, buelve a combertirla y muestrala

# tupla=[1,2,3]
# lista=list(tupla)
# if lista[1] == 2:             #cambiamos el 2 ppor el 10
#     lista[1] = 10
# nueva_tupla= tuple(lista)
# print(nueva_tupla)             # imprimimos el resultado

# ejercicio 19
#dad la tupla, accede al segundo numero si es mayor a 5 muestra "coordenada alta"

# tupla=[4,9]
# if tupla[1] > 5 :
#     print("coodenada alta")
# else :
#     print("coordenada baja")

#ejercicio 20
#compra si dos tuplas son iguales, si lo son muestra "tuplas iguales"

# tupla=[3,4]
# tupla1=[3,5]

# if tupla == tupla1 :
#     print("tuplas iguales")
# else :
#     print("tuplas diferentes")

#ejercicio 21 
#crea un diccionario si la edad es mayor a 18 muestra "adulto"

# diccionario={
#     "nombre": "juan",
#     "edad": 17
#     }
# if diccionario ["edad"] >= 18 :
#     print("adulto")
# else :
#     print("menor de edad")

# #ejercicio 22
# #crea un diccionario, si la edad es mayor a 18 cambia el valor de "edad" a 21, y muestralo 

# diccionario={
# "nombre" : "lucia",
# "edad" : 20
# }
# if diccionario["edad"] > 18 :
#     diccionario ["edad"] = 21
# print(f"{diccionario}")

#ejrcicio 23
#crea una diccionario. si no existe la clave, agrega con el valor "bogota" mostrar

# diccionario={
#     "nombre" : "carlos"
# }
# if "ciudad" not in diccionario :
#     diccionario ["ciudad"] = "bogota"
#     print(f"{diccionario}")

#ejercicio 24
#dado el diccionario verifica si la clave"pricio" exixte; si existe muestra su valor, si no, "no hay precio"

# diccionario={
#     "producto" : "pan ",
#     "precio" : 1200 
# }

# if "precio" in diccionario :
#     print(diccionario["precio"])
# else :
#     print("no hay precio")

#ejercicio 25
#crea un diccionario, si "pan" esta en el diccionario muestra su precio; si no muestra "producto no disponible"

diccionario={
    "pan" : 1200,
    "leche" : 2000
}
if "pan" in diccionario :
    print(diccionario["pan"])
else : 
    print("producto no disponible")

