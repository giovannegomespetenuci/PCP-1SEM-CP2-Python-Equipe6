#02

# entrada de dados
a = float(input("Insira o primeiro lado do triângulo: "))
b = float(input("Insira o segundo lado do triângulo: "))
c = float(input("Insira o terceiro lado do triângulo: "))

# ordenação decrescente dos valores
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

# definição da mensagem exibida ao usuário de acordo com a propriedade do triângulo
class1 = ""
class2 = ""
if a >= (b+c):
    print("Não forma um triângulo")
else:
    # classificação em relação aos ângulos
    if a**2 == (b**2 + c**2):
        class1 = "Triângulo retângulo"
    elif a**2 > (b**2 + c**2):
        class1 = "Triângulo obtusângulo"
    elif a**2 < (b**2 + c**2):
        class1 = "Triângulo acutângulo"
    # classificação em relação aos lados
    if a == b == c:
        class2 = "e equilátero"
    elif a == b or b == c or a == c:
        class2 = "e isósceles"
    print(class1, class2)