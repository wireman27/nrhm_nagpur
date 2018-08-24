print('hit it')
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
data = pd.read_csv(mainPath + '/masterTable2.csv')
paramTree = pd.read_csv(mainPath + '/componentTree.csv')

queryDeaths = '(indicId == "17.2.1" and quantType == "Total" and value != 0) or \
		(indicId == "17.2.2" and quantType == "Total" and value != 0) or \
		(indicId == "17.2.3" and quantType == "Total" and value != 0) or \
		(indicId == "17.2.4" and quantType == "Total" and value != 0) or \
		(indicId == "17.1" and quantType == "TOTAL" and value != 0) or \
		(indicId == "17.3.1" and quantType == "Total" and value != 0) or \
		(indicId == "17.3.2" and quantType == "Total" and value != 0) or \
		(indicId == "17.3.3" and quantType == "Total" and value != 0) or \
		(indicId == "17.3.4" and quantType == "Total" and value != 0) or \
		(indicId == "17.3.5" and quantType == "Total" and value != 0) or \
		(indicId == "4.1.2" and quantType == "TOTAL" and value != 0)' 

queryBirths = '(indicId == "4.1.1.c")'
queryPubDev = '(indicId == "2.2")'
queryPrivDev = '(indicId == "2.3")'
queryInpChild = '(indicId == "14.10.1.c" and quantType=="Children")'
queryInpAdult = '(indicId == "14.10.1.c" and quantType=="Adults")'
queryIFA = '(indicId == "1.5")'
queryAnem = '(indicId == "1.7.1")'

#time series of different blocks in terms of child mortality

blocksList = []
typeFacList = []
periodList = []
childMortalityList = []
privPubDevRatioList = []
childInpatientRatioList = []
immuASHAList = []
ifaDisp = []


#time-series

# gg = data.groupby(['block','period'])
# print(type(gg))

# for name, group in gg:
# 	totBirths = group.query(queryBirths)['value'].sum()
# 	totDeaths = group.query(queryDeaths)['value'].sum()
# 	totInpChild = group.query(queryInpChild)['value'].sum()
# 	totInpAdult = group.query(queryInpAdult)['value'].sum()

# 	blocksList.append(name[0])
# 	periodList.append(pd.to_datetime(name[1],infer_datetime_format=True))
# 	childMortalityList.append(round(totDeaths/totBirths,3))
# 	childInpatientRatioList.append(round(totInpChild/(totInpChild+totInpAdult),3))

# test = pd.DataFrame(columns=['block','period'])

# test['block'] = blocksList
# test['period'] = periodList
# test['childInpatientRatioList'] = childInpatientRatioList


# test.sort_values('period',inplace=True)
# test.to_csv(mainPath +'/csv/childInpRatio.csv',index=False)

# for block in data['block'].unique():
# 	blockData = test[test['block']==block]
# 	blockData.sort_values('period',inplace=True)
# 	x = blockData['period']
# 	y = blockData['childInpatientRatioList']
# 	plt.plot(x,y)


#comparisons

# gg = data.groupby('block')

# for name, group in gg:
# 	totPrivDev = group.query(queryPrivDev)['value'].sum()
# 	totPubDev = group.query(queryPubDev)['value'].sum()
# 	blocksList.append(name)
# 	privPubDevRatioList.append(round(totPrivDev/totPubDev,2))

# objects = blocksList
# y_pos = np.arange(len(objects))
# performance = privPubDevRatioList

# test = pd.DataFrame(columns=['block','privPubDevRatioList'])
# test['block'] = blocksList
# test['privPubDevRatioList'] = privPubDevRatioList
# test.to_csv(mainPath+'/csv/privPubDevRatio.csv',index=False)
 
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Private to Public Deliveries Ratio')

gg = data.groupby('typeFac')

for name, group in gg:
	totIFA = group.query(queryIFA)['value'].sum()
	totAnem = group.query(queryAnem)['value'].sum()
	typeFacList.append(name)
	ifaDisp.append(round(totIFA/totAnem,2))

test = pd.DataFrame(columns=['typeFac','ifaDisp'])

test['typeFac'] = typeFacList
test['ifaDisp'] = ifaDisp
test.to_csv(mainPath+'/csv/ifaDisp.csv',index=False)

objects = typeFacList
y_pos = np.arange(len(objects))
performance = ifaDisp
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('IFA/Anem')



plt.show()



