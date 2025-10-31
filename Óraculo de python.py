import random

def oraculo():
    print("🔮 Bienvenido al Oráculo de la Sabiduría 🔮")
    print("Haz una pregunta que pueda responderse con 'sí' o 'no'.")
    input("¿Cuál es tu pregunta?: ")

    respuestas = [
        "Sí, sin duda.",
        "No lo creo.",
        "Tal vez… el tiempo lo dirá.",
        "Por supuesto que sí.",
        "Definitivamente no.",
        "Es muy probable.",
        "No cuentes con ello.",
        "Las señales son confusas, intenta de nuevo.",
        "Depende de tus acciones.",
        "El universo dice que sí."
    ]

    print("\nEl oráculo responde...")
    print("✨", random.choice(respuestas), "✨")

oraculo()
