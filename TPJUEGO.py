import os
import random
import colorama 
from colorama import init, Fore
init(autoreset=True)

def Funcion_Presentacion()->str:
    '''Cambio las I de la presentacion del juego'''
    from colorama import init, Fore, Back
    init(autoreset=True)

    cambio_I:str =(Fore.RED + 'I')
    cambio_enven:str =(Fore.WHITE + 'enven')
    cambio_doaljuego:str = (Fore.WHITE + 'do al juego!')
    cambio_estospal:str = (Fore.WHITE + 'Estos Pal')
    cambio_tos_son:str = (Fore.WHITE + 'tos Son Un Ch')
    cambio_no:str = (Fore.WHITE + 'no')



    presentacion:str = (f'                                           ¡B{cambio_I}{cambio_enven}{cambio_I}{cambio_doaljuego}')

    presentacion_2: str = (f'                                         {cambio_estospal}{cambio_I}{cambio_tos_son}{cambio_I}{cambio_no}')
    
 
    print(presentacion)
    print(presentacion_2)
    return presentacion and presentacion_2
def ingresar_opcion_de_menu(opciones: list[str]) -> int:
    """funcion para organizar el menu con las opciones correspondientes"""

    print('\nOpciones válidas: \n')

    for x in range(len(opciones)):
        print(f'{x + 1} - {opciones[x]}')

    entrada: str = input('\nIngrese una opción: ')
    if entrada.isnumeric():
        opcion: int = int(entrada)
    else:
        opcion:int = 4
        os.system('cls')
    return opcion
def ingresar_numero_jugadores(jugadores)->int:

    '''validar la cantidad de jugadores entre 6 y 10'''
    validar_jugadores:bool = True
    
    while validar_jugadores == True:
        jugadores:str = input('\ningresar numero de jugadores (min 6 y max 10):  ')
        if jugadores.isnumeric():
            jugadores = int(jugadores)  
            if jugadores > 5 and jugadores <= 10  :              
               validar_jugadores = False
            else:
               os.system('cls') 
               print('ingrese una opcion valida')
               validar_jugadores = True
        else:
            os.system('cls') 
            print('por favor solo ingrese numeros')
            validar_jugadores = True       
    return jugadores
def eleccion_palito_del_usuario(eleccion_fila_jugador:int,eleccion_palito_a_sacar:int )-> list:
    ''' el usuario elige la fila y el palito para sacar de la piramide.
        Retorna los dos enteros que corresponden a la filay el palito'''
    eleccion_fila_jugador:str= input('\n   ingrese la fila del palito que desea sacar: ')
    eleccion_palito_a_sacar:str = input('\n   ingrese el palito a sacar contando de izquiera a derecha a partir del "-" :')
    
    
    if eleccion_fila_jugador.isnumeric() and eleccion_palito_a_sacar.isnumeric():
        eleccion_fila_jugador:int = int(eleccion_fila_jugador)
        eleccion_palito_a_sacar:int = int(eleccion_palito_a_sacar)
        eleccion_fila_jugador -= 1
        if eleccion_fila_jugador == 0:
            eleccion_palito_a_sacar += 6
        elif eleccion_fila_jugador == 1:
            eleccion_palito_a_sacar += 5

        elif eleccion_fila_jugador == 2:
            eleccion_palito_a_sacar += 4

        elif eleccion_fila_jugador == 3:
            eleccion_palito_a_sacar += 4

        elif eleccion_fila_jugador == 4:               #sumo a la columna el valor determinado para que se quite el palito en el lugar indicado por el usuario
            eleccion_palito_a_sacar += 3

        elif eleccion_fila_jugador == 5:
            eleccion_palito_a_sacar += 3

        elif eleccion_fila_jugador == 6:
            eleccion_palito_a_sacar += 2

        elif eleccion_fila_jugador == 7:
            eleccion_palito_a_sacar += 2

        elif eleccion_fila_jugador == 8:
            eleccion_palito_a_sacar +=1

        elif eleccion_fila_jugador == 9:
            eleccion_palito_a_sacar += 1

        elif eleccion_fila_jugador == 10:
            eleccion_palito_a_sacar += 1

        elif eleccion_fila_jugador == 11:
            eleccion_palito_a_sacar +=1

        elif eleccion_fila_jugador == 12:
            eleccion_palito_a_sacar += 0
        else:
            print('\ningrese una opcion valida')  
    else:
        print('\ningrese uns opcion valida')    
        eleccion_fila_jugador = 0
        eleccion_palito_a_sacar = 3    
        
    
   

    return eleccion_fila_jugador, eleccion_palito_a_sacar
