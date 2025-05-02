from fila import menu_ordem

def mostrar_menu():
    print("\n=== Menu da Fila de Banco ===")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Fim")


def adicionar_cliente(fila: list):
    nome = input("Informe o nome do cliente: ").strip()
    if nome:
        fila.append(nome)
        print(f"{nome} foi adicionado à fila.")
    else:
        print("Nome inválido. Tente novamente.")


def atender_cliente(fila: list):
    if fila:
        cliente = fila.pop(0)
        print(f"Atendendo cliente: {cliente}")
    else:
        print("Não há clientes na fila para atender.")


def main():
    fila = []

    while True:
        mostrar_menu()
        opcao = menu_ordem("Escolha uma opção (1-3): ", "Opção inválida. Digite um número de 1 a 3.")

        if opcao == 1:
            adicionar_cliente(fila)
        elif opcao == 2:
            atender_cliente(fila)
        elif opcao == 3:
            print("Encerrando programa.")
            break
        else:
            print("Opção fora do intervalo. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
