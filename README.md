# 📊 Adidas US Sales — Data Analysis Project
Este repositório contém o código completo utilizado para análise estatística da base de dados "Adidas US Sales" (Kaggle), conforme especificações do trabalho acadêmico seguindo normas ABNT.

# 🚀 Visão Geral
O objetivo é conduzir uma análise exploratória e inferencial sobre as vendas da Adidas nos EUA (2020–2021), incluindo:

1. Exploração dos dados: tratamento de inconsistências, verificação de formatos, outliers e dados faltantes.

2. Estatísticas descritivas: cálculo de média, mediana, variância, histogramas, Q‑Q plots e box‑plots.

3. Correlação entre variáveis quantitativas (Pearson/Spearman).

4. Testes de hipótese (ANOVA) sobre variáveis qualitativas.

5. Modelo de regressão linear para prever o lucro operacional, com análise de pressupostos (normalidade, homocedasticidade, multicolinearidade).

# 🛠️ Tecnologias & Instalação

- Python 3.8+

- Bibliotecas:

  `pip install pandas numpy matplotlib seaborn scipy statsmodel`

- Editor recomendado: Visual Studio Code com extensões Python e Jupyter

# 📈 Resultados e Conclusões

- Distribuições: identificados outliers e desbalanceamentos em diversas variáveis.

- Correlação: `vendas totais` e `lucro operacional` com correlação ~0,95.

- ANOVA: detectada significância estatística por método de venda e por varejista.

- Regressão Linear: modelo altamente explicativo (R² elevado); pressupostos atendidos após análise gráfica e teste.

# 📋 Como Executar

1. Clone o repositório:

  `git clone https://github.com/seu-usuario/adidas-us-sales-analysis.git`
  
2. Use o ambiente virtual:

  `python -m venv venv && venv\Scripts\activate  # Windows
  pip install -r requirements.txt`

3. Abra um notebook (`.ipynb`) no VS Code, Jupyter Notebook ou JupyterLab.

4. Execute todas as células — após isso, os gráficos verão exibidos e salvos na pasta `plots/`.
