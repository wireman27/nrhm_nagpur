import pandas as pd
import os
import numpy as np
import json

treemapList = []

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
data = pd.read_csv(mainPath + '/masterTable2.csv')

facilities = data['facility'].unique()

for fac in facilities:
	entry = dict()
	subset = data[(data["facility"]==fac)&(data["indicId"]=="1.1")]
	totANC = subset["value"].sum()
	parent = subset["typeFac"].iloc[0]
	grandparent = subset["block"].iloc[0]

	entry["id"] = fac
	entry["parent"] =  parent
	entry["grandparent"] =  grandparent
	entry["value"] = int(totANC)

	treemapList.append(entry)

test = pd.DataFrame()

df = pd.DataFrame(treemapList)
df.to_csv(mainPath+'/csv/treemap.csv',index=False)

# with open(mainPath + '/treemap.json','w') as f:
# 	json.dump(treemapList,f)



