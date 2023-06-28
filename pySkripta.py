import pandas as pd
import numpy as np



usRoadFull = pd.read_csv('D:/mongoo/us_road.csv')
print(usRoadFull.shape)
print("ucitao bazu i odradio shape")
#%%
usRoadFullNoNull = usRoadFull.dropna()
print("odradio drop na")
print(usRoadFullNoNull.shape)
print("odradio i shape")
#%%
print(usRoadFullNoNull.head(10))
#%%
df = usRoadFullNoNull
#%%
print(df.head(11))
#%%
print(df.isnull())
#%%
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
df['Temperature(F)'] = df['Temperature(F)'].astype('int')
df['Wind_Chill(F)'] = df['Wind_Chill(F)'].astype('int')
df['Humidity(%)'] = df['Humidity(%)'].astype('int')
df['Pressure(in)'] = df['Pressure(in)'].astype('int')
df['Visibility(mi)'] = df['Visibility(mi)'].astype('int')
df['Wind_Speed(mph)'] = df['Wind_Speed(mph)'].astype('int')
df['Precipitation(in)'] = df['Precipitation(in)'].astype('int')
#%%
df['Number'] = df['Number'].astype('int')
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
df['Start_day'] = df['Start_day'].astype('int')

df['Start_month'] = df['Start_month'].astype('int')

df['Start_year'] = df['Start_year'].astype('int')

df['End_day'] = df['End_day'].astype('int')

df['End_month'] = df['End_month'].astype('int')

df['End_year'] = df['End_year'].astype('int')
#%%
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
print(df.shape)
#%%
print(df.isnull())
#%%
df.to_csv("D:/mongoo/roads.csv")
print("odradjeno")
#%%
df = pd.read_csv('D:/mongoo/roads.csv')
print(df.shape)
print(df.head(11))
#%%
sdf = df.sample(100)
print(sdf.shape)
print(sdf.head(11))
#%%
pd.set_option('display.max_columns', 100)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth', 0)
sdf = df.sample(100)
print(sdf.shape)
print(sdf.head(11))
#%%
sdf['Days_worked'] = int(0)
#%%
print(sdf.shape)
print(sdf.head(11))
print(sdf.dtypes)
#%%
sdf['Days_worked'] = int(0)
print(sdf.shape)
#%%
print(sdf.shape)
print(sdf.head(11))
print(sdf.dtypes)
#%%
sd = 15
sm = 12
sy = 2020
ed = 18
em = 1
ey = 2021

dw = ((((((ey-sy)*12)+em)-sm)*30)+ed)-sd
print(dw)
#%%
sdf['Days_worked'] = (
    ((((((sdf['End_year']-sdf['Start_year'])*12)+sdf['End_month'])-sdf['Start_month'])*30)+sdf['End_day'])-sdf['Start_day']
    ) 
#%%
print(sdf.shape)
print(sdf.head(11))
print(sdf.dtypes)
#%%
print(df.shape)
print("################################3")
df['Days_worked'] = int(0)
df['Days_worked'] = (
    ((((((df['End_year']-df['Start_year'])*12)+df['End_month'])-df['Start_month'])*30)+df['End_day'])-df['Start_day']
    ) 
#%%
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
print(df["Days_worked"].min())
print(df["Days_worked"].max())
print(df["Days_worked"].count())
print(df["Days_worked"].mean())
print(df["Days_worked"].median())
#%%
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
df.to_csv("D:/mongoo/roads.csv")
print("odradjeno")
#%%
print(df.shape)
print(df.head(11))
print(df.dtypes)
#%%
df = df.drop('Unnamed: 0', axis=1)
print("odradjeno")
print(df.shape)
print("#######################")
print(df.head(1))
print("#######################")
print(df.dtypes)
#%%
print(df.head(11))
#%%
df.to_csv("D:/mongoo/roads.csv")
print("odradjeno")
#%%
import pandas as pd
df = pd.read_csv('D:/mongoo/roads.csv')
#%%
pd.set_option('display.max_columns', 100)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth', 0)

#%%
df1 = df
#%%
df1 = df1.iloc[:,31:]
#%%
print(df1.dtypes)
df1["ID"]= df['ID']
print("odradjeno")
print(df1.dtypes)
#%%
df1 = df1.drop(['Start_day',
                'Start_month',
                'Start_year',
                'End_day',
                'End_month',
                'End_year',
                'Days_worked'],axis = 1)
#%%
print(df1.dtypes)
df1["ID"]= df['ID']
print("odradjeno")
print(df1.dtypes)

#%%
df1.to_json(r'D:/mongoo/roadsNearRoadConditions.json') 
#%%
#print(df11.head(11)
#df11.to_json("D:/mongoo/roadsNearRoadConditions.json")
#%%
koloneZaIzbacivanje = df1.columns.tolist()
df = df.drop(koloneZaIzbacivanje, axis = 1)
#%%
df = df.drop('Unnamed: 0', axis = 1)
print(df.dtypes)
#%%
df["ID"]=df1['ID']
#%%
print(df.dtypes)
#%%
print(df.head(11))
#%%
df.to_json(r'D:/mongoo/roadsPrimary.json')
#%%
#df1 = df1.drop('Unnamed: 0', axis = 1)
print(df1.dtypes)




















