from typing import List
from collections import Counter

def soma(numeros: List[int]) -> int:
    return sum(numeros)

def multiplicar(numeros: List[int]) -> int:
    resultado: int = 1
    for numero in numeros:
        resultado *= numero
    return resultado

def duplicados(numeros: List[int]) -> List[int]:
    contagem_numeros = Counter(numeros)
    minimo_duplicatas: int = 2
    lista_numeros_repetidos: List[int] = [
        numero for numero, qtd in contagem_numeros.items() if qtd >= minimo_duplicatas
    ]
    return lista_numeros_repetidos

def impares(numeros: List[int]) -> List[int]:
    return list({numero for numero in numeros if numero % 2 != 0})

def pares(numeros: List[int]) -> List[int]:
    return list({numero for numero in numeros if numero % 2 == 0})

def primos(numeros: List[int]) -> List[int]:
    def numero_primo(numero: int) -> bool:
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True
    return list({numero for numero in numeros if numero_primo(numero)})
