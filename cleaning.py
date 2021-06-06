import pandas as pd                     #Importar la librería


#creacion de la base de datos
df = pd.read_csv('D:\\Documentos\\UNIR\\Captura y almacenamiento de datos\\Actividad 1\\Actividad1-MCAD_UNIR\\data_act_01.csv', engine= 'python')     #Importar el dataset                               #Conocer las columnas
df.head()         #Imprime los primeros resultados
df.dropna()
df = df[['CrimeId','OriginalCrimeTypeName', 'OffenseDate', 'CallTime', 'Disposition', 'Address', 'City']] #Se filtra el dataframe con los datos que mas interesan.

df.duplicated().sum()                      #Suma y cuenta cuantos duplicados hay en el dataset
df['CrimeId'].duplicated().sum()        #Duplicados de la serie
#Filtro los duplicados y los transformo a una lista.
duplicates = df[df['CrimeId'].duplicated(keep=False)]['CrimeId'].tolist()
duplicates[:10] #Segun el conteo anterior hay 4 registros duplicados, por lo que si imprimo la lista puedo ver cuales son.

set_duplicates = set(duplicates) # se crea un set de la lista de duplicados
for r in set_duplicates: #se recorre el set de duplicados y se compara con cada uno de los datos en el dataframe
    dup = df[df['CrimeId'] == r]
    df.loc[dup.iloc[1,:].name, 'CrimeId'] = df.loc[dup.iloc[1,:].name]['CrimeId'] + 1 #Si se encuentra un registro igual, se suma 1 a numero de crimeId.
    
df.duplicated().sum() #Verificamos que no haya ningun registro duplicado

df.isnull().sum() #Verificar nulos y contarlos.

