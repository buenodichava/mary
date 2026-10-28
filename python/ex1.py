pedidos = [
    {"cliente": "Ana", "valor": 250},
    {"cliente": "Carlos", "valor": 800},
    {"cliente": "Marina", "valor": 120},
    {"cliente": "João", "valor": 600}
]
soma_total = 0
valoralto = 0
media = 0

for pedido in pedidos:
   soma = pedido['valor']
   soma_total += soma
   print(f"{pedido['cliente']}: r${soma}")
   if pedido["valor"] > 300:
      print(f"cliente: {pedido['cliente']} - R$ {pedido['valor']}")
      valoralto += 1
      print(f"clientes com maior valor: {pedido['cliente']}")
      
media = soma_total/(len(pedidos))
print(f"valor total dos cliente: {soma_total}")
print(f"soma dos valores acima de 300: {valoralto}")
print(f"a media dos valores é: {media}")
