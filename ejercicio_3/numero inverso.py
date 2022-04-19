"""Programa para encontrar el inverso a
un número de cuatro digitos"""

print("•～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～")
print("•～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～")
print("•～ •～ •～ •～ • NÚMERO INVERSO •～ •～ •～  •～")
print("•～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～")
print("•～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～ •～")

# input
X = input("\ningrese el numero de cuatro digitos: ")
X = int(X)


#processing

Z1 = X % 10
Z2 = int((X % 100)/10)
Z3 = int((X % 1000)/100)
Z4 = int((X - (X % 1000))/1000) 

#output

print("\nEl inverso de los digitos " + str(X) + " es: " + str(Z1) + str(Z2) + str(Z3) + str(Z4) + "\n")

