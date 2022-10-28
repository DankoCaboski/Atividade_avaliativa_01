salario = float(input('Informe o salario: '))
vendas = float(input('Total de vendas: '))
if  vendas > 1500:
    vendas = vendas-1500
    salario = (salario) + (1500*0.05) + (vendas*0.07)
    print(f'O salario do funcionario será {salario}')

else:
    salario = salario + vendas*0.05
    print(f'O salario do funcionario será {salario}')
