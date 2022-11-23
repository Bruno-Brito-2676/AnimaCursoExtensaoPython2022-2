# Pede o nome do aluno e sua nota (0 a 10) e, se ele tirou nota 10, mostra "Você é o bichão, mesmo..."
nomeAluno = input("Digite o nome do aluno: ")
notaAluno = float(input("Digite a nota do aluno: "))

print(f"\n{nomeAluno}, sua nota é {notaAluno}.")

if(notaAluno == 10):
  print("Você é o bichão mesmo...")
elif(notaAluno >= 6 and notaAluno < 10):
  print(f"{nomeAluno}, bom trabalho.")
elif(notaAluno <= 5):
  print("BURROO!!! Não tirou 10 kkkkk")
else:
  print("Nota inválida!")