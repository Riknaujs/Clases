""""Ingresar por teclado 3 números enteros y mostrar
el menor de los 3 números ingresados y la suma de dichos números."""

x = int(input("Ingresar primer digito: "))
y = int(input("Ingresar segundo digito: "))
z = int(input("Ingresar tercer digito: "))

if (x < y) & (x < z):
    print(f"el numero {x} es menor")
elif (x < y) & (x < z):
    print(f"el numero {y} es menor")
else:
    print(f"el numero {z} es menor")
def suma(x,y,z):
    print(f"la suma total es: ", x + y + z)
suma(x,y,z)