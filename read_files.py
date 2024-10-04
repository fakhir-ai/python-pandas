import pandas as pd

df_csv = pd.read_csv(r"C:\Users\mumarfar\projects\python-pandas\data\countries of the world.csv")
df_txt = pd.read_table(r"C:\Users\mumarfar\projects\python-pandas\data\countries of the world.txt")
df_json = pd.read_json(r"C:\Users\mumarfar\projects\python-pandas\data\json_sample.json")

df_csv.info()
print(df_csv.describe())
