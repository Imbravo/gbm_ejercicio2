Autor: Jesus Ponte
Fecha: 12/09/2023

El problema está dividido en dos funciones:
1)unit_testing, la cual recibe por parametros un string del directorio donde se encuentran las pruebas unitarias,
y el formato del nombre de las pruebas unitarias que siguen el siguiente ejemplo: 'unit_test_1.txt'.
Esta función se encarga de leer cada una de las pruebas unitarias, obtiene linea por linea los valores de las carreras.
Como paso a paso:
-Obtiene g, como el numero de carreras y p, como el numero de pilotos.
-Lee las siguientes g lineas que representan carreas y las asigna a una lista
-Obtiene los s sistemas de puntaje
-Obtiene las siguientes s lineas que representan los puntos
-separa k y el sistema, y los transforma en un int y una lista.
-Llama a la funcion calc_points, pasandole por parametro la lista de carreras, el numero K de llegadas a evaluar y el
sistema de puntaje.
-Guarda el resultado en un archivo de texto con el formato 'unit_test_*_result.txt' donde * corresponde al numero de prueba
unitaria.

2) calc_points, recibe por parametros la lista de carreras, el numero K de llegadas a evaluar y el
sistema de puntaje.
-Se crea un diccionario donde se almacenan los puntos de cada piloto.
-Para cada carrera y cada piloto en la carrera se actualizan sus puntos correspondientes con el sistema de puntaje.
-Se utiliza max y list comprehension para obtener el maximo o los empates.
-Devolvemos la lista de los puntajes como un string con el formato correcto.

Nota: Se puede agregar una apertura de los documentos 'unit_test_*_result.txt' para hacer una limpieza de las respuestas.
Para no sobreescribir los documentos se pueden eliminar para que se generen al momento de correr el programa.