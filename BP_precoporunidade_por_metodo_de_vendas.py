import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="pastel")

df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

plt.figure(figsize=(8, 5))
sns.boxplot(x='sales_method', y='price_per_unit', data=df)
plt.title('Box‑Plot de Preço por Unidade por Método de Venda')
plt.xlabel('Método de Venda')
plt.ylabel('Preço por Unidade (US$)')
plt.tight_layout()
plt.show()