def funcion_piramide()->list :
    '''imprimir en pantalla la piramide inicial con todos los palitos, tanto blancos como rojos.
    Retorna la lista con la pirámide'''
    print('\n\n\n      ¡Que comience el juego!    \n\n\n    ')
     
    piramide:list[str] = [['1-         ',' ',' ',' ',' ',' ','- ','I ','-',' ',' ',' ',' ',' ',''], 
                             ['2-         ',' ',' ',' ',' ','- ','I ','I ','-',' ',' ',' ',' ',''], 
                              ['3-         ',' ',' ',' ','- ','I ','I ','I ','-',' ',' ',' ',' ',''], 
                            ['4-        ',' ',' ',' ','- ','I ','I ','I ','I ','-',' ',' ',' ',''], 
                             ['5-        ',' ',' ','- ','I ','I ','I ','I ','I ','-',' ',' ',' ',''], 
                            ['6-       ',' ',' ','- ','I ','I ','I ','I ','I ','I ','-',' ',' ',''], 
                              ['7-       ',' ','- ','I ','I ','I ','I ','I ','I ','I ','-',' ',' ',''], 
                             ['8-      ',' ','- ','I ','I ','I ','I ','I ','I ','I ','I ','-',' ',''], 
                               ['9-      ','- ','I ','I ','I ','I ','I ','I ','I ','I ','I ','-',' ',''],
                              ['10-    ','- ','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','-',''],
                                ['11-   - ','','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','-',''], 
                               ['12-  - ','','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','I ','-',''] ,
                               ['', '', '', '', '', '', '', '','', '', '', '' ]]
    
    jugadores = int
    jugadores:int = ingresar_numero_jugadores(jugadores)    
    numero_filas:int = jugadores + 2    
    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE    
    cantidad_palitos_rojos:int = (((jugadores + 2) * (jugadores + 3)) / 2 ) // 4
    contador:bool = 0
    while contador < cantidad_palitos_rojos:
       fila_palito_rojo = random.randrange(0, jugadores + 2)
       columna_palito_rojo = random.randrange(1, jugadores + 2)

   
       if (piramide[fila_palito_rojo][columna_palito_rojo] != ' ' and 
          piramide[fila_palito_rojo][columna_palito_rojo] != '- ' and 
          piramide[fila_palito_rojo][columna_palito_rojo] != '-'):
          piramide[fila_palito_rojo][columna_palito_rojo] = palito_rojo
          contador += 1      
    piramide = piramide[0:numero_filas]
    
    for filas in piramide[0:numero_filas]:
               ''.join(filas)
      
    return piramide
