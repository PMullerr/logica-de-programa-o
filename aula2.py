print("Meu primeiro programa aplicado a negócios")

#variaveis
produto = "Notebook"
preco = 3500.00
quantidade = 4
cliente_ativo = True
percentual_desconto = 10
percentual_comissao = 4
custo_unitario = 2600

#processos
total_venda = preco * quantidade
valor_desconto = total_venda * (percentual_desconto / 100)
valor_final = total_venda - valor_desconto
valor_comissao = total_venda * (percentual_comissao / 100)      
custo_total = custo_unitario * quantidade
lucro = valor_final - custo_total

#Saidas
print(produto)
print(preco)
print(quantidade)
print(cliente_ativo)
print(type(produto))
print(type(preco))
print(type(quantidade))
print(type(cliente_ativo))
print(total_venda)
print(valor_desconto)
print(valor_final)
print("Produto:", produto)
print("Preço unitário:", preco)
print("Quantidade:", quantidade)
print("Total da venda:", total_venda)
print("Percentual de desconto:", percentual_desconto, "%")
print("Valor do desconto:", valor_desconto)
print("Valor final da venda:", valor_final) 
print("Percentual de comissão:", percentual_comissao, "%")
print("Valor da comissão:", valor_comissao)
print("Custo unitário:", custo_unitario)
print("Custo total:", custo_total)

#novos dados
produto = "Monitor"
preco = 1800.00
quantidade = 7
percentual_desconto = 12
percentual_comissao = 5
custo_unitario = 1250

print("Produto:", produto)
print("Preço unitário:", preco)
print("Quantidade:", quantidade)
print("Total da venda:", total_venda)
print("Percentual de desconto:", percentual_desconto, "%")
print("Valor do desconto:", valor_desconto)
print("Valor final da venda:", valor_final) 
print("Percentual de comissão:", percentual_comissao, "%")
print("Valor da comissão:", valor_comissao)
print("Custo unitário:", custo_unitario)
print("Custo total:", custo_total)

