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

cliente=(input("que tipo de cliente eres:", ))
compra=(int(input("ingre el precio:", )))
clie=cliente
descuento=compra*0.20
total=compra-descuento 
if cliente==clie:
    print(f"su compra tiene un descuento por ser vip {total}")
else:
    print(f"su compra tiene un total de {compra}")


