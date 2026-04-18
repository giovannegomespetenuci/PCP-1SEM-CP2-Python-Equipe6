#01

import sys

# entrada de dados
estado = int(input("Insira o estado de origem do caminhão: "))
peso_ton = int(input("Insira o peso do caminhão (em toneladas): "))
cod_carga = int(input("Insira o código da carga: "))

peso_kg = peso_ton * 1000 # conversão de toneladas para quilos

# definição do preço do quilo da carga
if 10 <= cod_carga <= 20:
    preco_carga = peso_kg * 100
elif 21 <= cod_carga <= 30:
    preco_carga = peso_kg * 250
elif 31 <= cod_carga <= 40:
    preco_carga = peso_kg * 340
else:
    print("Erro! Insira um código de carga válido!")
    sys.exit()

# definição do valor do imposto pago na carga
match estado:
    case 1:
        imposto = preco_carga * 0.35
    case 2:
        imposto = preco_carga * 0.25
    case 3:
        imposto = preco_carga * 0.15
    case 4:
        imposto = preco_carga * 0.05
    case 5:
        imposto = "Isento"
    case _:
        print("Erro! Insira um estado válido!")
        sys.exit()

# saída de dados, exposição do resultados
print(f"O preço da carga é de R${preco_carga}")
if imposto == "Isento":
    print("Sua carga está isenta do imposto")
    print(f"O preço total da sua carga é de R${preco_carga}")
else:
    print(f"O total do imposto é de R${imposto}")
    valor_total = preco_carga + imposto
    print(f"O preço total da sua carga é de R${valor_total}")