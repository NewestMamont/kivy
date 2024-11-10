import pandas as pd
k=0
df = pd.read_csv('GooglePlayStore_wild.csv')
'''freeapp = df[(df['Type'] == 'Free')]['Reviews'].max()
payapp = df[(df['Type'] != 'Free')]['Reviews'].max()
a = df[(df['Content Rating'] == 'Teen')]['Size'].min()
a = df['Reviews'].max()
b = df[(df['Reviews']==a)]['Category']
a = df[(df['Content Rating'] == 'Teen')]['Content Rating'].value_counts()
b = df[(df['Content Rating'] == 'Everyone 10+')]['Content Rating'].value_counts()
a = df['Rating'].mean()
b = df[(df['Type'] == 'Free')]['Rating'].mean()
a = df.groupby(by = 'Category')['Size'].agg(['min','max'])
a = df.groupby(by='Category')['Rating'].value_counts()
a = df[df['Rating']>4.9]['Price'].value_counts()
a = df.groupby(by='Type')['Rating'].agg(['min', 'mean', 'max'])
a = df.groupby(by=['Content Rating', 'Type'])['Price'].agg(['min', 'median', 'max'])
a = df.groupby(by=['Category', 'Content Rating'])['Reviews'].max()['GAME']
a = df.groupby(by=['Category', 'Content Rating'])['Type'].max()['GAME']
def change_size(size:str):
    if size[-1]=='k':
        return float(size[:-1])/1024
    elif size[-1]=='M':
        return float(size[:-1])
    return -1
df.Size = df.Size.apply(change_size)
a = df[df['Category']=='TOOLS']['Size'].max()
def change_price(price:str):
    if price[0] == '$':
        return float(price[1:])
    return 0
def change_install(installs:str):
    installs = installs.replace(',','')
    installs = installs.replace('+','')
    return int(installs)
df['Installs'] = df['Installs'].apply(change_install)
df['Price'] = df['Price'].apply(change_price)
df['Profit'] = df['Installs'] * df['Price']
a = df['Profit'].max()'''


def change_str(genres:str):
    genres.replace(';','`')
    return str(genres)
df['Genres'] = df['Genres'].apply(change_str)
a = df['Genres']
print(a)