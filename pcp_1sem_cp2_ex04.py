def calcular_horas_extras(salario_base, horas):
    valor_total = salario_base * 0.015 * horas
    return valor_total

def calcular_descontos_faltas(salario_base, faltas):
    valor_total = salario_base * 0.02 * faltas
    return valor_total

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 's':
        return 0

    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    elif cargo == 4:
        return 100
    else:
        return 0

nome = input("Digite o seu nome: ")
cargo = int(input("Digite o seu cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Digite o seu salário base: "))
horas = float(input("Digite a quantidade de horas extras trabalhadas: "))
faltas = int(input("Digite a quantidade faltas no mês: "))
recebeu_bonus = input("Você recebeu bônus por desempenho? (s/n): ")

valor_horas = calcular_horas_extras(salario_base, horas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base + valor_horas + valor_bonus
total_acrescimos = valor_horas + valor_bonus
total_descontos = calcular_descontos_faltas(salario_base, faltas)
salario_final = salario_bruto - total_descontos

print()
print(f"Nome: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de descontos por faltas: R$ {total_descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
