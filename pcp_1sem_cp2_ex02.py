#Exercício 2 CP2 - PCP:

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
    print("NAO FORMA TRIANGULO")
else:
    # classificação em relação aos ângulos
    if a**2 == (b**2 + c**2):
        class1 = "TRIANGULO RETANGULO"
    elif a**2 > (b**2 + c**2):
        class1 = "TRIANGULO OBTUSANGULO"
    elif a**2 < (b**2 + c**2):
        class1 = "TRIANGULO ACUTANGULO"
    # classificação em relação aos lados
    if a == b == c:
        class2 = "E EQUILATERO"
    elif a == b or b == c or a == c:
        class2 = "E ISOSCELES"
    print(class1, class2)