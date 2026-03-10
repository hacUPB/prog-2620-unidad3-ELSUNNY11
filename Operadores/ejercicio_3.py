"""Ejercicio 3: Sistema de Becas
Una universidad otorga becas a los estudiantes si cumplen alguna de estas dos condiciones:
 
- Tener un promedio mayor o igual a 9.0.
- Estar en un nivel socioeconómico nivel 1 Y tener un promedio mayor a 8.0."""

# Datos del estudiante
promedio = float(input("Ingrese el promedio del estudiante: "))
nivel = int(input("Ingrese el nivel socioeconómico: "))

# Verificar si obtiene beca
beca = (promedio >= 9.0) or (nivel == 1 and promedio > 8.0)

print(beca)