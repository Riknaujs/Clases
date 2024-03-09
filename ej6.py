"""""- A un trabajador le descuentan de su sueldo el 10%, si su sueldo es menor o igual a 1000. por encima de 1000 y 
hasta 2000 el 5% del adicional, y por encima de 2000 el 3% del adicional. calcular el descuento y sueldo neto que
 recibe el trabajador dado su sueldo"""""


def calcular_descuento_sueldo(sueldo):
    if sueldo <= 1000:
        descuento = sueldo * 0.10
        sueldo_neto = sueldo - descuento
        return descuento, sueldo_neto
    else:
        return 0, sueldo

sueldo = float(input("Ingrese el sueldo del trabajador: "))
descuento, sueldo_neto = calcular_descuento_sueldo(sueldo)

print("El descuento es:", descuento)
print("El sueldo neto es:", sueldo_neto)