def funcion_turno(piramide_original:list, perdiste_turno:int, palitos_sacados_usuario:list, palitos_sacados_ia:dict)-> list:
   '''se ingresa a lista con la piramide original para que el usuario la modifique. 
   Tambien un valor para reconocer si el usuario habia perdido el turno anteriormente.}
   Retorna la piramide modificada por el usuario, un entero y una lista con los palitos que saca el usuario.'''
   
   palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE 
   piramide_modificada:list = piramide_original
   turno_contador:int = 0
   perdiste_turno:int = perdiste_turno
   contador_palitos_rojo:int = 0
   eleccion_fila_jugador = 0
   eleccion_palito_a_sacar = 0
   jugador_perdedor = None
   palitos:list  = contar_palitos(piramide_modificada)
   palitos_totales:int = palitos[0] + palitos[1]
   palitos_sacados_usuario:list = palitos_sacados_usuario
   jugador:str = 'usuario'
   if perdiste_turno != 1:                       # condicion para saber si el jugador puede jugar normalmente su turno
        while turno_contador < 3 :  
            os.system('cls')                                                       
            for fila in piramide_modificada[0:]:
                print(''.join(fila))
                           
            eleccion_fila_jugador, eleccion_palito_a_sacar  = eleccion_palito_del_usuario(eleccion_fila_jugador, eleccion_palito_a_sacar )

           
            if eleccion_fila_jugador == 0 and eleccion_palito_a_sacar == 3 and palitos_totales > 0 :                     #valores random que use para verificar si el jugador no habia elegido numeros enteros
                print('\n     no existe ningun palito en esa posicion. ingrese otra vez un nuevo valor     \n')     
                turno_contador = turno_contador
            else:                 
                if piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] != '  ' :
                    palitos:list  = contar_palitos(piramide_modificada)
                    palitos_totales:int = palitos[0] + palitos[1]
                    if (piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] != ' ' and
                        piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] == 'I ' and 
                        piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] != '-'):                               
                        piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] = '  ' #reemplazo de palitos blancos                           
                        turno_contador += 1
                        palitos_sacados_usuario[0] += 1
                        palitos:list  = contar_palitos(piramide_modificada)
                        palitos_totales:int = palitos[0] + palitos[1]
                        if palitos_totales < 1 :
                            jugador_perdedor = 1

                    elif ( piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] != ' ' and                                   
                        piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] != '-'): 
                            palitos:list  = contar_palitos(piramide_modificada)
                            palitos_totales:int = palitos[0] + palitos[1]
                            piramide_modificada[eleccion_fila_jugador][eleccion_palito_a_sacar] = '  ' 
                            palitos_sacados_usuario[0] += 1
                            if palitos_totales < 1 :
                                jugador_perdedor = 1
                                turno_contador = 99                                                                       #reemplazo de palitos rojos
                            print('\n   sacaste un palito rojo!    \n')
                            turno_contador += 1
                            if contador_palitos_rojo < 1 :   
                                contador_palitos_rojo += 1                         
                                dado:int = random.randrange (1,6)
                                input('   presione enter para tirar el dado.\n')
                                print(f'   !sacaste el numero  {dado}!\n')            #aca comienzan a funcionar los eventos                               
                                if dado == 1 :                              
                                    perdiste_turno = 1                                   
                                    print('   !Perdiste el próximo turno!\n')
                                elif dado == 2:
                                    piramide_modificada = evento_2(piramide_modificada)                                                                  
                                elif dado == 3:                                        
                                    piramide_modificada = evento_4(piramide_modificada)                                      
                                    os.system('cls')
                                    for fila in piramide_modificada[0:]:
                                            print(''.join(fila))
                                    print('\n             ¡Sacaste una fila!')
                                elif dado == 4:
                                    filas_piramide = len(piramide_modificada)  #saco el numero de filas para saber cuanto fue la cantidad inicial de palitos
                                    piramide_modificada = evento_5(piramide_modificada, filas_piramide) #genero una nueva piramide                                  
                                    os.system('cls')
                                    print(f'        el dado cayó en el número {dado}  \n')
                                    print('\n        se ha reiniciado la piramide!')
                                    for fila in piramide_modificada[0:]:
                                            print(''.join(fila))
                                elif dado == 5:
                                    print('\n        sacaste el numero 6, no sucede nada! ')
                                else:
                                    
                                    contador_palitos_rojo += 1
                    if palitos_totales < 1 :
                        jugador_perdedor = 'Usuario'
                        turno_contador = 99
                        
                    if turno_contador < 3 and jugador_perdedor is None:
                        continuar_sacando = input('\n   seguir sacando palitos? si/no  :  ')
                        if continuar_sacando.lower() == 'no' :                 
                                turno_contador = 3
    
                        else:
                            turno_contador = turno_contador                                                 
                if jugador_perdedor is not None:
                    print(f'\n      El jugador {jugador_perdedor} ha perdido el juego al retirar el último palito.\n')
                    print('                  FIN DE LA PARTIDA\n')
                    print(f'el usuario saco {palitos_sacados_usuario[0]} palitos en total.')
                    comparar_ganador_palitos(palitos_sacados_ia, palitos_sacados_usuario)
    
                    for jugador, palitos in palitos_sacados_ia.items():
                        print(f"\nel jugador {jugador} sacó {palitos} palitos en total")

                    
                    input('\npresiona enter para volver al menu principal') 
                    turno_contador = 99   
   else:     
        os.system('cls')         
        perdiste_turno = 0                       
        movimiento_palitos_piramide(piramide_modificada)
        print('\nTurno perdido')
        input('presione enter para ver el siguiente turno')
      
   return piramide_modificada, perdiste_turno, palitos_sacados_usuario
