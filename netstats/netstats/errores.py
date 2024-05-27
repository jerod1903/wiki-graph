"""Módulo de errores"""

class ErrorParametros(ValueError):
    def Error():
        return "ERROR: Faltan parámetros o los parametros ingresados son incorrectos."
    
class ErrorComando(ValueError):
    def Error():
        return "ERROR: La operación solicitada no existe."
    
class PaginaInexistente(ValueError):
    def Error():
        return "ERROR: La/s página/s solicitada/s no existe/n dentro de la red."

class ErrorNum(ValueError):
    def Error():
        return "ERROR: Por favor ingrese un número válido."
