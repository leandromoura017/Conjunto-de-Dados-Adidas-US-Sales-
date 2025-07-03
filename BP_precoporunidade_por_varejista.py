# 1. Importações
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Definir estilo visual
sns.set_theme(style="whitegrid", palette="pastel")

# 3. Carregar o dataset
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# 4. Criar o box‑plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='retailer', y='price_per_unit', data=df)

# 5. Personalização
plt.title('Box‑Plot de Preço por Unidade por Varejista')
plt.xlabel('Varejista')
plt.ylabel('Preço por Unidade (US$)')
plt.xticks(rotation=45)

# 6. Exibir o gráfico
plt.tight_layout()
plt.show()
