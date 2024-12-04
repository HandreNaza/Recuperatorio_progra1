import os
import random

COCINERO = 0
VOTO_J_UNO = 1
VOTO_J_DOS = 2
VOTO_J_TRES = 3



DESC = True
ASC = False


def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')

def pedir_num(mensaje:str, error:str, mini:int,maxi:int):
  num_ingresado = int(input(mensaje))

  while num_ingresado > maxi or num_ingresado < mini:
     num_ingresado = int(input(error))
  return num_ingresado

def pedir_numero_minimo(mensaje:str,mensaje_error:str,minimo:int) -> int:
    numero = int(input(mensaje))
    while numero < minimo:
        numero = int(input(mensaje_error))
    return numero


def inicializar_matriz(filas:int,columnas:int,valor_inicial:any)->list:
      matriz = []
      for i in range(filas):
          filas_aux = [valor_inicial] * columnas
          matriz += [filas_aux]
      return matriz

def hardcodear_datos(matriz_cocinero:list) -> None:
    cocinero = 1
    for i in range(len(matriz_cocinero)):
        matriz_cocinero[i][COCINERO] = cocinero
        matriz_cocinero[i][VOTO_J_UNO] = random.randint(1,100)
        matriz_cocinero[i][VOTO_J_DOS] = random.randint(1,100)
        matriz_cocinero[i][VOTO_J_TRES] = random.randint(1,100)
        cocinero += 1
    print("\nDatos hardcodeados con exito\n")



#PUNTO 1 -> Cargamos la matriz
def cargo_notas(matriz_cocinero:list) -> None:
    cocinero = 1
    for i in range(len(matriz_cocinero)):
        matriz_cocinero[i][COCINERO] = cocinero
        matriz_cocinero[i][VOTO_J_UNO] = pedir_num(f"Ingrese Voto jurado 1 participante {cocinero}:",f"Debe ser entre 1 y 100 \n Ingrese Voto jurado 1 participante {cocinero}: :",1,100)
        matriz_cocinero[i][VOTO_J_DOS] = pedir_num(f"Ingrese Voto jurado 2 participante {cocinero}:",f"Debe ser entre 1 y 100 \n Ingrese Voto jurado 2 participante {cocinero}: :",1,100)
        matriz_cocinero[i][VOTO_J_TRES] = pedir_num(f"Ingrese Voto jurado 3 participante {cocinero}:",f"Debe ser entre 1 y 100 \n Ingrese Voto jurado 3 participante {cocinero}: :",1,100)
        cocinero += 1
    print("\nDatos cargado con exito\n")

    return

#2 Muestro matriz con promedio

def muestro_matriz(matriz_cocinero:list) -> None:

    for i in range(len(matriz_cocinero)):
        print("Cocinero N° ",matriz_cocinero[i][COCINERO])
        print("Nota Jurado 1 :",matriz_cocinero[i][VOTO_J_UNO])
        print("Nota Jurado 2 :",matriz_cocinero[i][VOTO_J_DOS])
        print("Nota Jurado 3 :",matriz_cocinero[i][VOTO_J_TRES])
        print("Promedio de nota:",promedio_notas_fila(matriz_cocinero,i),"\n")
    return

#saco promedio
def promedio_notas_fila(matriz_cocinero:list,fila:int) -> int:
    promedio_notas = (matriz_cocinero[fila][VOTO_J_UNO] + matriz_cocinero[fila][VOTO_J_DOS] + matriz_cocinero[fila][VOTO_J_TRES]) // 3
    return promedio_notas

#3 ordeno matriz por promedio 

#Funcion ordenamiento
def ordenar_matriz(matriz_cocinero:list,criterio:bool)->bool:
    
    for fil_i in range(len(matriz_cocinero)-1):
        for fil_j in range(fil_i + 1,len(matriz_cocinero)):
            promedio_i = promedio_notas_fila(matriz_cocinero,fil_i)
            promedio_j = promedio_notas_fila(matriz_cocinero,fil_j)
            if (criterio == DESC and promedio_i < promedio_j) or (criterio == ASC and promedio_i > promedio_j):
                aux = matriz_cocinero[fil_i]
                matriz_cocinero[fil_i] = matriz_cocinero[fil_j]
                matriz_cocinero[fil_j] = aux

    return matriz_cocinero

#3.2 ordeno de mayor a menor
def ordenar_matriz_promedio(matriz_cocinero:list) -> list:
    
    ordenar_matriz(matriz_cocinero,DESC)   
               
    muestro_matriz(matriz_cocinero)

    return

#4 ordeno matriz por promedio 

def mostrar_peores(matriz_cocinero:list):
    
    ordenar_matriz(matriz_cocinero,ASC)           

    print("Los 3 Peores Promedios son:")

    for i in range(3):  # Intentamos acceder a los primeros 3 cocineros
        muestro_matriz([matriz_cocinero[i]])
        
    return

#5----------------------------------------------------------
def promedio_notas_totales(matriz_cocinero:list) -> None:
    suma_nota = 0
    for i in range(len(matriz_cocinero)):
        suma_nota += promedio_notas_fila(matriz_cocinero,i)

    promedio_total = suma_nota / len(matriz_cocinero)
    
    return round(promedio_total,2)


def muestro_supera_promedio(matriz_cocinero:list):
    promedio_total = promedio_notas_totales(matriz_cocinero)

    print(f"El promedio de notas totales es {promedio_total}")
    
    supero_promedio = False  # Variable para verificar si al menos un cocinero supera el promedio

    for i in range(len(matriz_cocinero)):
        if promedio_notas_fila(matriz_cocinero, i) > promedio_total:
            print(f"Supera el promedio")
            muestro_matriz([matriz_cocinero[i]])
            
            supero_promedio = True  # Si encontramos un cocinero que supera el promedio, cambiamos a True
    
    if supero_promedio == False:
        print("Ninguno superó el promedio")
    
    return
