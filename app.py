# Questão 1:

indice = 13  
soma = 0 
k = 0 

while k < indice: 
    k = k + 1 
    soma = soma + k

print(soma)

# Questão 2:

def fibonacci(n):
    a,b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or a == n
    
num = 34
if fibonacci(num):
    print(f"{num} pertence a sequência de fibonacci.")
else:
    print(f"{num} não pertence a sequência de fibonacci.")

# Questão 3:

import json

with open('dados.json') as file:
    dados = json.load(file)

valores = [item['valor'] for item in dados if item['valor'] > 0]
menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"O menor valor de faturamento ocorrido em um dia do mês: R${menor_valor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: R${maior_valor:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_da_media} dias")

# Questão 4:

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / valor_total) * 100
    print(f"Percentual de {estado}: {percentual:.2f}%")

# Questão 5:

def inverter_string(s):
    resultado = ""
    
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

string_original = "Eu irei conseguir minha vaga de Estágio na Target !"
string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")

