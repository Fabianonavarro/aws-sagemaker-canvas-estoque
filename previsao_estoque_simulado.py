import pandas as pd

# ====== Dataset completo em memória ======
dados = {
    "Produto": ["Caneta", "Caderno", "Mochila",
                "Caneta", "Caderno", "Mochila",
                "Caneta", "Caderno", "Mochila"],
    "Estoque_atual": [200, 100, 50,
                      180, 90, 45,
                      170, 80, 40],
    "Preco_unitario": [1.50, 5.00, 50.00,
                       1.50, 5.00, 50.00,
                       1.50, 5.00, 50.00],
    "Mes": [1, 1, 1,
            2, 2, 2,
            3, 3, 3],
    "Quantidade_vendida": [150, 80, 40,
                           160, 85, 35,
                           155, 70, 45]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# ====== Função simulada de previsão de estoque ======
def prever_estoque(produto, estoque_atual):
    # Simula previsão = 80% do estoque atual
    return int(estoque_atual * 0.8)

# Aplicar a previsão
df['Previsao_vendas'] = df.apply(lambda x: prever_estoque(x['Produto'], x['Estoque_atual']), axis=1)

# ====== Mostrar resultados ======
print("=== Previsões de Estoque ===")
print(df[['Produto', 'Estoque_atual', 'Previsao_vendas']])

# ====== Resumo final por produto ======
resumo = df.groupby('Produto')[['Estoque_atual', 'Previsao_vendas']].sum().reset_index()
print("\n=== Resumo Total por Produto ===")
print(resumo)

# ====== NOVO: Análise de Percentis P10, P50 e P100 ======
percentis = df.groupby('Produto')['Previsao_vendas'].agg(
    P10=lambda x: x.quantile(0.1),
    P50=lambda x: x.quantile(0.5),
    P100=lambda x: x.quantile(1.0)
).reset_index()

print("\n=== Percentis de Previsão de Vendas por Produto ===")
print(percentis)
