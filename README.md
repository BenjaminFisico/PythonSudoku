# PythonSudoku
Simple sudoku in Python with numpy library // Un sudoku simple en Python, utilizando la libreria numpy

![imagen de muestra](https://github.com/BenjaminFisico/PythonSudoku/assets/42160409/f94e31f7-ceb7-4331-83f6-d94f0d368403)


<h1>¿Por qué? </h1>
Mi objetivo principal con este proyecto era el de aprender a manejar mejor la libreria Numpy de Python.
Sin embargo creo que el sudoku representa un problema interesante que todo programador tendria que resolver al menos una vez en la vida.<br>Dado que las reglas del sudoku nos dicen que no se puede repetir ningún número, en ninguna fila, ni en ninguna columna, ni en ningún subcuadro de tres por tres, por lógica, nos obliga a manejar de diferentes formas las listas o en este caso matrices.<br>
Por ultimo diseñar un álgoritmo que sea capaz de resolver el sudoku de forma automatica es un reto interesante para los novatos, de hecho cuando empece a diseñar el programa me pase varios días tratando de encontrar el susodicho álgoritmo, y no voy a mentir finalmente lo tuve que buscar por Google, porque en un principio yo estaba pensando en álgoritmos que no usen la fuerza bruta.
Claramente es algo muy complejo, por eso finalmente me quede con el que usa todo el mundo, el álgoritmo de backtraking.
<h1>¿Como funciona?</h1>
Para jugar al sudoku se debe abrir una terminal del sistema y ejecutar el comando "py sudoku.py" desde el directorio en el que se encuentre dicho archivo.
El funcionamiento de cada método esta detallado en la documentación de los mismos.
Lo que puedo decir aca es que el archivo sudoku.py contiene un loop en el que se ejecuta toda la logica del juego aprobechando los otros dos módulos. 
Dentro de ese loop primero se imprime el tablero con los valores actuales, luego se verifica si el sudoku esta resuelto y finalmente se le pide al usuario que ingrese algo, siendo que hasta ahora se han programado las siguientes funciones:<br>
1- Colocar un nuevo número en una casilla modificable. Esto se hace ingresando tres números seguidos y separados por un espacio.<br>
   El primer número hace referencia a la fila en la que se encuentra la casilla a modificar.<br>
	 El segundo número hace referencia a la columna en la que se encuentra la casilla a modificar. <br>
	 El tercer número es el nuevo número a ingresar.<br>
2- Solucionar: ejecuta el algoritmo que resuelve el sudoku.<br>
3- Reiniciar: reinicia el sudoku, creando uno nuevo.<br>
4- help/ayuda: ver la información de ayuda.
<h1>Experiencia personal </h1>
Lo más bueno que me llevo de este pequeño proyecto es que me esmere en documentarlo bien, lo tome como una buena practica de documentación de código, aunque siempre se recomiende documentar en ingles, en este caso quise sentirme libre de expresarme en mi lengua materna. (tambíen porque me lleva menos tiempo).
<h1> Futuro </h1>
Para el futuro de este proyecto me gustaria:<br>
-> Crear un álgoritmo que construya sudokus unicos, teniendo en cuenta el nivel de dificultad. Si bien actualmente ya hice un álgoritmo de creación de sudokus, el mismo no regula de forma fiel la dificultad y se rige totalmente por las fuerzas de la aleatoriedad.<br>
-> Integrar el sudoku a un archivo html para visualizarlo en el navegador y volverlo mas didactico, aunque esto implicaria que varias de las cosas que ya hice aqui queden obsoletas.<br>
-> Como en sudoku.com incluir una opción que de una pista sobre como resolver una casilla del actual sudoku.
