#entrada
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade vendida: "))

#processos
total_vendas = preco * quantidade

#saidas
print("Produto: {}".format(produto))
print("Preço unitário: R$ {:.2f}".format(preco))
print("Quantidade comprada: {}".format(quantidade))
print("Total de compra: R$ {:.2f}".format(total_vendas))
