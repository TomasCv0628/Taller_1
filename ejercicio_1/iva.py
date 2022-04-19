"""PROGRAMA PARA CALCULAR EL IVA Y 
 PRECIO DE VENTA DE UN PRODUCTO"""

print("\n-----------------------------------")
print("---- IVA Y PRECIO DE VENTA --------")
print("-----------------------------------\n")

# input
x = input("Valor de del producto: ")
x = int(x)
y = input("Valor de del IVA: ")
y = int(y)

# processing

z1 = (x * y) / 100
z2 = x + z1

# output

print("El valor del producto del producto " + str(x) + " con el valor del IVA a " + str(y)
 + " Es igual a: " + str(z1) + "\ny su valor total es: " + str(z2))
