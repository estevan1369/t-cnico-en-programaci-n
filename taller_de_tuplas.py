#tupls : es muy similar a las listas, con la unica diferencia que utiliza parentesis en lugar de corchetes

# ejemplo

x=("ingresa dies digitos  .")
x1=(int(input("numero 1:", )))
x2=(int(input("numero 2:", )))
x3=(int(input("numero 3:", )))
x4=(int(input("numero 4:", )))
x5=(int(input("numero 5:", )))
x6=(int(input("numero 6:", )))
x7=(int(input("numero 7:", )))
x8=(int(input("numero 8:", )))
x9=(int(input("numero 9:", )))
x10=(int(input("numero 10:", )))

xp=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
c1=x1**2
c2=x2**2
c3=x3**2
c4=x4**2
c5=x5**2
c6=x6**2
c7=x7**2
c8=x8**2
c9=x9**2
c10=x10**2
sumatt=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10

promedio= sumatt//10
doble=sumatt*2
mitad=promedio//2

tup1=(x1,c1)
tup2=(x2,c2)
tup3=(x3,c3)
tup4=(x4,c4)
tup5=(x5,c5)
tup6=(x6,c6)
tup7=(x7,c7)
tup8=(x8,c8)
tup9=(x9,c9)
tup10=(x10,c10)

tuplas=[tup1,tup2,tup3,tup4,tup5,tup6,tup7,tup8,tup9,tup10]

print(f"los numeros que ingresaste{xp}")
print(f"el numero y su cuadrado{tuplas}")
print(f"la suma de los numeros{sumatt}")
print(f"el promedio de los numeros{promedio}")
print(f"el doble de la suma{doble}")
print(f"la mitad del promedio{mitad}")
