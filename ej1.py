#compra de articulos ejercicio1

articulos = int(input("ingrese la cantidad de sus articulos:"))

if articulos <= 3:
    print("Pagas en efectivo.")

if articulos >3:
    print("Pagas con cualquier forma de pago.")



# calcular el numero mayor de tres ejercicio 2

    num1 = int(input("Ingrese un numero:"))
    num2 = int(input("Ingrese un numero:"))
    num3 = int(input("Ingrese un numero:"))

    if num1 != num2 and num1 != num3 and num2 != num3:
        if num1 > num2:
            if num1 > num3:
                print("El numero mayor es:", num1)
            else:
                print("El numero mayor es:", num3)
        else:
            if num2 > num3:
                print("El numero mayor es:", num2)
            else:
                print("El numero maroy es:", num3)
    else:
        print("Ingrese tres numeros deiferentes:")



#identificar numero menor entre tres y su suma total ejercicio 3

        num1 = int(input("Ingrese un numero:"))
        num2 = int(input("Ingrese un numero:"))
        num3 = int(input("Ingrese un numero:"))

        if num1 != num2 and num1 != num3 and num2 != num3:
            if num1 < num2:
                if num1 < num3:
                    print("El numero menor es:", num1)
                else:
                    print("El numero menor es:", num3)
            else:
                if num2 < num3:
                    print("El numero menor es:", num2)
                else:
                    print("El numero menor es:", num3)

        else:
            print("Ingrese tres numeros diferentes")

        print("Su suma total es:", num1 + num2 + num3)


#ejercicio 4
        nombre = input("Ingrese su nombre:")
        hora = int(input("ingrese cantidad de horas trabajadas:"))
        sueldo = float(input("inggrese  "))

        if hora > 40:
            extra = hora - 40
            sueldo = (40 * sueldo) + (extra * (sueldo + sueldo * 0.50))
            print({nombre})
            print("Su sueldo es $:", sueldo)


#ejercicio 5
            camisa = float(input("Ingrese el costo del producto:"))
            cantidad = float(input("Ingrese la cantidad de productos:"))
            total = camisa + cantidad

            if cantidad > 0:
                if cantidad <= 3:
                    descuento = total * .10
                else:
                    descuento = total * .20

                print("Total a pagar por unidad: $", total - descuento)
                print("Su descuento es de:$", descuento)
                print("total a pagar:$", camisa * cantidad - descuento)

#ejercicio 6



