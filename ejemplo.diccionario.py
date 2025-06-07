#Und iccionario en python es una estructura de datos que permite almacenar valores,claves, es util cundo queremos asociar claves con un dato.

# #ejemplo

# x=(input("nombre de la mascota:" ,))
# x1=(input("tipo de animal:" ,))
# x2=(int(input("ingrese la edad:" ,)))
# x3=(input("nombre del dueño:" ,))
# x4=(input("ciudad donde se encuentra:" ,)) #PROYECTO

# datos={
#     "n_mascota": "x",
#     "t_animal": "x1",
#     "edad": "x",
#     "n_dueño": "x3",
#     "c_actual": "x4",
# }
# print(f"el nombre del animal es {x} el tipo de animal es {x1} la edad es {x2} el nombre del dueño es {x3}la ciudad donde se encuentran es {x4}")

# ejemplo:

dictionary = {"a": 1,
              "e": 2,
              }
print()
print(dictionary)
print(f"clave a: {dictionary["a"]}")
print(f"clave e: {dictionary["e"]}")

dictionary = {"nombers":[18,20,28],
              "groups":["a","1","b",2]
              }

print(dictionary)
print(f"clave numbers: {dictionary,"umbers"}")
print(f"clave groups: {dictionary,"groups"}")

print(f"clave numbers: {dictionary,"numbers"[1]}")
print(f"clave groups: {dictionary[ "groups"],["b"]}")

print(dictionary,["z"])
