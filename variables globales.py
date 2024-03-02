# Variable global
v_global = float(input('Variable global: '))
def f():
    # Accediendo a la variable global
    print("Valor de la variable global:", v_global)
def g():
    # Accediendo a la variable global
    print("Valor de la variable global:", v_global)


# Llamada a la función
f()
g()

# Modificando la variable global
# v_global = 100
print("Nuevo valor de la variable global:", v_global)
print("Valor de la variable global:", v_global)

v_global = 100000000
print("Nuevo Nuevo valor de la variable global:", v_global)
