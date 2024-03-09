#identificar numero menor entre tres y su suma total

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
            print("El numero menor es:", num2  )
        else:
            print("El numero menor es:", num3)

else:
    print("Ingrese tres numeros diferentes")

print("Su suma total es:", num1 + num2 + num3)
