# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro

# carrega dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# estatísticas descritivas
quant_cols = ['price_per_unit','units_sold','total_sales','operating_profit']
desc = df[quant_cols].describe()
desc.loc['var'] = desc.loc['std'] ** 2
print(desc)

# histogramas + box-plot
for col in quant_cols:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    sns.histplot(df[col], kde=True, ax=axes[0])
    axes[0].set_title(f'Histograma de {col}')
    sns.boxplot(x=df[col], ax=axes[1])
    axes[1].set_title(f'Box‑plot de {col}')
    plt.tight_layout()
    plt.show()

# teste Shapiro-Wilk
for col in quant_cols:
    stat, p = shapiro(df[col])
    print(f"{col}: W={stat:.3f}, p‑valor={p:.3f}")
