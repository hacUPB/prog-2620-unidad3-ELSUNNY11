Inicio

    Definir consumo_base
    Definir reserva_minima

    Leer combustible_inicial
    Leer num_tramos

    combustible_restante = combustible_inicial
    tramo = 1
    estado_vuelo = "En ruta"

    Mientras tramo <= num_tramos Hacer

        Mostrar "Tramo ", tramo

        Leer distancia
        Leer tipo_viento

        consumo_tramo = calcular_consumo(distancia, CONSUMO_BASE, tipo_viento)

        combustible_proyectado = combustible_restante - consumo_tramo

        Mostrar "Consumo estimado del tramo: ", consumo_tramo
        Mostrar "Combustible proyectado: ", combustible_proyectado

        Si combustible_proyectado < RESERVA_MINIMA Entonces
            Mostrar "ALERTA CRÍTICA"
            Mostrar "Combustible por debajo de la reserva mínima"
            Mostrar "Abortar ruta y desviar al aeropuerto alterno más cercano"
            estado_vuelo = "Desviado a alterno"
            Salir del ciclo
        Si no
            combustible_restante = combustible_proyectado
            Mostrar "Tramo completado"
            Mostrar "Combustible restante: ", combustible_restante
        Fin Si

        tramo = tramo + 1

    Fin Mientras

    Si estado_vuelo = "En ruta" Entonces
        Mostrar "Ruta completada con seguridad"
        Mostrar "Combustible final: ", combustible_restante
    Fin Si

Fin


Función calcular_consumo(distancia, consumo_base, tipo_viento)

    Si tipo_viento = "headwind" Entonces
        factor_viento = 1.14
    Sino Si tipo_viento = "tailwind" Entonces
        factor_viento = 0.91
    Sino
        factor_viento = 1.00
    Fin Si

    consumo = distancia * consumo_base * factor_viento

    Retornar consumo

Fin Función
