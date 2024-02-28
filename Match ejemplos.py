postre = input("ingrese su postre: ")
"galletas"
"brownies"
match postre:
    case "galletas":
        tiempo_coccion = 15
    case "brownies":
        tiempo_coccion = 25
    case _:
        tiempo_coccion = 0

if tiempo_coccion > 0:
    print(f"Horneando {postre} por {tiempo_coccion} minutos.")
else:
    print("Postre no reconocido.")
