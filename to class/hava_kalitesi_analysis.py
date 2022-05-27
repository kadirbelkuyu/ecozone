path_to_data = "../input/gdgyarma/77_202106_havakalitesiselcuklu.csv"
df = pd.read_csv(path_to_data,encoding='Windows-1252', sep=";", header=1)
#df = df[0:1963]#bonsa


"""df['PM10 ( - )']=df['PM10 ( - )'].str.replace(",",".")
df['PM10 ( - )']=df['PM10 ( - )'].str.replace(".","")
df['PM10 ( - )']=df['PM10 ( - )'].str.replace("-","-1")
df['PM10 ( - )']=df['PM10 ( - )'].astype(float)
df['PM10 ( - )']=df['PM10 ( - )'].loc[df['PM10 ( - )']!=-1.0]
df['PM10 ( - )']= df['PM10 ( - )'].dropna()
df['PM10 ( - )']=df['PM10 ( - )']/100


df['NOX ( - )']=df['NOX ( - )'].str.replace(",",".")
df['NOX ( - )']=df['NOX ( - )'].str.replace(".","")
df['NOX ( - )']=df['NOX ( - )'].str.replace("-","-1")
df['NOX ( - )']=df['NOX ( - )'].astype(float)
df['NOX ( - )']=df['NOX ( - )'].loc[df['NOX ( - )']!=-1.0]
df['NOX ( - )']= df['NOX ( - )'].dropna()
df['NOX ( - )']=df['NOX ( - )']/100
#meramda yok 

df['O3 ( - )']=df['O3 ( - )'].str.replace(",",".")
df['O3 ( - )']=df['O3 ( - )'].str.replace(".","")
df['O3 ( - )']=df['O3 ( - )'].str.replace("-","-1")
df['O3 ( - )']=df['O3 ( - )'].astype(float)
df['O3 ( - )']=df['O3 ( - )'].loc[df['O3 ( - )']!=-1.0]
df['O3 ( - )']= df['O3 ( - )'].dropna()
df['O3 ( - )']=df['O3 ( - )']/100



df['NO2 ( - )']=df['NO2 ( - )'].str.replace(",",".")
df['NO2 ( - )']=df['NO2 ( - )'].str.replace(".","")
df['NO2 ( - )']=df['NO2 ( - )'].str.replace("-","-1")
df['NO2 ( - )']=df['NO2 ( - )'].astype(float)
df['NO2 ( - )']=df['NO2 ( - )'].loc[df['NO2 ( - )']!=-1.0]
df['NO2 ( - )']= df['NO2 ( - )'].dropna()
df['NO2 ( - )']=df['NO2 ( - )']/100

#meramda var

df['CO ( - )']=df['CO ( - )'].str.replace(",",".")
df['CO ( - )']=df['CO ( - )'].str.replace(".","")
df['CO ( - )']=df['CO ( - )'].str.replace("-","-1")
df['CO ( - )']=df['CO ( - )'].astype(float)
df['CO ( - )']=df['CO ( - )'].loc[df['CO ( - )']!=-1.0]
df['CO ( - )']= df['CO ( - )'].dropna()
df['CO ( - )']=df['CO ( - )']/100
"""


df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )'].str.replace(",",".")
df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )'].str.replace(".","")
df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )'].str.replace("-","-1")
df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )'].astype(float)
df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )'].loc[df['PM10 ( µg/m3 )']!=-1.0]
df['PM10 ( µg/m3 )']= df['PM10 ( µg/m3 )'].dropna()
df['PM10 ( µg/m3 )']=df['PM10 ( µg/m3 )']/100


df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )'].str.replace(",",".")
df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )'].str.replace(".","")
df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )'].str.replace("-","-1")
df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )'].astype(float)
df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )'].loc[df['SO2 ( µg/m3 )']!=-1.0]
df['SO2 ( µg/m3 )']= df['SO2 ( µg/m3 )'].dropna()
df['SO2 ( µg/m3 )']=df['SO2 ( µg/m3 )']/100

df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )'].str.replace(",",".")
df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )'].str.replace(".","")
df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )'].str.replace("-","-1")
df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )'].astype(float)
df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )'].loc[df['NOX ( µg/m3 )']!=-1.0]
df['NOX ( µg/m3 )']= df['NOX ( µg/m3 )'].dropna()
df['NOX ( µg/m3 )']=df['NOX ( µg/m3 )']/100
#meramda yok 
"""
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )'].str.replace(",",".")
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )'].str.replace(".","")
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )'].str.replace("-","-1")
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )'].astype(float)
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )'].loc[df['O3 ( µg/m3 )']!=-1.0]
df['O3 ( µg/m3 )']= df['O3 ( µg/m3 )'].dropna()
df['O3 ( µg/m3 )']=df['O3 ( µg/m3 )']/100"""



df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )'].str.replace(",",".")
df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )'].str.replace(".","")
df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )'].str.replace("-","-1")
df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )'].astype(float)
df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )'].loc[df['NO2 ( µg/m3 )']!=-1.0]
df['NO2 ( µg/m3 )']= df['NO2 ( µg/m3 )'].dropna()
df['NO2 ( µg/m3 )']=df['NO2 ( µg/m3 )']/100

#meramda var

df['CO ( µg/m3 )']=df['CO ( µg/m3 )'].str.replace(",",".")
df['CO ( µg/m3 )']=df['CO ( µg/m3 )'].str.replace(".","")
df['CO ( µg/m3 )']=df['CO ( µg/m3 )'].str.replace("-","-1")
df['CO ( µg/m3 )']=df['CO ( µg/m3 )'].astype(float)
df['CO ( µg/m3 )']=df['CO ( µg/m3 )'].loc[df['CO ( µg/m3 )']!=-1.0]
df['CO ( µg/m3 )']= df['CO ( µg/m3 )'].dropna()
df['CO ( µg/m3 )']=df['CO ( µg/m3 )']/100


df.describe()