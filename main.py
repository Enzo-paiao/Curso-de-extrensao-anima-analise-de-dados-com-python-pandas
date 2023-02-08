
from IPython.display import display
import pandas as pd
import numpy as np



combustiveis_df = pd.read_excell("ca-2021-02.xlsx")
ca_df = combustiveis_df[['Revenda', 'Municipio','Produto', 'Valor de Venda' ]]
print(combustiveis_df.describe())
print(combustiveis_df.info())

display(ca_df)

gas_df = ca_df.loc[ca_df["Produto"] == "GASOLINA"]
display(gas_df)
display(gas_df['Valor de Venda'].max())