def funcion_turnoIA(piramide_modificada:list, ia_que_pierde_turno:list, palitos_sacados_ia: dict, palitos_sacados_usuario:list)->None:
    '''se ingresa la lista con la piramide, en donde la misma mediante un while se modifica la misma de manera aleatoria, 
        dependiendo de la cantidad de jugadores.
         Retorna la piramide modificada por los jugadores, una lista con los jugadores que pierden su proximo turno y un diccionario con los palitos que sacan los jugadores. '''
    
    piramide_modificada_ia:list = piramide_modificada
    turnos_jugadores_ia:int= len(piramide_modificada_ia) - 3
    turnos_restantes:int = 0
    ia_que_pierde_turno:list[int] = ia_que_pierde_turno
    jugador_perdedor = None
    palitos_sacados_ia: dict = palitos_sacados_ia
    palitos_sacados_usuario:list = palitos_sacados_usuario
    while turnos_restantes < turnos_jugadores_ia :
        jugador = turnos_restantes + 1
        if turnos_restantes not in ia_que_pierde_turno:
            turno_contador = 0
            contador_palitos_rojos: int = 0     
            os.system('cls')                           #limpio la consola justo antes del print de la piramide
            print('turno del contrincante....\n')       
            for fila in piramide_modificada_ia[0:]:
                print(''.join(fila))    
            print(f'\n  ↑↑↑   turno del jugador  {turnos_restantes + 1}   ↑↑↑\n')
            while turno_contador < 3 :
                    eleccion_fila_ia:int = random.randrange (0, len(piramide_modificada_ia))
                    eleccion_palito_ia:int  = random.randrange (1, len(piramide_modificada_ia)) 
                    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE
                    
                    if (
                        piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] != ' ' and
                        piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] != '  ' and
                        piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] != '-' and
                        piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] != '- '
                        ):
                        if  piramide_modificada[eleccion_fila_ia][eleccion_palito_ia] == 'I ' :     #me fijo si la eleccion es un palito comun                  
                            piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] = '  '
                            turno_contador += 1
                            piramide_modificada_ia:list = movimiento_palitos_piramide(piramide_modificada_ia)
                            palitos:list = contar_palitos(piramide_modificada_ia)
                            palitos_totales:int = palitos[0] + palitos[1]
                            palitos_sacados_ia = recuento_de_palitos(jugador, palitos_sacados_ia)
                        if (piramide_modificada[eleccion_fila_ia][eleccion_palito_ia] != 'I ' and piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] != '  '
                           ) :                                                                                                                                   #me fijo si la eleccion es un palito rojo
                        
                            palitos:list  = contar_palitos(piramide_modificada)
                            palitos_totales:int = palitos[0] + palitos[1]
                            turno_contador += 1
                            piramide_modificada_ia:list = movimiento_palitos_piramide(piramide_modificada_ia)
                            piramide_modificada_ia[eleccion_fila_ia][eleccion_palito_ia] = '  '     #reemplazo de palitos rojos
                            palitos_sacados_ia = recuento_de_palitos(jugador, palitos_sacados_ia)
                            print(f'\n     ¡el jugador {turnos_restantes + 1} saco un palito rojo!   \n')
                            palitos:list = contar_palitos(piramide_modificada_ia)
                            palitos_totales:int = palitos[0] + palitos[1]
                            if contador_palitos_rojos < 1  :
                                if palitos_totales > 1:
                                        contador_palitos_rojos += 1                           
                                        dado:int = random.randrange(1,6)
                                        print(f'        el dado cayó en el número {dado}  \n')
                                        if dado == 1 :                               
                                            ia_que_pierde_turno.append(turnos_restantes)                                       
                                            print(f'     ¡El jugador {turnos_restantes + 1} perdio el proximo turno!\n')
                                        elif dado == 2:
                                            evento_2(piramide_modificada_ia)                                             
                                            print(f'        ¡el jugador {turnos_restantes + 1} agrega mas palitos!\n')                                       
                                        elif dado == 3:                                           
                                            piramide_modificada_ia = evento_4_ia(piramide_modificada_ia)                                           
                                            
                                            os.system('cls')
                                            for fila in piramide_modificada_ia[0:]:
                                                print(''.join(fila))           
                                            print('\n               ¡BOMBA!')                                                                   
                                            print(f' \n     ¡el jugador {turnos_restantes + 1} retiro una fila!')
                                        elif dado == 4:
                                            filas_piramide = len(piramide_modificada_ia)
                                            piramide_modificada_ia = evento_5(piramide_modificada_ia, filas_piramide)                                   
                                            os.system('cls')
                                            print(f'        el dado cayó en el número {dado}  \n')
                                            print('\n       !Se ha reiniciado la piramide!      \n')
                                            for fila in piramide_modificada_ia[0:]:                                                 
                                                  print(''.join(fila))
                                            print('\n')
                                        elif dado == 4:
                                            print('           ¡no sucede nada!\n')   
                                        else:                                           
                                            contador_palitos_rojos += 1
                                else:
                                     jugador_perdedor = turnos_restantes + 1
                                     turno_contador = 99
                                     turnos_restantes = 99          
                            
                        if palitos_totales < 1:
                            jugador_perdedor = turnos_restantes + 1
                            
                            turno_contador = 99
                            turnos_restantes = 99
                            
                        if turno_contador < 3:
                            turno_contador += random.randrange(0,2)         
                    else:
                            turno_contador:int = turno_contador 
                              
            input('presione enter para ver el siguiente turno')      
            turnos_restantes  += 1   
            palitos:list = contar_palitos(piramide_modificada_ia)
            palitos_totales:int = palitos[0] + palitos[1]
        else:
            turnos_restantes  += 1
            ia_que_pierde_turno = ia_que_pierde_turno[1::]
    if jugador_perdedor is not None:
        os.system('cls')
        print(f'!El jugador {jugador_perdedor} ha perdido el juego al retirar el último palito¡\n')
        print('                    \n         FIN DE LA PARTIDA\n')       
        comparar_ganador_palitos(palitos_sacados_ia, palitos_sacados_usuario)
        print(f"el usuario sacó {palitos_sacados_usuario[0]} palitos en total.\n")
        for jugador, palitos in palitos_sacados_ia.items():
            print(f"el jugador {jugador} Sacó {palitos} palitos en total.\n")
            
            
        input('\npresione cualquier tecla para volver al menu principal')
    else:       
        print(f'\n         ¡aún quedan {palitos_totales} palitos!')
       
        
    
    return piramide_modificada_ia, ia_que_pierde_turno, palitos_sacados_ia   
