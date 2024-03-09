nombre = input("Ingrese su nombre:")
hora = int(input("ingrese cantidad de horas trabajadas:"))
sueldo = float(input("inggrese  "))

if hora > 40:
    extra = hora - 40
    sueldo = (40 * sueldo) + (extra * (sueldo + sueldo * 0.50))
    print({nombre})
    print("Su sueldo es $:", sueldo)





