"""Pedir el nombre, el jornal y la cantidad de dias de un obrero.
Calcular el sueldo y devolver *pedir aumento* *estas bien* o *prestame unos pesos* dependiendo si
gana menos, igual o mas que 1m/mes cop """


nombre = input("ingrese su Nombre: ")
Jornal = input("ingrese jornal: ")
dias = int(input("ingresar dias laborados: "))
match dias:
    case  dias.lower():
