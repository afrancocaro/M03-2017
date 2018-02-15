#!/usr/bin/python
# -*-coding: utf-8-*-

print("NÚMEROS NEGATIVOS")
numero = int(input("¿Cuántos valores quiere introducir? "))
if numero < 0:
    print("¡No se puede, imposible¡")
else:
	contador = 0
	for i in range (1, numero + 1):
		valor = float(input(f"Escriba el número {i}: "))
		if valor < 0:
			contador=contador+1
	if contador == 0:
		print ("No se ha escrito ningún número negativo.")
	elif contador == 1:
		print ("Se ha escrito un número negativo.")
	else:
		print ("Ha escrito {contador} números negativos.")