def contar_palitos(piramide:list) -> list[int]  :
    ''' se le debe introducir la lista de la piramide: guarda la cantidad de palitos en una lista, 
            en donde [0] es la cantidad de palitos blancos y [1] la cantidad de palitos rojos.
                                     Retorna una lista de enteros'''
    contador:int = 0
    contador_rojo:int = 0
    
    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE
    for fila in piramide:
        for palito in fila:
            if palito == 'I ' : 
                contador += 1
            elif palito == palito_rojo  :
                contador_rojo += 1 
    
    contador_total:list = [contador, contador_rojo]

    return contador_total
def contar_espacios_vacios(piramide:list) -> int:
    '''ingresar la lista con la piramide para evaluar la cantidad de espacios que reemplazaron a los palitos.
                                              Retorna un entero'''
    lugares_vacios:int = 0
    for fila in piramide:
        for palito in fila:
            if palito == '  ' : 
                lugares_vacios += 1
            else :
                lugares_vacios = lugares_vacios
    
    return lugares_vacios
def movimiento_palitos_piramide(piramide_modificada: list) -> list:
    '''se ingresa la lista con la piramide dentro para que sea reorganizada, luego de la funcion, ésta es modificada moviendo los palitos hacia arriba
    para que siga conservando la forma. Retorna la piramide modificada'''
    contador:int  = 0
    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE   
    while contador < 12: 
    
            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):    
                        if (
                            piramide_modificada[fila][palito] == 'I ' and
                            piramide_modificada[fila - 1][palito] == '  ' and
                            piramide_modificada[fila - 1][palito] != '-' and
                            piramide_modificada[fila - 1][palito] != palito_rojo and
                            piramide_modificada[fila - 1][palito] != '- '
                            ):
                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito] = 'I '

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):        
                        if (
                            piramide_modificada[fila][palito] == 'I ' and
                            piramide_modificada[fila - 1][palito + 1] == '  ' and
                            piramide_modificada[fila - 1][palito + 1] != '-' and
                            piramide_modificada[fila - 1][palito + 1] != palito_rojo and
                            piramide_modificada[fila - 1][palito + 1] != '- '
                            ):
                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito + 1] = 'I '

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):        
                        if (
                            piramide_modificada[fila][palito] == 'I ' and
                            piramide_modificada[fila][palito + 1] == '  ' and
                            piramide_modificada[fila][palito + 1] != '-' and
                            piramide_modificada[fila][palito + 1] != palito_rojo and
                            piramide_modificada[fila][palito + 1] != '- '
                            ):

                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila ][palito + 1] = 'I '

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):      
                        if (
                            piramide_modificada[fila][palito] == 'I ' and
                            piramide_modificada[fila - 1][palito - 1] == '  ' and
                            piramide_modificada[fila - 1][palito - 1] != '-' and
                            piramide_modificada[fila - 1][palito - 1] != palito_rojo and
                            piramide_modificada[fila - 1][palito - 1] != '- '
                            ):

                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito - 1] = 'I '

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):     
                        if (
                            piramide_modificada[fila][palito] == 'I ' and
                            piramide_modificada[fila ][palito -1] == '  ' and
                            piramide_modificada[fila][palito - 1] != '-' and
                            piramide_modificada[fila][palito - 1] != palito_rojo and
                            piramide_modificada[fila][palito - 1] != '- ' 
                            ):
                            
                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila ][palito - 1] = 'I '
            
            #palitos comunes

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):       
                        if (
                            piramide_modificada[fila][palito] == palito_rojo and
                            piramide_modificada[fila - 1][palito] == '  ' and
                            piramide_modificada[fila - 1][palito] != '-' and
                            piramide_modificada[fila - 1][palito ] != 'I ' and
                            piramide_modificada[fila - 1][palito] != '- '
                            ):
                            
                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito] = palito_rojo

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):    
                        if (
                            piramide_modificada[fila][palito] == palito_rojo and
                            piramide_modificada[fila - 1][palito + 1] == '  ' and
                            piramide_modificada[fila - 1][palito + 1] != '-' and
                            piramide_modificada[fila- 1][palito + 1] != 'I ' and
                            piramide_modificada[fila - 1][palito + 1] != '- '
                            ):

                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito + 1] = palito_rojo

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):    
                        if (
                            piramide_modificada[fila][palito] == palito_rojo and
                            piramide_modificada[fila][palito + 1] == '  ' and
                            piramide_modificada[fila][palito + 1] != '-' and
                            piramide_modificada[fila][palito + 1] != 'I ' and
                            piramide_modificada[fila][palito + 1] != '- '
                            ):
                            
                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila][palito + 1] = palito_rojo

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):    
                        if (
                            piramide_modificada[fila][palito] == palito_rojo and
                            piramide_modificada[fila - 1][palito -1] == '  ' and
                            piramide_modificada[fila - 1][palito - 1] != '-' and
                            piramide_modificada[fila - 1][palito -1] != 'I ' and
                            piramide_modificada[fila - 1][palito - 1] != '- '
                            ):

                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila - 1][palito - 1] = palito_rojo

            for fila in range(len(piramide_modificada) ):
                for palito in range(len(piramide_modificada[fila])):
                    if (
                        0 <= fila - 1 < len(piramide_modificada) and
                        0 <= palito + 1 < len(piramide_modificada[fila - 1])  
                        ):    
                        if (
                            piramide_modificada[fila][palito] == palito_rojo and
                            piramide_modificada[fila][palito -1] == '  ' and
                            piramide_modificada[fila][palito - 1] != '-' and
                            piramide_modificada[fila ][palito -1] != 'I ' and
                            piramide_modificada[fila][palito - 1] != '- '
                            ):

                            piramide_modificada[fila][palito] = '  '
                            piramide_modificada[fila][palito - 1] = palito_rojo
                                
            #palitos rojos
            contador += 1
          
    return piramide_modificada
