from entrada import ler_numero_inteiro

def main():
    numero = ler_numero_inteiro("Digite um numero inteiro: ", 
    "Isso não é um numero inteiro. Tente novamente"
    )
    print(f'Você digitou {numero}')

if __name__ == "__main__":
    main()
