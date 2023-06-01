import numpy as np
import random
import solver

"""
   --- MÓDULO para sudoku.py ---

    Contiene los metodos para:
        - Crear un nuevo tablero vacio - - - - - - - - -> createBoard():
        - Desordenar de forma aleatorea una lista dada -> randomLst(Args):
        - Generar un nuevo sudoku- - - - - - - - - - - -> generateProblem():
    
"""

def createBoard():
    """ Crea una matriz de 9x9 disque vacia 
        - cada casilla contiene '·' lo que en la logica de este sudoku significa vacio.

        Returns:
            tab (ndarray): matriz 9x9 con el tablero creado.
    """
    tab = np.array([["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"]])
    tab = np.concatenate((tab,tab))
    tab = np.concatenate((tab,[["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"]]))
    return tab

def randomLst(list_a):
    """ Desordena de forma aleatoria una lista dada, sin modificar su contenido.
        - Solo acepta listas de una dimensión.

        Args:
            - list_a (array): lista a desordenar.

        Returns:
            - rndList (array): Nueva lista con la lista anterior desordenada.
    
    """
    list = list_a[:]
    rndList = []
    
    # Este mismo proceso podia hacerse solo usando numpy de la siguiente forma:
    #    1. rnd = numpy.random.choice(list)
    #    2. rndList.append(rnd)
    #    3. list = np.delete(list,np.where(list == rnd)[0])
    # Esa habia sido mi primera opción pero por alguna razon falla en la primer vuelta duplicando un índice.

    while len(list) != 0:
        rnd = random.randint(0,len(list)-1)
        rndList.append(list[rnd])
        list = np.delete(list,rnd)

    return rndList

def generateProblem(celdasVacias = 50):
    """ Genera un nuevo sudoku aleatorio.
        -Este álgoritmo es de invención propia por lo que no aseguro que sea el mas eficiente,
         simplemente quise agregar la suficiente aleatoriedad sin que genere sudokus imposibles de resolver.
        -El proceso consiste en:
         1. Crear una fila aleatoria para los números superiores del tablero.
         2. Crear una fila aleatoria en la que ningún índice es igual al de la fila creada anteriormente, 
            esta corresponde a los números inferiores del tablero.
         3. Crear números aleatoreos que iran en la primer columna.
         4. Resolver el "sudoku" generado hasta ahora, esto implica que se puede "tardar mucho" en generar el problema.
         5. Transformar x celdas vacias en el sudoku ya resuelto. 
        -Aprobecho el método randomLst(): para generar filas aleatorias.
        -Otro método usado es isPosible(): del modulo solver.
        -También se hace uso del método solve(): presente en el módulo solver.

        Args:
            - celdasVacias (int): Representa la cantidad de celdas vacias en el sudoku, siendo 64 el maximo recomendado.

        Returns:
            - tab (ndarray): Matriz 9x9 que contiene el sudoku creado.    
    """
    #-- Fila superior
    print("Creando números superiores...")
    tab = np.array([randomLst(['1','2','3','4','5','6','7','8','9'])])
    
    #-- Crear filas intermedias vacias
    filasVacia = np.array([["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"],["·","·","·","·","·","·","·","·","·"]])
    tab = np.concatenate((tab,filasVacia))

    #-- Fila inferior
    print("Creando números inferiores...")
    distin = False
    #Este proceso se repite hasta que se cumpla la condición indicada abajo.
    while distin == False:
        rndaux = randomLst(['1','2','3','4','5','6','7','8','9'])
        distin = True
        #En ningún índice la fila inferior puede ser igual a la fila superior porque eso romperia el sudoku.
        for i in range(9):
            if tab[0,i] == rndaux[i]:
                distin = False
                break
    tab = np.concatenate((tab,[rndaux]))
    
    #-- Primer columna
    print("Aleatorizando números intermedios...")
    nueva = ["1","2","3","4","5","6","7","8","9"]
    i = len(nueva)-1
    #Como la columna comparte un número con la fila superior y otro con la inferior hay que eliminar dichos numeros de esta columna.
    while i >= 0:
        if nueva[i] == tab[0,0]:
            nueva = np.delete(nueva,i)
            i -= 1
            continue

        if nueva[i] == rndaux[0]:
            nueva = np.delete(nueva,i)

        i -= 1
    
    nueva = randomLst(nueva)
    i = 0
    #Se debe asegurar que la insercion de esta columna no viole las reglas del sudoku. 
    while i < len(nueva):
        if solver.isPosible(tab,i+1,0,nueva[i]):
            i +=1
        else:
            nueva = randomLst(nueva)
            i = 0

    for i in range(7):
        tab[i+1,0] = nueva[i]

    print("Buscando posible solucion... esto puede tardar...")
    if solver.solve(tab):
        print("Solucion encontrada!")
        print("Blanqueando casillas...")
        i = 0
        while i <= celdasVacias:
            y = random.randint(0,8)
            x = random.randint(0,8)
            if tab[y,x] != "·":
                tab[y,x] = "·"
                i +=1
    else:
        #En caso de no encontrar la solución al sudoku se vuelve a llamar a esta misma funcion de forma recursiva 
        # hasta generar uno que sea posible resolver. Hasta ahora esto nunca me paso pero por las dudas deje esta porción de código. 
        print("Solucion no encontrada :(")
        print("Reiniciando proceso")
        tab = generateProblem()

    return tab