#entradas
salario_fixo = 1400
vendas = 1300
percentual_comissao = 0.15

#processo
comissao = vendas * percentual_comissao
salario_total = salario_fixo + comissao

#saída
print("A comissão é de R$ {:.2f}".format(comissao))
print("O salário total é de R$ {:.2f}".format(salario_total))