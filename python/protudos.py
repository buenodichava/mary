produtos = [
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado"},  
    {"nome": "Monitor", "preco": 900},
    {"nome": "Cabo USB"}   
]

for produto in produtos:
    if "preco" in produto and produto["preco"] > 100:
        print(f"Produto: {produto['nome']} - R$ {produto['preco']}")

