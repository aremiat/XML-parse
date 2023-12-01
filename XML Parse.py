
import xml.etree.ElementTree as ET
import pandas as pd


series_list = [
    {
        "symbol": "BBDP1",
        "key" : "M.DE.N.VPI.C.A00000.I20.A",
        "frequency": "M",
        "title": "Consumer Price Index",
        "description": "Overall Increase in Prices for a given basket of goods",
        "unit": "2020=100",
        "adjustments": "Unadjusted"
    },
    {
        "symbol": "BBDP1",
        "key":"A.DE.N.VPI.C.A00000.I20.A",
        "frequency": "A",
        "title": "Consumer Price Index",
        "description": "Overall Increase in Prices for a given basket of goods",
        "unit": "2020=100",
        "adjustments": "Unadjusted"
    },
    #...
]



root = ET.parse("alex.xml")


namespace = {'bbk': 'http://www.bundesbank.de/statistik/zeitreihen/BBKcompact'}

freq = {
        'FREQ': root.find('.//bbk:Series', namespace).get('FREQ')}

value = {'BBK_ID': root.find('.//bbk:Series', namespace).get('BBK_ID'),
    'OBS': [
        {'TIME_PERIOD': obs.get('TIME_PERIOD'), 'OBS_VALUE': obs.get('OBS_VALUE')}
        for obs in root.findall('.//bbk:Obs', namespace)
    ]
}



df = pd.DataFrame(value)

# Extraire le titre de la première série dans la liste
title_to_replace = series_list[0]["title"]

# Renommer la colonne 'BBK_ID' en utilisant le titre
df = df.rename(columns={'BBK_ID': title_to_replace})

# ajoutez la fréquence à la série
df['frequence'] = pd.Series([freq] * len(df), index=df.index)

print(df)
