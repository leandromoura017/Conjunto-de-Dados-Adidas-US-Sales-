# 1. Importações
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

# 2. Carregamento dos dados
df = pd.read_csv('Adidas_US_Sales.csv', parse_dates=['invoice_date'], dayfirst=True)

# 3. Preparação do modelo de regressão
df_mod = pd.get_dummies(df, columns=['retailer', 'region', 'sales_method'], drop_first=True)
X = df_mod[['total_sales','price_per_unit','units_sold']]
X = sm.add_constant(X)
y = df_mod['operating_profit']
modelo = sm.OLS(y, X).fit()

# 4. Geração do Q-Q plot dos resíduos
qqplot(modelo.resid, line='45')
plt.title('Q-Q Plot dos Resíduos do Modelo de Regressão')
plt.tight_layout()
plt.show()
