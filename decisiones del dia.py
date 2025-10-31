def asistente_decisiones():
    print("=== Asistente de decisiones ===")
    dia = input("Ingresa el día de la semana: ")
    clima = input("Ingresa el clima (soleado, nublado, lluvioso): ")

    print("\nBasado en tus respuestas:")

    match dia:
        case "Lunes" | "Martes" | "Miércoles" | "Jueves" | "Viernes":
            if clima == "soleado":
                print("Es un buen día para trabajar al aire libre.")
            elif clima == "nublado":
                print("Podrías considerar trabajar en interiores.")
            elif clima == "lluvioso":
                print("Mejor quedarse en casa y trabajar desde allí.")
            else:
                print("Clima no reconocido. Por favor ingresa soleado, nublado o lluvioso.")

        case "Sábado" | "Domingo":
            if clima == "soleado":
                print("Perfecto para una excursión o actividad al aire libre.")
            elif clima == "nublado":
                print("Podrías considerar una actividad en interiores.")
            elif clima == "lluvioso":
                print("Es mejor quedarse en casa y disfrutar de un día de descanso.")
            else:
                print("Clima no reconocido. Por favor ingresa soleado, nublado o lluvioso.")

        case _:
            print("Día no reconocido. Por favor ingresa un día válido de la semana.")

asistente_decisiones()
