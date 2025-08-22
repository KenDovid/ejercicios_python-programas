print("Ingrese los valores: ")

v1 = float(input("Primer valor: "))
v2 = float(input("Segundo valor: "))

signo = input("Seleccione el operador ( +, -, *, / ): ")

if signo == '+':
    print("El resultado de la suma es:", v1 + v2)
elif signo == '-':
    print("El resultado de la resta es:", v1 - v2)
elif signo == '*':
    print("El resultado de la multiplicación es:", v1 * v2)
elif signo == '/':
    if v2 != 0:
        print("El resultado de la división es:", v1 / v2)
    else:
        print("Error: División entre cero no permitida")
else:
    print("Operador no válido")
