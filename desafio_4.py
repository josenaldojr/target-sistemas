faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o faturamento total
total = 0
for v in faturamento.values():
    total += v

# Calcula e exibe o percentual
for k, v in faturamento.items():
    p = v / total
    print(f'{k} {p:0.2%}')
