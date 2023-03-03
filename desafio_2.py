# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Calcula a sequência de Fibonacci até o número informado
n1, n2 = 0, 1
while n1 < numero:
    n1, n2 = n2, n1 + n2

# Informa se o número pertence ou não a sequência
if n1 == numero:
    print(f'O número {numero} pertence a sequência de Fibonacci.')
else:
    print(f'O número {numero} NÃO pertence a sequência de Fibonacci.')
