import os
from peewee import *
import folium
import webbrowser
webbrowser


db = SqliteDatabase('HOLA')

zodiaco = ''


class goku(Model):
    nombre = CharField(100)
    apellido = CharField(100) 
    foto = CharField(10000)
    pronunciación = CharField(100)
    serie = CharField(100)
    año = IntegerField(50)
    mes = IntegerField(50)
    dia = IntegerField(50)
    poder = CharField(100)
    frase_favorita = CharField(100)
    edad= IntegerField(50)
    altura = CharField(100)
    sexo = CharField(100)
    estado = CharField(100)
    direccion = CharField(100)
    latitud = IntegerField(100)
    longitud = IntegerField(100)


    class Meta:
        database = db


db.connect()
db.create_tables([goku])
    


def cls():
    os.system('cls')




def AgregarPersonaje():
    cls()
    print("Vamos tu personaje. ")
    gerald = goku()
    gerald.nombre = input("Digite el nombre del personaje que prefiera: ")
    gerald.foto = input("Digite la url de la foto: ")
    gerald.apellido = input("Digite el apellido del personaje: ")
    gerald.pronunciación = input("Digite su pronunciacion : ")
    gerald.serie = input("Digite la serie de donde proviene el personaje: ")
    gerald.año = input("Digite el año de nacimiento del personaje: ")
    gerald.mes = input("Digite el mes de nacimiento del personaje: ")
    gerald.dia = input("Digite el dia de nacimiento del personaje: ")
    gerald.poder = input("Digite cual es su poder: ")
    gerald.frase_favorita = input("Digite su frase favorita: ")
    gerald.sexo = input("Digite su sexo: ")
    gerald.altura = input("Digite la altura del personaje: ")
    gerald.estado = input("Si esta vivo, muerto o indefinido: ")
    gerald.direccion = input("Digite la direccion donde se encuentra el personaje: ")
    gerald.latitud = input("Digite la latitud exacta donde vive el personaje: ")
    gerald.longitud = input("Digite la longitud exacta donde vive el personaje: ")
    input("Personaje guardado, presione enter para continuar")
    gerald.save()

def confirmarDato(campo,valor):
    print("El campo "+campo+" tiene el valor "+valor)
    tpm = input("Digite el nuevo valor o dejalo en blanco para no cambiar: ")
    if tpm == "":
        return valor
    else:
        return tpm 

def ModificarPersonaje():
    cls()
    print("Digite el persanaje que desea moodificar: \n")
    print("=================================================")
    for gerald in goku.select(): 
        print(f" Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} \n Fecha de nacimiento: {gerald.dia} - {gerald.mes} - {gerald.año} \n Poder:  {gerald.poder} \n Frase favorita: {gerald.frase_favorita} \n sexo: {gerald.sexo} \n Altura: {gerald.altura} \n Estado: {gerald.estado} \n Direccion: {gerald.direccion} \n Latitud: {gerald.latitud} \n Longitud: {gerald.longitud} ")
        print("=================================================")
    fda = input("Precione 1 para salir o digite el nombre a modificar: ")
    if fda == "1":
        return False
    gerald = goku.select().where(goku.nombre == fda).get()

    gerald.nombre = confirmarDato("Nombre",str(gerald.nombre))
    gerald.apellido = confirmarDato("Apellido",str(gerald.apellido))
    gerald.serie = confirmarDato("Serie",str(gerald.serie))
    gerald.año = confirmarDato("Año de nacimiento",str(gerald.año))
    gerald.mes = confirmarDato("Mes de nacimiento",str(gerald.mes))
    gerald.dia = confirmarDato("Dia de nacimiento",str(gerald.dia))
    gerald.poder = confirmarDato("Poder",str(gerald.poder))
    gerald.frase_favorita = confirmarDato("Direccion",str(gerald.frase_favorita))
    gerald.sexo = confirmarDato("Sexo",str(gerald.sexo))
    gerald.altura = confirmarDato("Altura",str(gerald.altura))
    gerald.estado = confirmarDato("Sexo",str(gerald.estado))
    gerald.direccion = confirmarDato("Direccion",str(gerald.direccion))
    gerald.latitud = confirmarDato("Latitud",str(gerald.latitud))
    gerald.longitud = confirmarDato("Longitud",str(gerald.longitud))
    gerald.save()

    input("Registro modificado, precione enter para continuar ")

