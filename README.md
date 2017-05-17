# Analísis de Poesía [ES]
Un analizador de poesía basado en Python.

## Versiones

[A1.0.0] >>Añadido<< Creación de un vector que represente un poema mediante métricas de sintaxis.

[B1.0.0] >>Añadido<< Identificador del patrón de rima mediante enumeración.

[A1.0.1] >>Modificación<< Cambio en el vector de representación: Ahora el vector de representación del poema es unidimensional.

[B1.1.0] >>Modificación<< Cambio en el patrón de rima: En vez de un vector númerico utiliza un vector booleano de donde surge una nueva métrica.

[V4.0.0] >>Modificación<< Unificación de las dos aproximaciones A y B.

[V4.0.1] >>Modificación<< Reestructuración del código: Optimización del código, mayor legibilidad, más pitonico.

[V4.1.0] >>Añadido<< Implementación de un vector universal.

[V4.2.0] >>Añadido<< Matriz indicativa para visualizar las métricas realizadas.

[V4.3.0] >>Añadido<< Tres (3) métodos de comparación.

[V4.4.0] >>Añadido<< El usuario es libre de elegir qué desea comparar.

[V4.5.0] >>Modificación<< Revisión del código, pruebas, código comentado, soporte en GitHub, versiones, changelog, readme y tópicos.

[V4.6.0] >>Añadido<< Manejo de datos de entrada erróneos.

[V4.7.0] >>Modificación<< Impresión de datos con formato. Separación entre procesos de análisis y comparación.

[V5.0.0] >>Añadido<< Reestructuración del proceso. Mediante el uso de un diccionario ahora el analisis es modular.

[V5.1.0] >>Añadido<< Tablas únicas de diferencia, formateado de salida y actualización de los comentarios del nuevo código.

[V5.1.1] >>Modificación<< Normalizada la rima.

[V5.1.2] >>Pruebas<< La similitud coseno no está mal: La diferencia computacional entre los dos métodos es mínima: 2x10^-16

[V5.1.3] >>Modificación<< Ahora todas las medidas están en distancia.

[V5.2.0] >>Modificación<< Pruebas de ploteado: Se descubrió un error en la aproximación hecha, se arregló este inconveniente.

[V5.3.0] >>Añadido<< Gráfica de variación de parámetro de rima vs Distancia coseno para un solo poema.

[V5.4.0] >>Añadido<< Nuevo modelo que permite calcular la grafica "Variación de parámetro de rima vs Distancia coseno" individual y para todo el corpus.

[V5.5.0] >>Añadido<< Método que plotea la rima original vs rima de la traducción de todo el corpus.

[V5.6.0] >>Añadido<< Implementado un algoritmo simple para centrar los plots y los intervalos automaticamente.

[V5.6.1] >>Pruebas<< Arreglados algunos bugs menores.

[V5.6.2] >>Modificación<< Código comentado, demos hechas y actualización en GitHub.

[5.6.3] >>Añadido<< Linea de referencia para la grafica "Rima original VS Rima traducción".

[5.6.4] >>Añadido<< Se asignan etiquetas para identificar cada punto de la gráfica "Rima original VS Rima traducción".

[5.6.5] >>Pruebas<< Comprobada el correcto funcionamiento de la grafica de "Rima Origen Vs Rima Traduccion".

[5.7.0] >>Pruebas<< Gráfica "Rima Origen Vs Rima Traduccion" hecha manualmente.

[5.7.1] >>Modificación<< La función para normalizar un vector ahora devuelve el vector en vez de sobreescribirlo.

[5.7.2] >>Modificación<< La función para contar parrafos ahora es independiente.

[5.7.3] >>Modificación<< Se separó la función para contar versos.

[5.7.4] >>Modificación<< Se separó la función para calcular la rima de un poema.

[5.7.5] >>Modificación<< Ahora el calculo del vector de un poema no se normaliza.

[5.8.0] >>Añadido<< Una función que permite calcular la rima promedio de un corpus.

[5.8.1] >>Modificación<< Separada la función que permita plotear "Parámetro de rima VS Rima promedio".

[5.8.2] >>Añadido<< Leyenda en la gráfica "Parámetro de rima VS Rima promedio".

[5.9.0] >>Añadido<< Sistema para calcular la rima de cada poema en el corpus, resultado: Una lista con la rima de todos los poemas original/traducidos.

[5.9.1] >>Modificación<< Separada la función de plotear "Rima original VS Rima traducción". El proceso se simplificó usando las nuevas funciones.

[5.10.0] >>Añadido<< Función para calcular la matriz de poemas (Anteriormente sólo se imprimia)

[5.11.0] >>Añadido<< Mediante el uso de palabras claves una única funcion puede obtener diferentes datos.

[5.11.1] >>Modificación<< Separado el metodo de listar el nombre de los poemas.

[5.12.0] >>Añadido<< Función para imprimir la matriz de poemas.

[5.13.0] >>Añadido<< Método que permite obtener la matriz de comparación (Anteriormente sólo imprimirla, sin guardar los datos)

