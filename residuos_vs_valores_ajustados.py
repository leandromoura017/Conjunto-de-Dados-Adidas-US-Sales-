import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Carregar os dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# Ajustar o modelo de regressão
df_mod = pd.get_dummies(df, columns=['retailer', 'region', 'sales_method'], drop_first=True)
X = df_mod[['total_sales', 'price_per_unit', 'units_sold']]
X = sm.add_constant(X)
y = df_mod['operating_profit']
model = sm.OLS(y, X).fit()

# Obter valores ajustados e resíduos
fitted = model.fittedvalues
residuals = model.resid

# Criar o gráfico Residuals vs Fitted
plt.figure(figsize=(8, 5))
sns.scatterplot(x=fitted, y=residuals, alpha=0.6)
sns.regplot(x=fitted, y=residuals, scatter=False, lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plt.axhline(0, color='gray', linestyle='--')
plt.title('Gráfico Residuals vs Fitted')
plt.xlabel('Valores Ajustados (Fitted)')
plt.ylabel('Resíduos')
plt.tight_layout()
plt.show()
