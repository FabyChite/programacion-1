while True:
    print("** Calculadora Interactiva **")
    print("Elige una operación:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "5":
        print("¡Adiós!")
        break
    elif opcion not in ["1", "2", "3", "4"]:
        print("Opción inválida. Por favor, elige una opción válida.")
        continue

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Error: Los valores ingresados no son números válidos.")
        continue

    if opcion == "1":
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es {resultado}")
    elif opcion == "2":
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es {resultado}")
    elif opcion == "3":
        resultado = num1 * num2
        print(f"El producto de {num1} y {num2} es {resultado}")
    elif opcion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es {resultado}")
        else:
            print("Error: No se puede dividir por cero.")

    print()