"""
Generador de números de Fibonacci
Dado una posición, la función devuelve el número de Fibonacci en esa posición de la secuencia.
El número cero en la secuencia de Fibonacci es 0. El primer número es 1
Los números negativos no son aceptados
"""

def fibonacci(position):
  if(position < 0):
    raise ValueError("Invalid input")
  if(position == 1 or position == 2):
    return 1
  return fibonacci(position - 1) + fibonacci(position - 2)
