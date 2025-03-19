# attached-python
Programa de cómputo y formato de resultados de Test de Apego en Adultos.

## Requisitos
- `python`, versión 3.6+.

## Ejecución
El script toma como argumento el nombre del usuario a quién se le toma el test.
Si no se indica dicho argumento, lo consulta de forma interactiva.

Posterior a esto, se deberá suplir la respuesta del usuario una a la vez, la
cual deberá ser un número entero entre 1 y 6, para que después el programa
escriba un archivo tipo csv con el número de pregunta, el factor de apego que
evalúa dicha pregunta y la respuesta del usuario que fue suministrada en el
paso anterior. Dicho archivo puede ser abierto en cualquier editor de hojas de
cálculo que soporte el formato de MS Excel (xlsx).

## TODO
De momento, no está completa la funcionalidad para computar los resultados del
test. Eventualmente, el script tomará los resultados presentes en el archivo
csv del usuario y calculará el resultado, dando el tipo de apego que
corresponde a las respuestas del usuario.
