
nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina']

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def creacion_diccio():
    diccionario={}

    for i in range(len(nombres)):
        diccionario[nombres[i]]=notas_1[i],notas_2[i]

    return(diccionario)

def promedio_individual(diccionario): 
    promedios={}
    res=0
    for diccio in diccionario:
        for num in diccionario[diccio]:
            res+=num
        print(f'el promedio de {diccio} es: {res/2}')
        promedios[diccio]=res/2
        res=0
    return(promedios)

def promedio_general(promedios):
    total=0
    for promedio in promedios:
        total+=promedios[promedio]
    prom=total/len(promedios)
    print(f'el promedio total es: {prom}')
    return (prom)

def promedio_mas_alto(promedios):
    clave=max(promedios, key=promedios.get)
    print(f'el estudiante con el promedio mas alto es: {clave} con un promedio de: {promedios[clave]}')
    
def promedio_mas_bajo(promedios):
    clave=min(promedios, key=promedios.get)
    print(f'el estudiante con el promedio mas bajo es: {clave} con un promedio de: {promedios[clave]}')

d=creacion_diccio()
p=promedio_individual(d)
promedio_general(p)
promedio_mas_alto(p)
promedio_mas_bajo(p)