#6----------------------------------------------------
def promedio_jurados(matriz_cocinero:list):
    promedio_j_1 = 0
    promedio_j_2 = 0
    promedio_j_3 = 0
    
    for i in range(len(matriz_cocinero)):
            promedio_j_1 += matriz_cocinero[i][VOTO_J_UNO]
            promedio_j_2 += matriz_cocinero[i][VOTO_J_DOS]
            promedio_j_3 += matriz_cocinero[i][VOTO_J_TRES]

    t_promedio_j_1 = promedio_j_1 // len(matriz_cocinero)
    t_promedio_j_2 = promedio_j_2 // len(matriz_cocinero)
    t_promedio_j_3 = promedio_j_3 // len(matriz_cocinero)

    if t_promedio_j_1 < t_promedio_j_2 and t_promedio_j_1 < t_promedio_j_3:
        print(f"Jurado Uno fue el que Puso peores notas en promedio un total de :{t_promedio_j_1}")
       
    elif t_promedio_j_2 < t_promedio_j_1 and t_promedio_j_2 < t_promedio_j_3:
        print(f"Jurado Dos fue el que Puso peores notas en promedio un total de :{t_promedio_j_2}")

    else: 
        print(f"Jurado Tres fue el que Puso peores notas en promedio un total de :{t_promedio_j_3}")

  
#7-----------------------------------------------------------

#Sumo Notas
def sumo_notas(matriz_cocinero:list,fila:int) -> int:
    suma_notas = (matriz_cocinero[fila][VOTO_J_UNO] + matriz_cocinero[fila][VOTO_J_DOS] + matriz_cocinero[fila][VOTO_J_TRES])
    return suma_notas

#Sumo notas y comparo
def sumo_notas_comparo(matriz_cocinero:list) -> list:
     numero = pedir_num("Ingrese un Numero enre el 3 y 300: ","Error Debe ser entre 3 y 300 Ingrese num: ",3,300)
     supero_promedio = False  # Variable para verificar si al menos un cocinero supera el promedio
     for i in range(len(matriz_cocinero)):
        if sumo_notas(matriz_cocinero, i) == numero:
            print(f"Suma las notas iguales al {numero}")
            muestro_matriz([matriz_cocinero[i]])
            
            supero_promedio = True 
    
     if supero_promedio == False:
        print("Ninguno igualo el nuemro")
    
     return


#8-----------------------------------------------------------

def elijo_ganador(matriz_cocinero:list) -> list:
   
    ordenar_matriz(matriz_cocinero, DESC)            

    # Obtener el promedio del ganador (primera fila de la matriz ordenada)
    promedio_ganador = promedio_notas_fila(matriz_cocinero, 0)

    # Inicializar la lista de empates
    empates = [None] * len(matriz_cocinero)
    indice = 0 

    # Encontrar todas las filas que tengan el mismo promedio que el ganador
    for i in range(len(matriz_cocinero)):
        if promedio_notas_fila(matriz_cocinero, i) == promedio_ganador:
            empates[indice] = matriz_cocinero[i]  # Asignar directamente
            indice += 1

    # Reducir la lista
    empates = empates[:indice]
    if len(empates) == 1:  # Si solo hay un ganador
        print("El ganador es: ")
        muestro_matriz([matriz_cocinero[0]])  # Mostrar solo el primer cocinero (el ganador)

    elif len(empates) > 1:  # Si hay empate
       
        elejir_desempate(empates)
                
    return


#Hago desempate
def elejir_desempate(matriz_empate:list) -> list:
    print("Los cocineros empatados son")

    if len(matriz_empate) > 2:
        matriz_empate = matriz_empate[:2]

    muestro_matriz(matriz_empate)

    voto_jurado_uno = pedir_numero_minimo("Jurado Uno Ingrese el numero del participante: ","Error/Reingrese la cantidad de votos: (No puede ser negativo): ",0)
    voto_jurado_dos = pedir_numero_minimo("Jurado Dos Ingrese el numero del participante: ","Error/Reingrese la cantidad de votos: (No puede ser negativo): ",0)
    voto_jurado_tres = pedir_numero_minimo("Jurado Tres Ingrese el numero del participante: ","Error/Reingrese la cantidad de votos: (No puede ser negativo): ",0)
    
    if voto_jurado_uno == voto_jurado_dos or voto_jurado_uno == voto_jurado_tres:
        ganador = voto_jurado_uno
        
    elif voto_jurado_dos == voto_jurado_tres:
        ganador = voto_jurado_dos
    else:
        # sin acuerdo elegir aleatoriamente
        print("No hay acuerdo, el ganador se elige aleatoriamente.")
        ganador_aleatorio = random.randint(0, 1)
        print(f"El ganador es el cocinero: {matriz_empate[ganador_aleatorio][COCINERO]}")
        muestro_matriz([matriz_empate[ganador_aleatorio]])
        return
    
     #mostrar al ganador
    if ganador == matriz_empate[0][COCINERO]:
        print("El ganador es el cocinero:", matriz_empate[0][COCINERO])
        muestro_matriz([matriz_empate[0]])
    elif ganador == matriz_empate[1][COCINERO]:
        print("El ganador es el cocinero:", matriz_empate[1][COCINERO])
        muestro_matriz([matriz_empate[1]])

    return
    
    


 