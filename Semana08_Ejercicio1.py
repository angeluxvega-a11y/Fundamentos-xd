from eii_utils import leer_entero, limpiar_consola, leer_booleano, leer_booleano_opcional, leer_entero_opcional
#Variables
continuar:bool = True
i:int = 0
total:int = 0
edad:int = 0
promedio:float = 0

limpiar_consola() 

while continuar:
    edad = leer_entero_opcional("Digite la edad", 19)
    i = i + 1
    total += edad
    continuar = leer_booleano_opcional("Desea continuar", True)

promedio = total / i
print(promedio)