def evento_2(piramide: list) -> list:
    '''ingresar la lista con la piramide, se cuentan la cantidad de espacios en blanco mas los palitos para ver la cantidad maxima a agregar.
                                    luego se reemplazan los espacios en blanco por palitos comunes.
                                                 Retorna la piramide modificada'''
    palitos_parciales = contar_palitos(piramide)
    palitos_totales = palitos_parciales[0] + palitos_parciales[1]
    lugares_vacios = contar_espacios_vacios(piramide)
    maximos_palitos_a_agregar = palitos_totales + lugares_vacios
    
    contador = 0

    filas = len(piramide)
    palitos_por_fila = len(piramide[0])
    if lugares_vacios != 0 :
        palitos_a_agregar = random.randrange(0, lugares_vacios)
        while contador < palitos_a_agregar:
            fila = random.randrange(filas)
            palito = random.randrange(palitos_por_fila)

            if fila < len(piramide) and palito < len(piramide[fila]) and piramide[fila][palito] == '  ':
                piramide[fila][palito] = 'I '
                contador += 1
    else: 
        print('no se pueden agregar mas palitos')
    
    return piramide
def evento_4(piramide:list)-> list:
    '''ingresa la lista con la piramide para que el usuario elija que fila reemplazar en la misma. 
     Retorna la piramide modificada'''
    
    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE 
    evento = True
    while evento == True:
        print('\n      ¡BOMBA!')
        fila_seleccionada:str = input('\ningrese la fila que quiere retirar:  ') 
        if fila_seleccionada.isnumeric() :
            fila_seleccionada = int(fila_seleccionada) - 1
            
            if 0 <= fila_seleccionada < len(piramide):
                # Elimina todos los palitos de la fila seleccionada
                for palito in range(len(piramide[fila_seleccionada])):
                    if  piramide[fila_seleccionada][palito] == 'I ' or  piramide[fila_seleccionada][palito] == palito_rojo :
                        piramide[fila_seleccionada][palito] = '  '
                        print(f'     ¡sacaste la fila {fila_seleccionada}!')
                        evento = False
            else:
                os.system('cls')
                print('elegi una fila valida')
        else:   
            os.system('cls')  
            print('elegi una fila valida') 
            evento = True   
    return piramide
