"""Programa para hallar la raiz con exponente n"""

print("\n-------------------------------------")
print("-------- RAIZ CON INDICE n ----------")
print("-------------------------------------" + "\n")

#input

n = input("Indice de la raiz: ")
n = int(n)
X = input("Radicando de la raiz: ")
X = int(X)

#processing

Z = X**(1/n)

#output

print("El valor de la raiz con indice " + str(n) + " del valor " + str(X) + " es igual a: " + str(Z))
