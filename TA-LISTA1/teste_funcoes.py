from funcoes02 import soma, multiplicar, duplicados, impares, pares, primos

def main() -> None:
    numeros: list[int] = []
    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        numeros.append(numero)

    print(f'Soma {soma(numeros)}')
    print(f'Multiplicação {multiplicar(numeros)}')
    print(f'Duplicados {duplicados(numeros)}')
    print(f'Impares {impares(numeros)}')
    print(f'Pares {pares(numeros)}')
    print(f'Primos {primos(numeros)}')

if __name__ == "__main__":
    main() 
