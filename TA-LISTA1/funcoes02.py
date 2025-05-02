from typing import List
from collections import Counter

def soma(numeros: List[int]) -> int:
    return sum(numeros)

def multiplicar(numeros: List[int]) -> int:
    from functools import reduce
    return reduce(lambda x, y: x * y, numeros, 1)

def duplicados(numeros: List[int]) -> List[int]:
    return [numero for numero, qtd in Counter(numeros).items() if qtd > 1]

def impares(numeros: List[int]) -> List[int]:
    return list({numero for numero in numeros if numero % 2 != 0})

def pares(numeros: List[int]) -> List[int]:
    return list({numero for numero in numeros if numero % 2 == 0})

def primos(numeros: List[int]) -> List[int]:
    def numero_primo(numero: int) -> bool:
        return numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))
    return list({numero for numero in numeros if numero_primo(numero)})
