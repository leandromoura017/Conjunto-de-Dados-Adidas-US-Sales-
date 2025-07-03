# 1. Importações
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Configurações visuais (opcional, mas recomendado)
sns.set_theme(style="whitegrid", palette="pastel")

# 3. Leitura dos dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# 4. Criação do box‑plot
plt.figure(figsize=(8, 5))
sns.boxplot(x='sales_method', y='operating_profit', data=df)

# 5. Personalizações (título e rótulos)
plt.title('Box‑Plot de Lucro Operacional por Método de Venda')
plt.xlabel('Método de Venda')
plt.ylabel('Lucro Operacional (US$)')

# 6. Exibição do gráfico
plt.tight_layout()
plt.show()
