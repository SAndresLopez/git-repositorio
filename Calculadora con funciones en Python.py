#Ahora haremos una calculadora:
def mostrar_menú():
    print(f"""Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")
    return int(input("Ingresa una opcion: "))

def pedir_valores():
    operando1 = float(input("Ingresa el primer valor: "))
    operando2 = float(input("Ingresa el segundo valor: "))
    return operando1, operando2

def ejecutar_operacion(opcion,salir):
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = operando1 + operando2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f"El resultado de la multiplicacion es: {resultado}")
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f"El resultado de la division es: {resultado}")
    elif opcion == 5:
        print("Saliendo del programa de calculadora, hasta pronto!")
        salir = True
    else:
        print("opcion no existe, selecciona otra opción")
    return salir

if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menú()
        salir = ejecutar_operacion(opcion, salir)