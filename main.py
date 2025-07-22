import pandas as pd
import random
from faker import Faker
from datetime import datetime
from pathlib import Path

fake = Faker('pt_BR')
random.seed(42)
Faker.seed(42)

produtos = [
    "Camiseta", "Mangá", "Action Figure", "Mochila", "Broche",
    "Boné", "HQ", "Poster", "Caneca", "Chaveiro", "Adesivo", "Capacete Replica"
]
formas_pagamento = ["Crédito", "Débito", "Dinheiro", "Pix", "Boleto"]

nomes_lojas = [
    "Geek Universe", "Nerd World", "Planeta HQ", "Mundo Otaku", "Action Center",
    "Pixel Store", "Herói Urbano", "Caverna do Geek", "Multiverso Pop", "Nexus Geek"
]
cidades_estados = [
    ("São Paulo", "SP"), ("Rio de Janeiro", "RJ"), ("Belo Horizonte", "MG"),
    ("Porto Alegre", "RS"), ("Curitiba", "PR"), ("Florianópolis", "SC"),
    ("Salvador", "BA"), ("Recife", "PE"), ("Fortaleza", "CE"), ("Brasília", "DF")
]

num_pedidos = int(input("Quantas linhas de pedidos você deseja gerar? "))

output_dir = Path.cwd() / "relatorios"
output_dir.mkdir(exist_ok=True)

lojas = []
for i in range(len(nomes_lojas)):
    cidade, uf = cidades_estados[i]
    lojas.append({
        "codigo_loja": f"LJ{i+1:03}",
        "nome_loja": nomes_lojas[i],
        "Cidade": cidade,
        "UF": uf
    })
df_lojas = pd.DataFrame(lojas)

faixa_precos = {
    "Camiseta": (20, 120),
    "Mangá": (20, 150),
    "Action Figure": (150, 800),
    "Mochila": (100, 250),
    "Broche": (5, 20),
    "Boné": (30, 100),
    "HQ": (15, 150),
    "Poster": (15, 40),
    "Caneca": (30, 70),
    "Chaveiro": (10, 25),
    "Adesivo": (2, 10),
    "Capacete Replica": (500, 1500)
}

pedidos = []
for i in range(1, num_pedidos + 1):
    data_pedido = fake.date_between(start_date='-1y', end_date='today')
    loja = random.choice(lojas)
    produto = random.choice(produtos)
    qtde = random.randint(1, 5)
    faixa = faixa_precos[produto]
    preco_unit = round(random.uniform(*faixa), 2)
    pagamento = random.choice(formas_pagamento)

    pedidos.append({
        "ID Pedido": f"PD{i:05}",
        "Data Pedido": data_pedido.strftime('%Y-%m-%d'),
        "Código Loja": loja["codigo_loja"],
        "Produto": produto,
        "Qtde": qtde,
        "Preco Unit": preco_unit,
        "Pagamento": pagamento
    })
df_pedidos = pd.DataFrame(pedidos)

df_pedidos.to_csv(output_dir / "pedidos_geek.csv", index=False)
df_lojas.to_csv(output_dir / "lojas_geek.csv", index=False)

print(f"\nArquivos gerados com sucesso em: {output_dir}")
