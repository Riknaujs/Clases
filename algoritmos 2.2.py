lista = []
sPalabra = input("ingrese su Nombre: ")
while sPalabra != "":
    lista += [sPalabra]
    print('escriba su jornal señor(a): ' + sPalabra)
    sPalabra = input()

print('Las palabras que ha escrito son: %s' % lista)
