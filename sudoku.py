import os
from os import system
import re
import numpy as np

import tabCreator
import solver

""" ┌───────────────────────────────────┐
    │ Codigo creado por Benjamin Fisico:│
    │ https://github.com/BenjaminFisico │
    └───────────────────────────────────┘  """

def clearScreen():
    """ Limpia la pantalla de la terminal en la que se este ejecutando el programa """
    if os.name == "nt":
        system("cls")
    else:
        system("clear")

def insertInBoard(fil,col,num):
    """ Inserta un número dado y en las cordenadas dadas del tablero (tab)
    
        Args:
            fil (int): Número de la fila en la que se quiere insertar
            col (int): Número de la columna en la que se quiere insertar
            num (int): Número a insertar
    """
    if (0 < fil < 10) and (0 < col < 10) and (0 < num < 10):
        fil -= 1
        col -= 1
        # En tabInicial las casillas que no son un · son inmodificables
        if tabInicial[fil,col] == "·":
            tab[fil,col] = str(num)
        else:
            print(" Esa casilla esta bloqueada ")
            input()
    else:
        print(" Los números deben estar entre 1 y 9 inclusive")
        input()

def printBoard(tablero):
    """ Imprime por pantalla un tablero 9x9
        con la forma de un sudoku.
        Incluye números de referencia para las filas y las columnas.
        - Ejemplo: 
        ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐
        │x│1│2│3│4│5│6│7│8│9│
        ├─┼─┴─┴─┼─┴─┴─┼─┴─┴─┤
        │1│· · ·│· · ·│· · ·│

        Args:
            - tablero (ndarray): tablero a visualizar en pantalla
    """
    print(" \033[1;30;47m"+"┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐")
    print(" │x│1│2│3│4│5│6│7│8│9│")
    print(" ├─┼─┴─┴─┼─┴─┴─┼─┴─┴─┤")
    for y in range(0,9):
        print("\033[1;30;47m"+f" │{y+1}│",end="")
        for x in range(0,9):
            if tabInicial[y,x] == '·':
                print("\033[1;31m"+f"{tablero[y,x]}",end="")
            else:
                print("\033[;36;47m"+f"{tablero[y,x]}",end="")

            if x == 2 or x == 5 or x == 8:
                print("\033[1;30;47m"+"│",end="")
            else:
                print(" ",end="")

        print("")
        if y == 2 or y == 5:
            print(" ├─┼─────┼─────┼─────┤")

    print("\033[1;30;47m"+" \033[1;30;47m"+"└─┴─────┴─────┴─────┘")

# --- GAMELOOP ---
tabInicial = tabCreator.generateProblem()
tab = np.array(tabInicial)
user_input = ""

while user_input != "exit":
    # -- Impresion por pantalla
    clearScreen()
    print("SUDOKU BY BENJAMIN FISICO")
    printBoard(tab)

    # -- Analiza si el sudoku esta resuelto
    if solver.validateSol(tab):
        # Verificar si la solución la encontro el usuario o el algoritmo
        if np.array_equal(tabInicial,tab):
            print("El algoritmo a completado el sudoku")
            print("No te desanimes la proxima vez podras lograrlo")
        else:
            print("HAS COMPLETADO EL SUDOKU :D")
            print("     FELICITACIONES      ")
        print("Ingresa 'reiniciar' si quieres volver a jugar")
    
    # -- Input del usuario
    print("¡Ingresa 'help' o 'ayuda' para ver la informacion de ayuda!")
    user_input = input("\033[0;0;0m" + "Digite un número -> ")
    user_input = user_input.lower()
    input_int = re.split(r'\s',user_input)
    
    # -- El usuario ingreso tres números
    if len(input_int) == 3 and (input_int[0].isdigit() and input_int[1].isdigit() and input_int[2].isdigit()):
        insertInBoard(int(input_int[0]),int(input_int[1]),int(input_int[2]))
    
    # -- El usuario ingreso solucionar
    if input_int[0] == "solucionar":
        if solver.solve(tabInicial):
            print("Solucionado!")
        else:
            print("Hubo un problema! No tiene solución :(")
        input()
        tab = tabInicial

    # -- El usuario ingreso reiniciar
    if input_int[0] == "reiniciar":
        tabInicial = tabCreator.generateProblem()
        tab = np.array(tabInicial)

    # -- El usuario ingreso help o ayuda
    if input_int[0] == "help" or input_int[0] == "ayuda":
        print("- Bienvenido a la ayuda del Sudoku By Benjamin Fisico -")
        print("1. El tablero de sudoku esta compuesto por una matriz de 9x9")
        print("     -En dicho tablero se pueden observar números de color celeste que son inmodificables")
        print("     y números rojos que son los colocados por el usuario.")
        print("     -En la parte superior hay una serie de números que van del 1 al 9 y señalan las diferentes columnas del tablero.")
        print("     -Asi mismo a la izquierda del tablero hay otra serie de números que tambien van del 1 al 9 y señalan las diferentes filas del tablero.")
        print("2. Para colocar un número en una casilla simplemente debes ingresar: ")
        print("     -Tres números enteros mayores que 0 y menores que 10 ")
        print("     -Los tres números deben estar uno atras del otro y separados por un espacio ")
        print("     -El primer número corresponde a la fila en la que se quiere colocar un número, ")
        print("     el segundo a la columna y el tercero es el nuevo número a colocar.")
        print("     -Por ejemplo: 5 7 3 coloca el número 3 donde se cruzan la fila 5 y la columna 7")
        print("3. Ingresa 'solucionar' para que el algoritmo de backtraking resuelva el sudoku ")
        print("4. Ingresa 'reiniciar' para empezar un nuevo sudoku")

        input("--- Preciona [ ENTER ] para continuar ---")
