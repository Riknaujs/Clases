camisa = float(input("Ingrese el costo del producto:"))
cantidad = float(input("Ingrese la cantidad de productos:"))
total = camisa + cantidad

if cantidad > 0:
    if cantidad <= 3:
        descuento = total * .10
    else:
        descuento = total * .20

    print("Total a pagar por unidad: $", total - descuento)
    print("Su descuento es de:$",descuento)
    print("total a pagar:$",camisa * cantidad - descuento)
