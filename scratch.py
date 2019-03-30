import pandas as pd
dataset=pd.read_csv("smdata.csv")
print (dataset)
print (dataset.columns)
dataset.columns=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
print (dataset)