def EliminarPersonaje():
    cls()
    print("Personajes agregados ")
    for gerald in goku.select(): 
        print("=================================================")
        print(f" Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} ")
        print("=================================================")
    idx = input("Digite el nombre del personaje que desea eliminar o precione 1 para salir: ")
    if idx == "1":
        return False

    gerald = goku.select().where(goku.nombre == idx).get()    
    input(f"El personaje: {gerald.nombre} fue borrado, precione enter para continuar ")
    gerald.delete_instance()

def ListaPersonajes():
    cls()
    for gerald in goku.select():
        print("=================================================")
        print(f" Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} ")
        print("=================================================")
     
    fda = input("Precione 1 para salir: ")
    if fda == "1":
        return False
    gerald = goku.select().where(goku.nombre == fda).get()

def  ListaSigno():
    gerald = goku()

    for gerald in goku.select():
        print("=================================================")
        print(f"Nombre: {gerald.nombre} \nApellido: {gerald.apellido} \nSerie: {gerald.serie} ")
        

        zodiaco = []
        if gerald.mes == 12:
            if gerald.dia >= 22:
                zodiaco = 'Capricornio'

        elif gerald.mes == 1:
            if gerald.dia <= 20:
                zodiaco = 'Capricornio'

        elif gerald.mes == 1:
            if gerald.dia >= 21:
                zodiaco = 'Acuario'

        elif gerald.mes == 2:
            if gerald.dia <= 19:
                zodiaco = 'Acuario'

        elif gerald.mes == 2:
            if gerald.dia >= 20:
                zodiaco = 'Pisis'

        elif gerald.mes == 3:
            if gerald.dia <= 20:
                zodiaco = 'Pisis'

        elif gerald.mes == 3:
            if gerald.dia >= 21:
                zodiaco = 'Aries'

        elif gerald.mes == 4:
            if gerald.dia <= 20:
                zodiaco = 'Aries'

        elif gerald.mes == 4:
            if gerald.dia >= 21:
                zodiaco = 'Tauro'

        elif gerald.mes == 5:
            if gerald.dia <= 21:
                zodiaco = 'Tauro'

        elif gerald.mes == 5:
            if gerald.dia >= 22:
                zodiaco = 'Geminis'

        elif gerald.mes == 6:
            if gerald.dia <= 21:
                zodiaco = 'Geminis'

        elif gerald.mes == 6:
            if gerald.dia >= 22:
                zodiaco = 'Cancer'

        elif gerald.mes == 7:
            if gerald.dia <= 23:
                zodiaco = "Cancer"

        elif gerald.mes == 7:
            if gerald.dia >= 24:
                zodiaco = "Leo"


        elif gerald.mes == 8:
            if gerald.dia <= 23:
                zodiaco = 'Leo'

        elif gerald.mes == 8:
            if gerald.dia >= 22:
                zodiaco = 'Virgo'

        elif gerald.mes == 9:
            if gerald.dia <= 23:
                zodiaco = 'Virgo'

        elif gerald.mes == 9:
            if gerald.dia >= 24:
                zodiaco = 'Libra'
            
        elif gerald.mes == 10:
            if gerald.dia <= 23:
                zodiaco = 'Libra'
        
        elif gerald.mes == 10:
            if gerald.dia >= 24:
                zodiaco = 'Escorpio'
            
        elif gerald.mes == 11:
            if gerald.dia <= 22:
                zodiaco = 'Escorpio'
    
        elif gerald.mes == 11:
            if gerald.dia >= 23:
                zodiaco = 'Sagitario'
            
        elif gerald.mes == 12:
            if gerald.dia <= 21:
                zodiaco = 'Sagirario'
        
        print("El signo de este personaje es:",zodiaco)
        print("=================================================")

    fda = input("Precione 1 para salir: ")
    if fda == "1":
        return False
    gerald = goku.select().where(goku.nombre == fda).get()


