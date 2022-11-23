contador = 1
print(contador)
contador = contador+1 
contador += 1
print(contador)

print("\nForma com o while")

while(contador <= 10):
  print(contador)
  contador += 1

# Laço for (pythobn for = for each)
fruta = "\nmorango\n"
print(fruta)

fruta1 = "Morango"
fruta2 = "Laranja"
fruta3 = "Pêra"

#Lista

frutas = ["Morango", "laranja", "Pêra   "]
print(frutas)

# quero exibir apenas a 3a fruta
print(frutas[2])

# Exibir quantas firtas tem na minha lista?
print(len(frutas))

# Quero incluir uma fruta nova
frutas.append("manga")
print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

i=0
while(i<4):
  print(frutas[i])
  i += 1

i=0
while(i<len(frutas)):
  print(frutas[i])
  i += 1

print("\nExemplo das frutas com FOR")

for fruta in frutas:
  print(fruta)