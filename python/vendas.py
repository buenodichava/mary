vendas = [
    {"produto": "Mouse", "preco": 80, "quantidade": 2},
    {"produto": "Teclado", "preco": 150, "quantidade": 1},
    {"produto": "Monitor", "preco": 900, "quantidade": 3},
    {"produto": "Cabo USB", "preco": 25, "quantidade": 4}
]

total_vendas = 0

for venda in vendas:
    total = venda["preco"] * venda["quantidade"]
    total_vendas += total

    print(f"{venda['produto']}: R$ {total}")

print(f"Total das vendas: R$ {total_vendas}")