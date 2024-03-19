"""semaforo"""
color = input("ingrese el color: ")

match color:
    case "rojo":
         print("pare")
    case "amarillo":
         print("cuidado")
    case "verde":
         print("siga")
    case _:
         print("no reconocido el color")
