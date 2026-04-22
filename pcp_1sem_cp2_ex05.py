# Exercício 5 CP2 - PCP

import sys

# Funções
def pode_aprovar(idade, renda, valor):
    if idade < 18:
        print("Empréstimo negado: cliente menor de idade.")
        sys.exit()
    if valor > renda * 20:
        print("Empréstimo negado: valor solicitado excede 20x a renda mensal do cliente.")
        sys.exit()

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    elif parcelas <= 24:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    PMT = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
    return PMT

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor


# Bloco de Informações do cliente
Nome_Cliente     = input("Digite o nome do cliente que solicitará o empréstimo: ")
Idade_Cliente    = int  (input("Digite a idade do cliente: "))
Renda_Mensal     = float(input("Digite a renda mensal do cliente: "))
Valor_Emprestimo = float(input("Digite o valor desejado do empréstimo: "))
Numero_Parcelas  = int  (input("Digite o numero de parcelas que irá pagar (3 a 24): "))

# Validações
pode_aprovar(Idade_Cliente, Renda_Mensal, Valor_Emprestimo)

if Numero_Parcelas < 3 or Numero_Parcelas > 24:
    print("Empréstimo negado: número de parcelas inválido. Digite um valor entre 3 e 24.")
    sys.exit()

# Cálculos
taxa    = definir_taxa(Numero_Parcelas)
parcela = calcular_parcela(Valor_Emprestimo, taxa, Numero_Parcelas)
total   = calcular_total(parcela, Numero_Parcelas)
juros   = calcular_juros(total, Valor_Emprestimo)

# Saída
print("\nEmpréstimo aprovado")
print(f"Nome do cliente:      {Nome_Cliente}")
print(f"Valor financiado:     R$ {Valor_Emprestimo:.2f}")
print(f"Taxa de juros:        {taxa * 100:.0f}% ao mês")
print(f"Valor da parcela:     R$ {parcela:.2f}")
print(f"Total pago:           R$ {total:.2f}")
print(f"Total de juros pagos: R$ {juros:.2f}")