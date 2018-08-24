import pandas as pd
import os
import numpy as np
import json

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

nm = pd.read_csv(mainPath +'/boundaries/nameMappings.csv')
idc = pd.read_csv(mainPath + '/analysis/interDistrictComparison.csv')

with open(mainPath+'/boundaries/maharashtra_districts.geojson','r') as f:
	geoj = json.loads(f.read())

count = 0

for feature in geoj['features']:
	d1 = feature['properties']['DISTRICT']
	d2 = nm[(nm['name_boundaries']==d1)&(nm['type']=='district')]['name_nrhm'].iloc[0]

	for ind in idc.columns: 
		if ind != 'name':
			val = idc[idc['name']==d2][ind].iloc[0]
			geoj['features'][count]['properties'][ind] = val

			if d2 == 'Aurangabad':
				print(geoj['features'][count]['properties'][ind])
				print(val)
	count = count + 1

# with open(mainPath + '/geojson/interDistrict.geojson','w') as f:
# 	json.dump(geoj,f)






