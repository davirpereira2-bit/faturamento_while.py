faturamento_total = 0.0

print('---SISTEMA DE FATURAMENTO---')

while True :
  preco_unitario= 7.0
  unidades_vendidas = int(input('digite a quantidade:'))
 
  preco_total = preco_unitario * unidades_vendidas
  print(f'preço total R$ {preco_total}')

  faturamento_total += preco_total
  print('Venda registrada com sucesso!')

  continuar = input('Deseja registrar outra venda? (s/n): ').strip().lower()
  if continuar == 'n':
      break

print(f'faturamento total do dia R$ {faturamento_total}')   
