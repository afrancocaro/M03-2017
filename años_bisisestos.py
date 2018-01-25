# !/usr/bin/python
# -*-coding: utf-8-*-

ano=input ("Introduce un año:")
if (ano%4==0):
	if (ano%100==0):
		if (ano%400==0):
			print("El año es bisiesto")
		else:
			print("El año no es bisiesto")
	else:
		print("El año es bisiesto.")
else:
	print("El año no bisiesto.")
