import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 1. Carregar dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# 2. Construção do modelo de regressão
df_mod = pd.get_dummies(df, columns=['retailer','region','sales_method'], drop_first=True)
X = df_mod[['total_sales','price_per_unit','units_sold']]
X = sm.add_constant(X)
y = df_mod['operating_profit']
model = sm.OLS(y, X).fit()

# 3. Obtenção de resíduos e valores ajustados
fitted = model.fittedvalues
residuals = model.resid

# 4. Plot Resíduos vs Valores Ajustados
plt.figure(figsize=(8, 5))
sns.scatterplot(x=fitted, y=residuals, alpha=0.6)
sns.regplot(x=fitted, y=residuals, scatter=False, lowess=True,
            line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plt.axhline(0, color='gray', linestyle='--')
plt.title('Resíduos vs Valores Ajustados')
plt.xlabel('Valores Ajustados (Fitted)')
plt.ylabel('Resíduos')
plt.tight_layout()
plt.show()
