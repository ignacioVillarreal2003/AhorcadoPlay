import random

peliculas = [
    'El Padrino',
    'Titanic',
    'Pulp Fiction',
    'El Señor de los Anillos: La Comunidad del Anillo',
    'La La Land',
    'Matrix',
    'Coco',
    'Forrest Gump',
    'Avatar',
    'Star Wars: Episodio IV - Una nueva esperanza',
    'Jurassic Park',
    'El Rey León',
    'Gladiador',
    'Inception',
    'Harry Potter y la piedra filosofal',
    'Casablanca',
    'El Silencio de los Corderos',
    'E.T. El Extraterrestre',
    'The Shawshank Redemption',
    'Blade Runner'
]

peliculaAleatoria = peliculas[random.randint(0,len(peliculas))].lower()
errores = 6
letrasUsadas = []

def jugar():
    global errores
    while errores > 0:
        palabra = imprimirPalabra()
        if ('_' not in palabra):
            print(f'Juego completado\nGracias por jugar.\nLa pelicula era {peliculaAleatoria}')
            return
        print('Pelicula: ', palabra)
        letra = input('Ingrese una letra: ').lower()
        if letra in letrasUsadas:
            print(f'La letra {letra} ya a sido usada')
        elif letra not in peliculaAleatoria:
            errores -= 1
            print(f'La letra {letra} no esta. Quedan {errores} intentos.')
        if letra not in letrasUsadas:
            letrasUsadas.append(letra)
            print('Letras usadas: ', letrasUsadas)
        print('----------------------------------')


def imprimirPalabra():
    palabraOculta = ""
    for i in peliculaAleatoria:
        if i in letrasUsadas:
            palabraOculta += i
        elif (i == " "):
            palabraOculta += " "
        else:
            palabraOculta += "_"
    return palabraOculta

jugar()