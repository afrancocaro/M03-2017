#!/usr/bin/python
# -*-coding: utf-8-*-

minimo = int(input("Escriba un número: "))
maximo = int(input(("Escriba un número mayor que" + str(minimo) + ": "))
while minimo >= maximo:
	maximo=int(input("Escriba un número entre" str(minimo) "no es mayor que" str(maximo) + ". Inténtelo de nuevo: "))
	numero= float(input("Escriba un número entre" + str(minimo) + "y" + str(maximo) + ":"))
contador=0

while minimo <=numero <= maximo:
	contador+1
	numero=float(input("Escribe un número entre" ,minimo, "y", str(maximo) + ".")
elif contador ==1
	print("Ha escrito 1 número entre", minimo, "y", str(maximo) + ".")
else:
	print("Ha escrito", contador, "números entre", minimo, "y", str(maximo) + ".")
print("Programa terminado")
