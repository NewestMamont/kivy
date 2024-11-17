import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')

c = str(input('Введите имя и фамилию режиссера на английском'))
df['Revenue (Millions)'].fillna('0', inplace = True)
def change_revenue(revenue):
    return float(revenue)
df['Revenue (Millions)'] = df['Revenue (Millions)'].apply(change_revenue)
df['Rating'].fillna('0', inplace = True)
a = df.info()
df['New'] = df[(df['Director'] == c)]['Director']
b = df.groupby(by = ['Year', 'New'])['Rating'].mean()
print(b)