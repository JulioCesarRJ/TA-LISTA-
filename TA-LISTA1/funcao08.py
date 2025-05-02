def capitalizar_palavras(frase: str) -> str:
    palavras = frase.split()
    palavras_capitalizadas = [palavra.capitalize() for palavra in palavras]
    return " ".join(palavras_capitalizadas)