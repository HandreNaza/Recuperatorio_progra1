from funciones import *
#https://onlinegdb.com/wbCZ0OhZZ

def ejecutar_menu():
    matriz_cocinero = inicializar_matriz(5,4,0) 
    bandera_cocinero = False
    while (True):
            print("Ingrese un número para continuar:\n"
            "1 Cargar Cocineros\n"
            "2 Mostrar Cocineros con Votos de Jurados\n"
            "3 Ordenar Cocineros Por mejor Nota Promedio\n"
            "4 Muestro Peores 3 notas promedio \n"
            "5 Muestro Cocineros que superen promedio\n"
            "6 Jurado malo\n"
            "7 Sumatoria (la suma de su nota iguala al número ingresado) entre 3 y 300\n"
            "8 Definir Ganador\n"
            "9 salir")
            opcion = pedir_num("Debe ingrsar una Opcion entre 1 y 8: ","Opcion invalida ingrese números entre 1-8\nSu opcion: ",1,9)
            if opcion == 1:  
                  #hardcodear_datos(matriz_cocinero)
                  cargo_notas(matriz_cocinero)
                  bandera_cocinero = True
            if opcion == 2:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")
                  else: 
                       muestro_matriz(matriz_cocinero)
                  pass
            elif opcion == 3:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                      print("Muestro en orden de Promedio Descendiente")
                      ordenar_matriz_promedio(matriz_cocinero)
                  pass
            elif opcion == 4:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                      mostrar_peores(matriz_cocinero)
                  pass
            elif opcion == 5:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                      muestro_supera_promedio(matriz_cocinero)
                  pass
            elif opcion == 6:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                       promedio_jurados(matriz_cocinero)
                  pass
                  
            elif opcion == 7:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                       sumo_notas_comparo(matriz_cocinero)
                  pass
                  
            elif opcion == 8:
                  if bandera_cocinero == False:
                      print("debe cargar Datos los datos para continuar")

                  else:
                       elijo_ganador(matriz_cocinero)
                  pass
                
            elif opcion == 9:
                 print("Saliendo...")
                 break
            limpiar_consola()
ejecutar_menu()

