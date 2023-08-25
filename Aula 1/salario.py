# Salario por Hora / Número de Horas no Mês
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o Sindicato
# Printar: salario bruto, quanto pagou ao INSS, quanto pagou ao Sindicato e o salario liquido

horas_mensais = int(input('Quantidade de horas mensais: '))
salario_hora = float(input('Salário por hora: '))
salario_bruto = horas_mensais*salario_hora
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-(ir+inss+sindicato)

print(f'Tabela de consulta de Salário:\nSalário Bruto: R$ {salario_bruto}\nTaxa Imposto de Renda (11%): R$ {ir}\nTaxa INSS (8%): R$ {inss}\nTaxa do Sindicato (5%): R$ {sindicato}\n\nSeu salário final e liquido é: R$ {salario_liquido}')