def evento_4_ia(piramide:list)-> list:   
    ''' se ingresa la lista con la piramide para que de manera aleatoria se retire una fila.
                                Retorna la piramide modificada'''
    palitos:list = contar_palitos(piramide)
    palitos_totales:int = palitos[0] + palitos [1]
    if palitos_totales >= 2 :
        fila_seleccionada:int = random.randrange (1, len(piramide))
        palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE 
        if 0 <= fila_seleccionada < len(piramide):
            # Elimina todos los palitos de la fila seleccionada
            for palito in range(len(piramide[fila_seleccionada])):
                if  piramide[fila_seleccionada][palito] == 'I ' or  piramide[fila_seleccionada][palito] == palito_rojo :
                    piramide[fila_seleccionada][palito] = '  '
                    print(f'¡Retiro la fila {fila_seleccionada + 1}!')
    else:
        print('!solo queda un palito!')
    return piramide    
def evento_5(piramide:list, filas_piramide:int) ->list :
    
    '''muestra en pantalla la piramide inicial con todos los palitos, tanto blancos como rojos'''
    
    
   
    
    jugadores:int =  filas_piramide - 2  
    
    for fila in range(len(piramide))   :
        for palito in range(len(piramide[fila]))  :
            if (piramide[fila][palito] == '  '):     #genero de nuevo la piramide
                    piramide[fila][palito] = 'I '
    palitos = contar_palitos(piramide)
    palitos_rojos_parciales:int = palitos[1]                #palitos rojos que hay en la piramide actualmente
    palito_rojo:str = Fore.RED + 'I ' + Fore.WHITE    
    cantidad_original_palitos_rojos:int = (((jugadores + 2) * (jugadores + 3)) / 2 ) // 4
    contador:int = 0
    palitos_rojos_a_agregar = cantidad_original_palitos_rojos - palitos_rojos_parciales
    while contador < palitos_rojos_a_agregar:                 
        fila_palito_rojo = random.randrange(0, jugadores + 2)
        columna_palito_rojo = random.randrange(1, jugadores + 2)

    
        if (piramide[fila_palito_rojo][columna_palito_rojo] != ' ' and 
            piramide[fila_palito_rojo][columna_palito_rojo] != '- ' and 
            piramide[fila_palito_rojo][columna_palito_rojo] != '-'):
            piramide[fila_palito_rojo][columna_palito_rojo] = palito_rojo         # agrego la cantidad de palitos rojos correspondientes
            contador += 1      
        piramide = piramide[0:filas_piramide]
        
        for filas in piramide[0:filas_piramide]:
                ''.join(filas)
      
    return piramide
def recuento_de_palitos(jugador_actual:int, palitos_sacados:dict) -> list:
    ''' Ingresa un entero que correponde al numero de jugador,  con un diccionario que
        agrega como clave el entero y suma la cantidad de palitos que saca ese jugador '''
    if jugador_actual not in palitos_sacados:
         palitos_sacados[jugador_actual] = 0
    else:
         palitos_sacados[jugador_actual] += 1
    return palitos_sacados
