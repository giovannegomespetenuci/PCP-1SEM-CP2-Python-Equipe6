#03

#Solicitação das notas do 1ªSemestre:
CheckPoint1 = float(input("Digite a nota do Checkpoint 1:"))
CheckPoint2 = float(input("Digite a nota do Checkpoint 2:"))
CheckPoint3 = float(input("Digite a nota do Checkpoint 3:"))
Sprint1 = float(input("Digite a nota da Sprint 1: "))
Sprint2 = float(input("Digite a nota da Sprint 2: "))
GlobalSolution = float(input("Digite a nota da Global Solution: "))

# Lógica para encontrar a menor nota entre os 3 Checkpoints
if CheckPoint1 <= CheckPoint2 and CheckPoint1 <= CheckPoint3:
    menor_cp = CheckPoint1
elif CheckPoint2 <= CheckPoint1 and CheckPoint2 <= CheckPoint3:
    menor_cp = CheckPoint2
else:
    menor_cp = CheckPoint3

# Calculo da média e nota final:
media_semestre = (((CheckPoint1 + CheckPoint2 + CheckPoint3 - menor_cp + Sprint1 + Sprint2)/4)*0.4) + (GlobalSolution * 0.6)

MediaCPeso = media_semestre * 0.4

print(f"\nMédia Do 1ºSemestre (Sem Peso): {media_semestre:.1f}\n"
      f"Média Do 1ºSemestre (Com Peso): {MediaCPeso:.1f}")






