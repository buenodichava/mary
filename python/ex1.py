pedidos = [
    {"cliente": "Ana", "valor": 250},
    {"cliente": "Carlos", "valor": 800},
    {"cliente": "Marina", "valor": 120},
    {"cliente": "João", "valor": 600}
]
soma_total = 0
valoralto = 0
media = 0
maiorvalor = 0
nome_maior_cliente = ""
segundo_valor = 0
nome_segundo_cliente = ""
cliente_atencao = []
cliente_baixo = []

for pedido in pedidos:
    soma = pedido['valor']
    soma_total += soma
    print(f"{pedido['cliente']}: r${soma}")
    if pedido["valor"] > 300:
        print(f"cliente: {pedido['cliente']} - R$ {pedido['valor']}")
        valoralto += 1

    if pedido["valor"] > maiorvalor:
        segundo_valor = maiorvalor
        nome_segundo_cliente = nome_maior_cliente
        maiorvalor = pedido["valor"]
        nome_maior_cliente = pedido["cliente"]
    elif pedido["valor"] > segundo_valor:
        segundo_valor = pedido["valor"]
        nome_segundo_cliente = pedido["cliente"]

    if pedido["valor"] >= 500:
        cliente_atencao.append((pedido["cliente"], pedido["valor"]))

    if pedido["valor"] <= 300:
        cliente_baixo.append((pedido["cliente"], pedido["valor"]))

print("clientes de valor baixo")
for nome, valor in cliente_baixo:
    print(f" {nome} R${valor}")

print("cliente quem precisao de atençao")
for nome, valor in cliente_atencao:
    print(f" {nome} R${valor}")

print(f"cliente mais alto é: {nome_maior_cliente} {maiorvalor}")
print(f"segundo maior: {nome_segundo_cliente} R${segundo_valor}")
media = soma_total/len(pedidos)
print(f"valor total dos cliente: {soma_total}")
print(f"soma dos valores acima de 300: {valoralto}")
print(f"a media dos valores é: {media}")