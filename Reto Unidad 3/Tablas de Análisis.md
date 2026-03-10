# TABLA DE ENTRADA  
| VARIABLE | TIPO | DESCRIPCIÓN |
|----------|------|-------------|
| combustible_inicial | Real | Combustible inicial del avión |
| num_tramos | Entero | Número de tramos de la ruta |
| distancia | Real | Distancia del tramo en km |
| viento | Cadena | Tipo de viento |    

# TABLAS DE SALIDA  
| VARIABLE | TIPO | DESCRIPCIÓN |
|----------|------|-------------|   
| consumo_tramos | real | Combustible estimado consumido en el tramo actual, en kg |
| combustible_proyectado | real | Combustible que quedaría al terminar el tramo |
| cumbustible_restante | real | Combustible actualizado después de completar un tramo seguro |
| mensaje_alerta | Cadena | Mensaje crítico si el combustible proyectado baja de la reserva mínima |
| estado_vuelo | Cadena | Indica si el vuelo continúa, aborta ruta o completa la ruta |     

# TABLA DE CONSTANTES Y VARIABLES DE CONTROL    
| VARIABLE | TIPO | CLASIFICACIÓN | DESCRIPCIÓN |
|----------|------|---------------|-------------|
| consumo_base | real | Constante | Consumo base del avión en kg/km |
| reserva_minima | real | Constante | Límite mínimo legal de combustible que no se debe sobrepasar |
| factor_viento | real | Variable | Ajusta el consumo según el tipo de viento |
| combustible | real | Variable de proceso | Combustible disponible en cada momento del vuelo |
| tramo | entero | Variable de control | Contador que indica en qué tramo va el avión |
| num_tramos | entero | Variable de control | Cantidad máxima de tramos a recorrer |
| consumo_tramo | real | Variable de proceso | Combustible consumido en el tramo actual |
| combustible_proyectado | real | Variable de proceso | Combustible calculado antes de decidir si seguir o abortar |
| viento | cadena | Variable de entrada | Tipo de viento del tramo actual |
| distancia | real | Variable de entrada | Distancia del tramo actual |
