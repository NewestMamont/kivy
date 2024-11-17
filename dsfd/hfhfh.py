import pandas as pd
df = pd.read_csv('countries_of_the_world.csv')
df['Birthrate'].fillna('0', inplace = True)
df['Deathrate'].fillna('0', inplace = True)
def change_thing(birthrate:str):
    birthrate = birthrate.replace(',', '.')
    return float(birthrate)
def change_death(deathrate:str):
    deathrate = deathrate.replace(',', '.')
    return float(deathrate)
def change_final(deathtobirth:str):
    deathtobirth = deathtobirth.replace('inf', '0')
    return float(deathtobirth)
df['Birthrate'] = df['Birthrate'].apply(change_thing)
df['Deathrate'] = df['Deathrate'].apply(change_death)
df.info()
a = round(df.groupby(by=['Region'])['Birthrate'].mean(),1)
b = round(df.groupby(by='Region')['Deathrate'].mean(),1)
df['DeathToBirth']=df['Birthrate'] - df['Deathrate']
c = df.groupby(by='Region')['DeathToBirth'].mean()
print(c)