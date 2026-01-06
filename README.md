# Previsão de Estoque Inteligente (Simulação SageMaker Canvas)

Este projeto simula a criação de um modelo de **previsão de estoque** utilizando conceitos de Machine Learning no-code, inspirados no Amazon SageMaker Canvas. O objetivo é prever a demanda futura de produtos e auxiliar decisões estratégicas de reabastecimento.

---

## Objetivo

- Prever a quantidade de vendas futuras com base em dados históricos.
- Analisar fatores que impactam as vendas, como estoque atual e preço.
- Fornecer insights para otimização de estoque e planejamento de compras.

---

## Estrutura do Projeto

aws-sagemaker-canvas-estoque/

├── previsao_estoque_simulado.py # Script principal com dataset e previsões

└── README.md # Este arquivo


# Observação: Neste projeto, o dataset está **integrado diretamente no script**, não sendo necessário CSV.


## Passo a Passo do Projeto

### 1. Dataset

O dataset simulado contém informações de estoque e vendas de três produtos ao longo de três meses:

| Produto | Estoque atual | Preço unitário | Mês | Quantidade vendida |
|---------|---------------|----------------|-----|------------------|
| Caneta  | 200           | 1.50           | 1   | 150              |
| Caderno | 100           | 5.00           | 1   | 80               |
| Mochila | 50            | 50.00          | 1   | 40               |
| ...     | ...           | ...            | ... | ...              |

> O dataset é fictício e serve para simular previsões como se fosse no SageMaker Canvas.

---

### 2. Script de Previsão

O script `previsao_estoque_simulado.py`:

- Cria o dataset em memória.
- Calcula a **previsão de vendas** como 80% do estoque atual.
- Gera duas saídas:
  1. Tabela detalhada de previsão por produto e mês.
  2. Resumo total de estoque e previsão por produto.

Exemplo de execução:

=== Previsões de Estoque ===
Produto Estoque_atual Previsao_vendas
0 Caneta 200 160
1 Caderno 100 80
2 Mochila 50 40
3 Caneta 180 144
4 Caderno 90 72
5 Mochila 45 36
6 Caneta 170 136
7 Caderno 80 64
8 Mochila 40 32

=== Resumo Total por Produto ===
Produto Estoque_atual Previsao_vendas
0 Caneta 550 440
1 Caderno 270 216
2 Mochila 135 108



### 3. Insights Estratégicos

- Produtos com estoque maior terão maior previsão de vendas.
- O modelo simulado permite planejar reabastecimento para evitar excesso ou falta de produtos.
- Apesar de ser uma simulação, cobre todo o fluxo de trabalho do SageMaker Canvas: **dataset → previsão → análise de resultados → insights**.

---

## Próximos Passos / Extensões

- Adicionar mais variáveis (promoções, feriados, clima) para melhorar a previsão.
- Criar gráficos de tendência com matplotlib ou seaborn.
- Simular diferentes modelos de previsão (por exemplo, ajustando o percentual de previsão).

---

## Referências

- [Documentação do SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Repositório Base da DIO](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque)
