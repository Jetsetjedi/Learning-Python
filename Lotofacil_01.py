import pandas as pd
from pandas_profiling import ProfileReport
base = pd.read_csv("titanic_train.csv")
profile = ProfileReport(base,title="profile teste")
#print(profile)
profile.to_file('relatorio.html')