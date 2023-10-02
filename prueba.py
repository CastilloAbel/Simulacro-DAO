from camion import Camion
from bidon import Bidon
from caja import Caja
from packing import Packing


def mostrarListado(listado):
    for i in listado:
        print(i)


def main():
    c = Camion("AAE432", 250)
    camion2 = Camion("END153", 150)
    c1 = Packing("Indumentaria", 2, 10, 0.5)
    c2 = Packing("Armamento", 10, 12, 0.8)
    c3 = Packing("Alimentos", 1, 54, 0.6)
    c4 = Packing("Provisiones", 3, 15, 0.2)
    b1 = Bidon("Nafta", 15, 1.3)
    b2 = Bidon("Aceite", 10, 0.8)
    b3 = Bidon("Acido", 10, 1.2)
    t1 = Caja("armas", 6)
    t2 = Caja("fusiles", 2)
    t3 = Caja("revolver", 5)
    t4 = Caja("balas", 3)
    t5 = Caja("rifles", 4)
    print("Datos iniciales de camiones...")
    print(c)
    print(camion2)

    print("--------")
    print("Subiendo Cargas...")
    try:
        c.subir_cargas(c1)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        c.subir_cargas(c2)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        c.subir_cargas(c3)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        c.subir_cargas(c4)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.subir_cargas(b1)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        c.subir_cargas(b2)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")

    print("------------")
    c.a_reparacion()
    print(c)
    print("---------")

    try:
        camion2.subir_cargas(b3)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.subir_cargas(t1)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.subir_cargas(t2)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")

    print("----------------")
    c.en_viaje()
    print(c)
    print("----------------")

    try:
        camion2.subir_cargas(t3)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.subir_cargas(t4)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.subir_cargas(t5)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        c.subir_cargas(c4)
    except Exception:
        print("Ha excedido el Limite")
    else:
        print("Carga Correcta")
    try:
        camion2.bajar_cargas(t5)
    except Exception:
        print("No se encontro la carga")
    else:
        print("Descargada...")

    print("-------------")
    camion2.en_viaje()
    c.de_regreso()
    print(c2)
    print(c1)

    print("----------------")
    print(c)
    print("Listado del camion 1")
    mostrarListado(c.cargas_en_orden())

    print("------------")
    print(camion2)
    print("Listado del camion 2")
    mostrarListado(camion2.cargas_en_orden())


if __name__ == "__main__":
    main()