import pandas as pd
import numpy as np
import random
from openpyxl import Workbook
wb = Workbook()
sheet = wb.active

df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan], [19, 439, 6, 452, 226, 232]],
                  index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                  columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],
                                                      ['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
df.style.format(precision=0, na_rep='MISSING', thousands=" ",
                formatter={('Decision Tree', 'Tumour'): "{:.2f}",
                           ('Regression', 'Non-Tumour'): lambda x: "$ {:,.1f}".format(x*-1e6)})
sheet.append(df)
wb.save("predykcja.xlsx")
