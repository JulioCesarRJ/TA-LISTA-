IGNORAR = {
    'a', 'o', 'as', 'os', 'de', 'da', 'do', 'das', 'dos',
    'em', 'no', 'na', 'nos', 'nas', 'e', 'com', 'por',
    'para', 'um', 'uma'
}

def capitalizar_titulo(frase: str) -> str:
    palavras = frase.lower().split()
    resultado = []

    for i, palavra in enumerate(palavras):
        if i == 0 or palavra not in IGNORAR:
            resultado.append(palavra.capitalize())
        else:
            resultado.append(palavra)

    return " ".join(resultado)
