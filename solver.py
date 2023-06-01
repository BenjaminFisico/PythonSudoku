import numpy as np

"""
    -- Este módulo es un complemento de sudoku.py y tabCreator.py --

    Contiene los metodos para:
        - Analizar si el sudoku esta resuelto - - - - - - - - - - - - - - - -> validateSol(args):
        - Verificar si colocar un número en determinada casilla es correcto -> isPosible(args):
        - Resolver de forma automatica el sudoku- - - - - - - - - - - - - - -> solve(args):
"""

def validateSol(tablero):
    """
        Valida si el tablero de sudoku esta resuelto.
        Lo que significa que en cada fila, columna y subcuadro de 3x3 se repite ningún número.
        En cuando esa regla no se cumple para alguna de las secciones mencionadas, entonces se corta la ejecucion devolviendo False.

        Args:
            - tablero (ndarray): matriz 9x9 que contiene cada casilla a validar

        Returns:
            - (True): El algoritmo llego hasta el final por lo tanto el sudoku esta resuelto.
            - (False): El sudoku no esta resuelto.
    """
    for y in range(0,9):
        #-- Verificar si en cada fila no se repite ningún número y no hay ·
        fila = np.unique(tablero[y])
        if np.shape(fila)[0] == 9:
            if '·' in fila:
                return False
        else:
            return False
        #-- Verificar si en cada columna no se repite ningún número y no hay ·
        colum = np.unique(tablero[:,y])
        if np.shape(colum)[0] == 9:
            if '·' in colum:
                return False
        else:
            return False
    
    #-- Verificar que en cada subCuadro no se repite ningún número y no hay ·
    for y in range(0,3):
        for x in range(0,3):
            subCuadro = []
            for i in range(y*3,y*3+3):
                for j in range(x*3,x*3+3):
                    subCuadro.append(tablero[i,j])
            subCuadro = np.unique(subCuadro)
            if np.shape(subCuadro)[0] == 9:
                if '·' in subCuadro:
                    return False
            else:
                return False
    
    #-- Si la ejecución llega a este punto significa que el sudoku esta resuelto.
    return True
    

def isPosible(tablero,fil,col,num):
    """ Valida si colocar determinado número en determinada casilla ayuda a resolver el sudoku.
        Es decir que ese número no esta, ni en esa fila, ni en esa columna, ni en ese subcuadro.

        Args:
            - tablero (ndarray): Matriz 9x9 que contiene todas las casillas del sudoku.
            - fil         (int): Índice de la fila donde se encuentra la casilla a verificar.
            - col         (int): Índice de la columna donde se encuentra la casilla a verificar.
            - num     (str/int): Número que se quiere verificar.

        Returns:
            - (True): Si el número no se repite.
            - (False): Si el número ya se encuentra. 
    """
    fila = tablero[fil]
    colum = tablero[:,col]
    #-- Recoger el subcuadro al que pertenece la casilla seleccionada
    subCuadro = []
    sbCy = (fil//3)*3
    sbCx = (col//3)*3
    for i in range(sbCy,sbCy+3):
        for j in range(sbCx,sbCx+3):
            subCuadro.append(tablero[i,j])

    num = str(num)
    if (num not in fila) and (num not in colum) and (num not in subCuadro):
        return True
    
    return False

def solve(tablero):
    """ Busca una posible solución para el sudoku dado.
        -Este metodo es recursivo y utiliza la fuerza bruta para encontrar la dicha solución.
        -El algoritmo va casilla por casilla probando si es posible poner cada número,
         en el momento en que encuentra que poner un número en una casilla es posible, pasa a la siguiente.
         Si en una casilla se recorren los números posibles(del 1 al 9) sin que ningúno sea posible entonces
         significa que el número correcto para dicha casilla ya fue colocado en una de las anteriores,
         por lo tanto regresa y verifica si en una de las casillas anteriores es posible poner otro número.
         Si en ningúna de las casillas anteriores es posible poner otro número entonces el sudoku no tiene solución.
        -Este metodo aprobecha el metodo isPosible(): que se encuentra en este mismo módulo.
        -El hecho de que este algoritmo use la fuerza bruta implica que dependiendo de la forma del problema,
         va a tardar o mucho o muy poco en resolver el sudoku.

        Args:
            - tablero (ndarray): matriz 9x9 que contiene el sudoku a resolver.
              ¡ADVERTENCIA!: el tablero pasado por parametro es modificado, 
              es decir: este álgoritmo no te dice si el sudoku puede ser resuelto, directamente lo resuelve.

        Returns:
            - (True): En caso de que se haya solucionado el sudoku.
            - (False): En caso de que No se haya encontrado la solución.
    """
    # Por cada llamado recorre absolutamente todas las casillas.
    for i in range(9):
        for j in range(9):
            if tablero[i,j] == '·':
                for r in range(1,10):
                    #Intentar insertar r en [i,j]
                    if isPosible(tablero,i,j,r):
                        tablero[i,j] = str(r)
                        #Aquí el backtraking guarda el estado actual del tablero.
                        if solve(tablero):
                            return True
                        else:
                            tablero[i,j] = '·'
                #Backtraking 
                return False
    # Solucionado
    return True
