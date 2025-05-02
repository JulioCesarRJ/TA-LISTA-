def ler_numero_inteiro(mensagem: str, mensagem_erro: str)-> int:
    while True:
        entrada_numero = input(mensagem)
        try:
            return int(entrada_numero)
        except ValueError:
            print(mensagem_erro)

