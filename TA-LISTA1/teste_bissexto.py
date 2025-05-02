from bissexto import ano_bissexto

def main():
    try:
        ano = int(input("Digite um ano:"))
        if ano_bissexto(ano):
            print(f'O ano {ano} é bissexto')
        else:
            print(f'O ano {ano} não é bissexto')
    except ValueError:
        print("Erro! Digite um número interio válido")

if __name__ == "__main__":
    main()