def comparar_ganador_palitos(palitos_sacados_ia:dict, palitos_sacados_usuario:list) -> None:
    '''Ingresa un diccionario con una lista, compara los jugadores del diccionario con los palitos que sacaron para 
    saber el que saco más, y luego lo compara con el número entero que guarda la lista con los palitos del usuario.
    Muestra en pantalla el jugador que saco mas palitos'''
    jugador_max_palitos = None
    max_palitos = 0

    for jugador, palitos in palitos_sacados_ia.items():
        if palitos > max_palitos:
            max_palitos = palitos
            jugador_max_palitos = jugador
        elif palitos == max_palitos and max_palitos > palitos_sacados_usuario[0]:
            print('¡Hubo un empate en la cantidad de palitos sacados!\n')
            jugador_max_palitos = None
        # Comparar los resultados
    if jugador_max_palitos is not None:
        if max_palitos > palitos_sacados_usuario[0]:
            print(f'\n¡EL JUGADOR {jugador_max_palitos} SACÓ MÁS PALITOS QUE TODOS!\n')
        elif max_palitos < palitos_sacados_usuario[0]:
            print(f'\n¡Felicidades! ¡Fuiste el jugador que sacó más palitos!\n')
       
    return
def main() -> None:
    
  programa_proceso:bool = True
  piramide:list = []   
  while  programa_proceso == True :
         presentacion = Funcion_Presentacion()
         opciones:tuple = (
     'comenzar el juego',
     'reglas',
     'salir'
     )
         opcion:int = ingresar_opcion_de_menu(opciones)


         if opcion == 1:
            os.system('cls')
            juego_en_proceso: bool = True          
            piramide:list = funcion_piramide()
            numero_jugadores = len(piramide) - 2
            palitos:list = contar_palitos(piramide)
            turno_perdido = 0
            cantidad_inicial_palitos:int = palitos[0] + palitos[1]
            ia_que_pierde_turno:list = []
            palitos_sacados_ia:dict = {}
            palitos_sacados_usuario:list = [0]
            #bucle para poder ir repitiendo los turnos
            while  juego_en_proceso == True:
               
                piramide_modificada, turno_perdido, palitos_sacados_usuario = funcion_turno(piramide, turno_perdido, palitos_sacados_usuario, palitos_sacados_ia) 
                palitos:list = contar_palitos(piramide_modificada)
                palitos_totales:int = palitos[0] + palitos[1]
                if palitos_totales < 1:
                    
                    juego_en_proceso = False
                    os.system('cls')
                    programa_proceso = True
                else:               
                    piramide_modificada_ia, ia_que_pierde_turno, palitos_sacados_ia  = funcion_turnoIA(piramide_modificada, ia_que_pierde_turno, palitos_sacados_ia, palitos_sacados_usuario)  

                  
                palitos:list = contar_palitos(piramide_modificada_ia)
                palitos_totales:int = palitos[0] + palitos[1]
                juego_en_proceso = True
                if palitos_totales < 1:
                    
                    juego_en_proceso = False
                    os.system('cls')
                    programa_proceso = True
                else:
                    programa_proceso = True
         elif opcion == 2:
            print(' El juego consiste en una pirámide de palitos de tamaño variable, y cantidad de jugador variable. ')
            print(' En su turno, cada jugador podrá elegir entre 1 a 3 palitos que desee retirar, y retirarlos de lamisma.')
            print(' El jugador que retire el último palito pierde.')
            print(' Entre los palitos, encontraremos siempre algunos de color rojo, que al retirarse, producirán un evento aleatorio.')
            print(' En caso de retirar másde un palito rojo en el mismo turno, ocurrirá solo un evento')
            print(' Al retirar “palito rojo”, se tira un dado y en base al valor entre 1 y 6 se ejecuta un evento')
            print('1) El jugador pierde su próximo turno.')
            print('2) Se agregan entre 1 y M palitos, en caso de no poder agregarse a totalidad, se agrega elmáximo que se pueda (no superar cantidad inicial de palitos')
            print('3) Se bloquean/congelan el 20% de los palitos (en el caso que el valor sea < 1 entonces se toma 1 palito) , durante 3 turnos los jugadores no podrán retirarlos.')
            print('4) Bomba: el jugador debe retirar una fila completa a su elección.')
            print('5) Nueva pirámide: se genera una nueva pirámide, del mismo tamaño que la original.')
            print('6) No hace nada')
            salir_reglas:str = input('\n\npresione cualquier tecla para volver al menu principal  ')
            if salir_reglas != '':
                 programa_proceso = True    
         elif opcion == 3:
            
            programa_proceso = False
         else:
            print('\n ingrese una opcion valida')
            programa_proceso = True
            
  print('gracias por jugar!')      

   
main()