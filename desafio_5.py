def inverte_string(palavra):
    inverso = palavra[::-1]

    return inverso


palavra = input("Insira um palavra: ")
invertida = inverte_string(palavra)
print(invertida)
