"""Programa para realizar la suma de 
los primeros números entender positivos"""


print("\n❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈")
print("❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈")
print("❈❈❈❈❈❈❈❈❈❈❈❈ SUMATORIA ❈❈❈❈❈❈❈❈❈❈❈❈")
print("❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈")
print("❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈❈" + "\n")


# input

n = input("Inserte elvalor de N:")
n = int(n)

# processing

Z = int((n*(n+1))/2)

# output

print("\nLa suma de los " + str(n) + " primero terminos" +"\n" + "\nes: " + str(Z) + "\n")
