import requests

resposta = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10
)

resposta.raise_for_status()
usuarios = resposta.json()

contadore = 0

for usuario in usuarios:
    nome = usuario["name"]
    if len(nome) > 15:
        contadore += 1
        print(f"Nome grande: {nome} ({len(nome)} caracteres)")

print(f"total nome com mais de 15 caracteres: {contadore}")