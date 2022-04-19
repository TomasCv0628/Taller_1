"""Programa para encontrar el area y
perimetro de un circulo"""


print("\n*********************************")
print("******** Área y Perimetro *******")
print("************* de un *************")
print("************ CÍRCULO ************")
print("*********************************" + "\n")

#input

X = input("Valor del radio: ")
X = int(X)
#processing

import math

Z1 = 2 * math.pi * X
Z2 = math.pi * (X**2)
#output

print("El perimetro del circulo con radio " + str(X) + " Es igual a " + str(Z1) + "\n Y su área es " + str(Z2))
