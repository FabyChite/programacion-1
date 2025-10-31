texto = print("Hola, soy un analizador de textos. ¿En qué puedo ayudarte hoy?")
while True:
    print("\n** Analizador de Textos **")
    print("Elige una opción:")
    print("1. Contar palabras")
    print("2. Contar caracteres")
    print("3. Encontrar una palabra específica")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "4":
        print("¡Adiós!")
        break
    elif opcion not in ["1", "2", "3"]:
        print("Opción inválida. Por favor, elige una opción válida.")
        continue

    texto = input("Por favor, ingresa el texto a analizar: ")

    if opcion == "1":
        palabras = texto.split()
        cantidad_palabras = len(palabras)
        print(f"El texto contiene {cantidad_palabras} palabras.")
    elif opcion == "2":
        cantidad_caracteres = len(texto)
        print(f"El texto contiene {cantidad_caracteres} caracteres.")
    elif opcion == "3":
        palabra_buscar = input("Ingresa la palabra que deseas encontrar: ")
        ocurrencias = texto.lower().count(palabra_buscar.lower())
        print(f"La palabra '{palabra_buscar}' aparece {ocurrencias} veces en el texto.")



