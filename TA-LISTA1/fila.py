def menu_ordem(mensagem: str, mensagem_erro: str) -> int:
    while True:
        entrada = input(mensagem)
        if entrada.strip().lstrip('-').isdigit():
            return int(entrada)
        else:
            print(mensagem_erro)
