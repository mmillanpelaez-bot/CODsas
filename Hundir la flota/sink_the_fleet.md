Diagramas de Flujo - Hundir la FlotaAsignatura: COD (DAM-1)A continuación se presentan los diagramas de flujo correspondientes a la lógica de la aplicación solicitada.1. Función queNavioEs(valor)Objetivo: Recibir un valor entero y devolver el nombre del navío correspondiente como cadena de texto.flowchart TD
    A([Inicio: queNavioEs]) --> B[/Entrada: valor/]
    B --> C{¿valor == 1?}
    C -- Sí --> D[Retornar 'Submarino']
    C -- No --> E{¿valor == 2?}
    E -- Sí --> F[Retornar 'Buque']
    E -- No --> G{¿valor == 4?}
    G -- Sí --> H[Retornar 'Portaaviones']
    G -- No --> I[Retornar 'Desconocido' o 'Agua']
    D --> Z([Fin])
    F --> Z
    H --> Z
    I --> Z
2. Función recorrerFila(fila)Objetivo: Recorrer una lista (fila), identificar si hay naves, imprimirlas y contar las partes encontradas.Nota: Se asume que esta función llama a queNavioEs y salidaPorPantalla según la descripción del enunciado.flowchart TD
    A([Inicio: recorrerFila]) --> B[/Entrada: fila/]
    B --> C[Inicializar: partes_encontradas = 0]
    C --> D[Inicializar: indice = 0]
    
    D --> E{¿indice < longitud de fila?}
    E -- No (Fin del bucle) --> K[Retornar partes_encontradas]
    K --> L([Fin])
    
    E -- Sí --> F[Obtener valor = fila[indice]]
    F --> G{¿Es navío?}
    G -- No (Es 0) --> J[Incrementar indice]
    
    G -- Sí (1, 2 o 4) --> H[nombre = queNavioEs<valor>]
    H --> I[Llamar salidaPorPantalla<br>con coordenada e info]
    I --> M[partes_encontradas = partes_encontradas + 1]
    M --> J
    
    J --> E
Nota sobre esNavio: En el diagrama, la decisión "¿Es navío?" corresponde a la función auxiliar mencionada en la tabla esNavio(valor) que devuelve True si el valor no es 0.3. Función recorrerTablero(tablero)Objetivo: Iterar sobre la matriz principal, delegar el procesamiento de cada fila y acumular el total global.flowchart TD
    A([Inicio: recorrerTablero]) --> B[/Entrada: tablero/]
    B --> C[Inicializar: total_naves = 0]
    C --> D[Inicializar: i = 0]
    
    D --> E{¿i < longitud de tablero?}
    E -- No (Fin recorrido) --> K[Retornar total_naves]
    K --> L([Fin])
    
    E -- Sí --> F[Obtener fila_actual = tablero[i]]
    F --> G[subtotal = llamar recorrerFila<fila_actual>]
    G --> H[total_naves = total_naves + subtotal]
    H --> I[Incrementar i]
    I --> E
