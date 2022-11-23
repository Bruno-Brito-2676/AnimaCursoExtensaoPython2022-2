# Criação de funções
preco = 19.90

# Calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
# Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

# Aqui é o USO... aqui é imposto a calcular...
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função(7%){imposto}")

#Explicação variável local x global
print(preco) #????
preco_produto = 100
print(preco_produto) #????

# Agora calcular imposto a alíquota agora é 7%
valores = [1.99, 24.50, 78.27, 1515.5]

# se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de .... é ...." (1o. prço, 2o. imposto)
for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

# Declarar uma função calcular_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto
  
for valor in valores:
    print(f"O imposto de {valor} é {calcular_imposto(valor)}")