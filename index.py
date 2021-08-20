#Geraldo Ventura
#2021-0104
import os
from  func import *

continuar = True


    
while continuar:
    os.system('cls')

    print("""
===============================================
Aplicación para registrar personajes de ANIME: 
===============================================

    1- Gestionar Personajes. 
    2- Reporte de Personaje
    3- Configuración de Personaje
    4- Acerca De 
    5- Salir 

    """)
    opt = input("Digite una opcion valida: ")
    if opt == '1':
        cls()
        print("""
===============================================
Aplicación para registrar personajes de ANIME.:
===============================================

    A- Agregar personajes 
    B- Modificar personajes
    C- Eliminar personajes
    E- Volver atras

    """)
        opt = input("Digite una opcion valida: ")
        if opt == 'A' or opt == 'a':
            AgregarPersonaje()
        if opt == 'B' or opt == 'b':
            ModificarPersonaje()
        if opt == 'C' or opt == 'c':
            EliminarPersonaje()
        if opt == 'D' or opt == 'd':
            opt == '1'

    elif opt == '2':
        cls()
        print("""
===============================================
Aplicación para registrar personajes de ANIME:
=============================================== 

    A- Ver lista de personajes 
    B- Lista de personajes por signo zodiacal
    C- Exportar personajes a HTML
    D- Exportar para el mapa
    E- Lista de personajes por serie
    F- Lista de personaje por estado (Vivo, Muerto e indefinidos)
    G- Volver atras
    """)
        opt = input("Digite la opcion que prefiera: ")
        if opt == 'A' or opt == 'a':
            ListaPersonajes()
        if opt == 'B' or opt == 'b':
            ListaSigno()
        if opt == 'C' or opt == 'c':
            Exportar()
        if opt == 'D' or opt == 'd':
            Localization()
        if opt == 'E' or opt == 'e':
            ListaSerie()
        if opt == 'f' or opt == 'f':
            ListaEstado()
        if opt == 'G' or opt == 'g':
            opt == '2'

    elif opt == '3':
        cls()
        print("""
===============================================
Aplicación para registrar personajes de ANIME.
===============================================

    A- Modificar serie
    B- Eliminar serie
    C- Agregar serie
    D- Estados
    E- Genero
    F- Salir


        """)
        opt = input("Digite la opcion que prefiera: ")
        if opt == 'A' or opt == 'a':
            ModificarSeries()
        if opt == 'B' or opt == 'b':
            EliminarSerie()
        if opt == 'C' or opt == 'c': 
            AgregarSerie()
        if opt == 'D' or opt == 'd':
            Estados()
        if opt == 'E' or opt == 'e':
            Genero()
        if opt == 'F' or opt == 'f':
                opt == '2'
    elif opt == '4':
        AcercaDe()
    elif opt == '5':
        continuar = False
        input("Hasta luego.... Precione enter para salir. ")
    else:
        input("Por favor introduzca una opcion valida que sea del 1 al 5: ")