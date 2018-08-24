import pandas as pd
import os
import re

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
# file for indicators
# testFile = mainPath + "/data/DHIS (APRIL 15-MARCH 16)/BHIWAPUR BLOCK/PHC/Copy of MonthlyProgressReportMIES_PHC Jawali_Apr-2015.xls"
finalList = list()
parents = [None, None, None, None, None]

data = pd.read_excel(testFile)
params = data.iloc[6:data.shape[0],1:3]
params.dropna(how='all',inplace=True)

params.columns = ['param','desc']

paramIds = params['param'].tolist()

for param in paramIds:
	param = str(param)
	entry = dict()
	entry['param']=param
	if re.search(r'Part',param):
		entry['parent']='none'
		parents[0] = param
	elif re.search(r'M',param):
		entry['parent']=parents[0]
		parents[1]=param
	elif param.count('.') == 1:
		entry['parent']=parents[1]
		parents[2]=param
	elif param.count('.') == 2 and not re.search(r'\d[a-zA-Z]|\d\(',param) :
		entry['parent']=parents[2]
		parents[3] = param
	elif param.count('.') == 2 and re.search(r'\d[a-zA-Z]|\d\(',param):
		entry['parent']=parents[3]
	elif param.count('.') == 3:
		entry['parent']=parents[3]
	finalList.append(entry)

final = pd.DataFrame(finalList)

componentTree = final.merge(params,on='param',how='inner')
componentTree = componentTree.reindex(['param','desc','parent'],axis='columns')
componentTree.columns = ['indicId','desc','parent']
componentTree.to_csv(mainPath+'../csv/componentTree.csv',index=False)





