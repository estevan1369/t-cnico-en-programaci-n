print("sistema_de_gestion_academica")

cargop=(input("ingrese el cargo:", ))   #estamos solicitando contraseñas
ti=(input("ingrese la ti:", ))

registro={
    "cargo": cargop, 
    "ti":ti
}
print()
print(registro)
print(f"clave cargo:{registro["cargo"]}")    #estamos confirmando la identidad
print(f"clave ti:{registro["ti"]}")

xx=(input("introdusca el apellido del etudiante:", ))   #estamos solicitando datos del estudiante
x=(input("introdusca el nombre del estudiante:", ))
x1=(input("introdusca la materia:", ))
x2=(float(input("intrudusca la nota des estudiante:", )))
x3=(float(input("intrudusca la nota des estudiante:", )))
x4=(float(input("intrudusca la nota des estudiante:", )))
x5=(float(input("intrudusca la nota des estudiante:", )))
x6=(float(input("intrudusca la nota des estudiante:", )))
x7=(input("introdusca el grado del estudiante:", ))
x8= x2 + x3 + x4 +x5 + x6
x9= x8 / 5
x10= x + " " + xx 
print("hola", x10 ,"en la materia de", x1 ,"tiene las siguientes notas", x3 ," ", x4 ," ", x5 ," ", x6, " ",x7, "con un promedio de", x9) #este pprintejecuta toda la informacion sobre el estudiante
