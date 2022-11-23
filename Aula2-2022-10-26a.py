# Comando input(): quero permitir que
# o usuário digite algo...
nome = input("Escreva seu nome: ")
idade = int(input("Escreva sua idade: "))

# Comando para pegar o sexo
sexo = input("Escreva seu sexo (M ou F): ")

# Comando de saída..exibir na tela
print(f"\nBoa noite, sua idade é {idade}")

# Comando de saída..exibir na tela
print(f"Boa noite {nome}, sua idade é {idade}")

# Comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")

# E se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print(f"O dobro da idade sua é {dobro}\n")

# Estrutura condicional - o famoso "SE" (if)
#Se a pessoa foir maior de idade mostre "você é maior de idade, ótimo! Já pode beber ou dirigir"
if(idade >= 18):
  print("Você é maior de idade,   ótimo! Já pode beber ou dirigir.\n")
else:
  print("Você é menor de idade! NÃO pode beber ou dirigir.\n")

# E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)
# Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
if(sexo == "M" and idade >= 18):
  print("E você também precisa/precisou prestar o serviço militar obrigatório.\n")

print("Vai ser executada de qualquer jeito.\n")