# 1. Importações
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Configuração visual (estilo do gráfico)
sns.set_theme(style="whitegrid", palette="pastel")

# 3. Carregamento dos dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# 4. Criação do box‑plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='units_sold', data=df, order=['Northeast','South','West','Midwest','Southeast'])

# 5. Personalização do gráfico
plt.title('Box‑Plot de Unidades Vendidas por Região')
plt.xlabel('Região')
plt.ylabel('Unidades Vendidas')
plt.xticks(rotation=45)

# 6. Exibição do gráfico
plt.tight_layout()
plt.show()
