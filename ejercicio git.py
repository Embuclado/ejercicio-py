libros = [
    ['Papelucho programador', 'Marcela Paz', 1983],
    ['Don Python de la Mancha', 'Miguel de Cervantes', 1615],
    ['Raw_input y Julieta', 'William Shakespeare', 1597],
    ['La tuplamorfosis', 'Franz Kafka', 1915]
    # ...
]

datos_autores = {
    # autor: nacimiento, defuncion, idioma
    'William Shakespeare': [[1564,  4, 26], [1616,  5,  3], 'inglés'],
    'Franz Kafka':         [[1883,  7,  3], [1924,  6,  3], 'alemán'],
    'Marcela Paz':         [[1902,  2, 28], [1985,  6, 12], 'español'],
    'Miguel de Cervantes': [[1547,  9, 29], [1616,  4, 22], 'español']
    # ...
}
def obtener_idioma(titulo):
    for i in libros:
        if i[0] == titulo:
            autor = i[1] 
    for autores in datos_autores:
        if autores == autor:
            idioma = datos_autores[autores][2]
            return idioma
def obtener_autor(titulo):
    for i in libros:
        if i[0] == titulo:
            autor = i[1]
            return autor 
def calcular_annos_antes_de_morir(titulo):
    for autores in datos_autores:
        autor = obtener_autor(titulo)
        if autores == autor:
            fallecimiento = datos_autores[autores][1][0]
    for i in libros:
        if i[0] == titulo:
                fecha = i[2]
                años_escrito_libro = fallecimiento - fecha
                return años_escrito_libro 

titulo = input('Ingrese titulo del libro: ')
print('El libro fue escrito en', obtener_idioma(titulo))
print('por', obtener_autor(titulo))
print('El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años')
print('después de haber escrito el libro')