[5.14.0] >>Añadido<< Método para imprimir unicamente los valores de la matriz de comparación (Este metodo se diseño exclusivamente para prueba)

[5.14.1] >>Modificación<< Mejorado el método para imprimir como texto la matrix de comparación. Ahora se ajusta automaticamente.

[6.0.0] >>Añadido<< Todo ha sido pasado a programacion funcional. El codigo está mejor estructurado. Código comentado y documentado.

Para ver las versiones, mire las [etiquetas en el repositorio](https://github.com/dfzunigah/Poetry-Analysis/releases)

# Poetry Analizer [EN]
A Python based poetry ananlysis.

## Versioning

[A1.0.0] >>Added<< Poem vector representation using syntax metrics.

[B1.0.0] >>Added<< Rhythm pattern identificator using numeric values.

[A1.0.1] >>Modification<< Poem vector repreentation is now unidimensional.

[B1.1.0] >>Modification<< Rhythm pattern identificator represented through boolean vector.

[V4.0.0] >>Modification<< Unification of approach A and B.

[V4.0.1] >>Modification<< Code re-writed: Optimization, better readability, Pythonic way.

[V4.1.0] >>Added<< Universal vector representation.

[V4.2.0] >>Added<< Matrix aid for metrics visualization.

[V4.3.0] >>Added<< Three (3) comparison methods.

[V4.4.0] >>Added<< User is now free to choose metrics to compare.

[V4.5.0] >>Modification<< Code revision, tests, documentation, GitHub support, versioning, changelog, readme and topics.

[V4.6.0] >>Added<< Input exceptions handling.

[V4.7.0] >>Modification<< Analysis and comparing are now independent processes. Data is not format-printed.

[V5.0.0] >>Added<< New aproach: Functional programming. Through a dictionary, analysis can be modular.

[V5.1.0] >>Added<< Difference comparison tables, output formated and code comments updated.

[V5.1.1] >>Modification<< Rhyme normalized.

[V5.1.2] >>Tests<< Cosine similitude isn't wrong: Computational difference in both methods implemented is 2x10^-16

[V5.1.3] >>Modification<< Now all comparison metrics are distances.

[V5.2.0] >>Modification<< Plotting tests: A bug was discovered in the model used. Problem now solved.

[V5.3.0] >>Added<< "Variation of rhyme parameter VS Cosine distance" graphics for a single poem.

[V5.4.0] >>Added<< New model allows to compute "Variation of rhyme parameter VS Cosine distance" graphics for individual poems and for full corpus.

[V5.5.0] >>Added<< Plot method for "Original Poem Rhyme Vs Translated Poem Rhyme" of full corpus.

[V5.6.0] >>Added<< Implemented a simple algorithm for centering and resizing plots automatically.

[V5.6.1] >>Tests<< Minor bugs fixed.

[V5.6.2] >>Modification<< Code commented, some demos, feed-back and GitHub update.

[5.6.3] >>Added<< Reference line to "Original Rhyme VS Traduction Rhyme" graphic.

[5.6.4] >>Added<< Each point in "Original Rhyme VS Traduction Rhyme" graphic is now identifiable.

[5.6.5] >>Tests<< Proper operation of "Original Rhyme VS Traduction Rhyme" graphic.

[5.7.0] >>Tests<< "Original Rhyme VS Traduction Rhyme" graphic made manually.

[5.7.1] >>Modification<< Normalize function now returns a value instead of overwriting last value.

[5.7.2] >>Modificationn<< Paragraph counting function is now independent.

[5.7.3] >>Modification<< Verse counting function is now separated.

[5.7.4] >>Modification<< Rhyme calculus function is now separated.

[5.7.5] >>Modification<< Vector representation not normalized.

[5.8.0] >>Added<< Rhyme Average in corpus function

[5.8.1] >>Modification<< "Rhyme Parameter VS Average Rhyme" plotting function is now independent.

[5.8.2] >>Added<< Legend to "Rhyme Parameter VS Average Rhyme" graphic.

[5.9.0] >>Added<< System to calculate each poem rhyme in the corpus, result: A list with the rhyme of all original/translated poems.

[5.9.1] >>Modification<< Plotting function "Rhyme Parameter VS Average Rhyme" is now independent. Process is now easier to do.

[5.10.0] >>Added<< Get poems matrix function (Previously it was a printing function)

[5.11.0] >>Added<< Through keywords, functions can now get different data.

[5.11.1] >>Modification<< Poem name listing method is now separated.

[5.12.0] >>Added<< Poems matrix printing function.

[5.13.0] >>Added<< Get matrix comparison method (Previously data wasn't saved, just printed)

[5.14.0] >>Added<< Comparison matrix printing method: Prints only the values (Function designed for testing)

[5.14.1] >>Modification<< Comparison matrix printing method improved.

[6.0.0] >>Added<< Functional programming implemented. Code is now documented. GitHub updated.

For the versions available, see the [tags on this repository](https://github.com/dfzunigah/Poetry-Analysis/releases).
