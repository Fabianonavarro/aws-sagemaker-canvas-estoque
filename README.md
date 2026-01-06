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

├── previsao_estoque_simulado.py       # Script principal com dataset e previsões

└── README.md                          # Este arquivo


# Observação: Neste projeto, o dataset está **integrado diretamente no script**, não sendo necessário CSV.


Passo a Passo do Projeto
1. Dataset

O dataset simulado contém informações de estoque e vendas de três produtos ao longo de três meses:

Produto	Estoque atual	Preço unitário	Mês	Quantidade vendida

Caneta	200	1.50	1	150

Caderno	100	5.00	1	80

Mochila	50	50.00	1	40


...	...	...	...	...

O dataset é fictício e serve para simular previsões como se fosse no SageMaker Canvas.

2. Script de Previsão

O script previsao_estoque_simulado.py:

Cria o dataset em memória.

Calcula a previsão de vendas como 80% do estoque atual.

Gera três saídas:

Tabela detalhada de previsão por produto e mês.

Resumo total de estoque e previsão por produto.

Percentis de previsão de vendas (P10, P50, P100) por produto.

Exemplo de execução:

=== Previsões de Estoque ===
Produto Estoque_atual Previsao_vendas

0 Caneta 200 160

1 Caderno 100 80

2 Mochila 50 40

3 Caneta 180 144

...

=== Resumo Total por Produto ===
Produto Estoque_atual Previsao_vendas

0 Caneta 550 440

1 Caderno 270 216

2 Mochila 135 108

=== Percentis de Previsão de Vendas por Produto ===
Produto   P10   P50  P100

0 Caneta  136  144   160

1 Caderno  64   72    80

2 Mochila  32   36    40

### 3. Insights Estratégicos

Produtos com estoque maior terão maior previsão de vendas.

Percentis P10, P50 e P100 permitem planejar cenários conservador, médio e máximo de demanda.

O modelo simulado cobre todo o fluxo de trabalho do SageMaker Canvas: dataset → previsão → análise de resultados → insights estratég

---

## Referências

- [Documentação do SageMaker Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Repositório Base da DIO](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque)


Portfólio e Projetos:

• Portfólio: https://portifolionavinfo.netlify.app/

• DIO: https://www.dio.me/users/nav_info_suporte

• GitHub: https://github.com/Fabianonavarro

• LinkedIn: https://www.linkedin.com/in/fabiano-de-navarro


### Conhecimentos em Inteligência Artificial

Experiência prática em Inteligência Artificial e análise de dados, aplicando técnicas de Machine Learning para tratamento, análise e interpretação de dados, utilizando Python e bibliotecas especializadas.
Habilidade em automação de processos, visualização de dados e geração de insights estratégicos para apoiar decisões de negócios.
Experiência adquirida por meio de projetos práticos e cursos em Ciência de Dados, Data Analytics e IA, com integração em ambientes em nuvem (AWS).