def Exportar(): 
    cls()
    
    for gerald in goku.select():
        print("=================================================")
        print(f" Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} ")
        print("=================================================")

    idx = input("digite el nombre del personaje a exportar: ")

    gerald = goku.select().where(goku.nombre == idx).get()

    f = open('holamundo.html','w')

    html ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Licendia para motores</title>
    </head>
    <body>
    <style>
        .container{
            margin: auto;
            padding: 10%;
            background-image:url("Licencia.jpeg");
            border-radius: 1px;
            background-repeat: no-repeat;
        }
        

 </style>""" + f"""
    <div class="container">
            <img src="{gerald.foto}">
            <li>Nombre: {gerald.nombre}</li>
            <li>Direccion: {gerald.direccion}</li>
            <li>Apellido: {gerald.apellido}</li>
            
    </div>
        </body>
         </html>
    """

    f.write(html)
    f.close()
    webbrowser.open('holamundo.html')

def ListaSerie():
    gerald = goku()
   
    idx = input("digite el nombre de la serie que desea ver: ")
    gerald = goku.select().where(goku.serie == idx).get()

    for gerald in goku.select():

        if idx == gerald.serie:
            print("=================================================")
            print(f"Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} ")
            print("=================================================")
    
    
    fda = input("Precione 1 para salir: ")
    if fda == "1":
        return False

def ListaEstado():
    gerald = goku()
   
    idx = input("digite el vivo, muerto o indefinido para ver los personajes segun su estado: ")
    gerald = goku.select().where(goku.estado == idx).get()

    for gerald in goku.select():

        if idx == gerald.estado:
            print("=================================================")
            print(f"Nombre: {gerald.nombre} \n Apellido: {gerald.apellido} \n serie: {gerald.serie} \n Estado: {gerald.estado}")
            print("=================================================")
    
    
    fda = input("Precione 1 para salir: ")
    if fda == "1":
        return False

def ModificarSeries():
    cls()
    print("Lista de series: \n")
    print("=================================================")
    for gerald in goku.select(): 
        print(f" serie: {gerald.serie}  ")
        print("=================================================")
    fda = input("Precione 1 para salir o digite la serie a modificar: ")
    if fda == "1":
        return False
    gerald = goku.select().where(goku.serie == fda).get()
    
    gerald.serie = confirmarDato("Serie",str(gerald.serie))    
    gerald.save()

    input("Registro modificado, precione enter para continuar ")

def EliminarSerie():
    cls()
    print("Series agregadas ")
    for gerald in goku.select(): 
        print(f" serie: {gerald.serie}  ")
        print("=================================================")
    
    idx = input("Digite la serie que desea eliminar o precione 1 para salir: ")
    if idx == "1":
        return False

    gerald = goku.select().where(goku.serie == idx).get()    
    input(f"La serie: {gerald.serie} esta borrado, presione enter para continuar ")
    gerald.delete_instance()

def AgregarSerie():
    cls()
    gerald = goku()
    for gerald in goku.select(): 
        print(f" {gerald.serie} ")
        print("=================================================")
    
    fda = input("Digite el nombre de la serie a agregar: ")
    gerald.serie = fda
    gerald.save()
    if fda == "1":
        return False

    input(f"La serie {gerald.serie} esta agregada, precione enter para salir")

def Estados():
    cls()
    print("Lista de estados: \n")
    print("=================================================")
    for gerald in goku.select(): 
        print(f" El personaje: {gerald.nombre} esta {gerald.estado} ")
        print("=================================================")
    fda = input("Precione 1 para salir o digite el nombre del personaje a modificar: ")
    if fda == "1":
        return False
    gerald = goku.select().where(goku.nombre == fda).get()
    
    gerald.estado = confirmarDato("Estado",gerald.estado)    
    gerald.save()

    input("Registro modificado, precione enter para continuar ")

def Genero():
    cls()
    print("Lista de Genero: \n")
    print("=================================================")
    for gerald in goku.select(): 
        print(f" El personaje: {gerald.nombre} es {gerald.sexo} ")
        print("=================================================")

    idx = input("Precione 1 para salir o digite el nombre del personaje a modificar: ")
    gerald = goku.select().where(goku.nombre == idx).get()
    
    if idx == "1":
        return False
    
    gerald.sexo= confirmarDato("Genero",gerald.sexo)    
    gerald.save()

    input("Se ha modificado un registro, precione enter para continuar ")

def Localization():
    gerald = goku()
    fm = folium.Map(location=[36.208424, 138.252924],zoom_start=8,titles = "anime.html")

    for gerald in  goku.select():
        folium.Marker(location=[gerald.latitud,gerald.longitud], tooltip="Click me", popup=f'Nombre:  {gerald.nombre}  Apellido:  {gerald.apellido}  Edad:  {gerald.edad}  Poder:{gerald.poder} Sexo: {gerald.sexo} ').add_to(fm)
     
    fm.save("mapa.html")
    webbrowser.open('mapa.html')

def AcercaDe():
    opt = input("A-Para ver el video del desarrollador, B-para salir: ")

    if opt == "A" or opt == "a":
        webbrowser.open('https://youtu.be/eweV4HqK8jQ')
    if opt == "B" or opt == "b":
        return False
    else:
        print("Digite una opcion valida")