from eii_utils import limpiar_consola
plastico1: str = "4123-5555-6666-7777"
plastico2: str = "4123-5555-6666-x"
plastico3: str = "4123-5555-6666-777a"
plastico4: str = "4123555566667777"
plastico5: str = "5123555566667777"


def funcion_inversa(texto:str) -> list[int]:
    salida:list[int] = []
    for caracter in texto:
        salida.append(int(caracter))

    return salida

if __name__ == "__main__":
    print(funcion_inversa(plastico5))