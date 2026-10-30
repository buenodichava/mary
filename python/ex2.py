produtos = [
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 900}
]
preco_baixo = 0

for produto in produtos:
    if produto["preco"] < 500:
        print(f"produtos: {produto['nome']} - R${produto['preco']}")
        preco_baixo += 1 

print(f"os Produtos abaixo de 500: {preco_baixo}")