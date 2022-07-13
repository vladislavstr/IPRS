pip install pandas
import pandas as pd

data_inventory = pd.read_excel('ипрс.xlsx', index_col=0) 

print (data_inventory)

