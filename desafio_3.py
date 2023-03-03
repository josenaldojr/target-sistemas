import json


def main():

    with open("./dados/dados.json") as dados_json:
        dados = json.load(dados_json)

    # Dados contendo os dias com faturamento (valor > 0.0)
    dias_com_faturamento = [d for d in dados if d["valor"] > 0]

    menor_maior = menor_maior_valor(dias_com_faturamento)
    dias = dias_superio_media(dias_com_faturamento)

    print(f'Menor valor: {menor_maior[0]}')
    print(f'Maior valor: {menor_maior[1]}')
    print(f'Dia(s) superior(es) à média: {dias}')


def menor_maior_valor(dados):
    menor = maior = dados[0]["valor"]
    for d in dados:
        valor = d["valor"]
        # Verifica o MENOR valor
        if valor < menor:
            menor = valor
        # Verifica o MAIOR valor
        if valor > maior:
            maior = valor

    return menor, maior


def dias_superio_media(dados):
    soma, media, dias = 0, 0, 0
    for d in dados:
        valor = d["valor"]
        # Calcula à média
        soma += valor
        qtde = len(dados)
        media = soma / qtde
        # Varifica quantidade de dias superior à media
        if valor > media:
            dias += 1

    return dias
