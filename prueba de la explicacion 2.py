def suma(a, b):
    """Esta funcion devuelve la suma de dos numeros"""
    resultado = a + b
    return resultado
a = float(input("ingrese primer dato: "))
b = float(input("ingrese segundo dato: "))
# Llamada a la funcion con argumentos
resultado_suma = suma(a, b)
print(resultado_suma)
