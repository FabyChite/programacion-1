info_tienda=("Game on!", 2010)
print("Informacion de la tienda:"), info_tienda
inventario={
    "The last of us":{"precio":60,"stock":10},
    "God of war":{"precio":50,"stock":15},
    "Uncharted 4":{"precio":40,"stock":20}
}

segundo_juego=list(inventario.keys())[1]
print("precio de", segundo_juego, ":", inventario[segundo_juego]["precio"])

primer_juego=list(inventario.keys())[0]
inventario[primer_juego]["stock"]-=1
print("stock restante de", primer_juego, ":", inventario[primer_juego]["stock"])
inventario[primer_juego]["stock"]

