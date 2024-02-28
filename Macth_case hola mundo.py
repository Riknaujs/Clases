nombre = input("Ingrese su nombre: ")

match nombre.lower():
    case "james" | "ricardo" | "maria" | "jose" | "luis" | "ramon" | "jesus" | "juan" | "alexandra" | "alejandra" |\
         "valentina" | "james" | "alejandro" | "miguel" | "sergio" | "moises":
        print("Hola mundo, soy " + str(nombre))
    case _:
        print("Hola mundo, no reconocí tu nombre")
