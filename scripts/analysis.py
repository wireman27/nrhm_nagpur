import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import json
print('hit it')

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")

data = pd.read_csv(mainPath + '/masterTable2.csv')
paramTree = pd.read_csv(mainPath + '/componentTree.csv')

listOfFac = []
y0 = []
y1 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

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

queryVacc = '(indicId == "10.1.09")'

queryIFA = '(indicId == "1.5")'
queryAnem = '(indicId == "1.7.1")'
queryANC = '(indicId == "1.1")'
query25kg = '(indicId == "4.2.2")' 
queryPpCheck = '(indicId == "6.1") or (indicId == "6.2")' 
queryJSY = '(indicId == "1.2")' 

# ols model


def createListOfFac(birthThresh):
	gg = data.groupby('facility')
	for facility, group in gg:
		totBirths = group.query(queryBirths)['value'].sum()
		totANC = group.query(queryANC)['value'].sum()
		totIFA = group.query(queryIFA)['value'].sum()
		totDeaths = group.query(queryDeaths)['value'].sum()
		tot25kg = group.query(query25kg)['value'].sum()
		totVacc = group.query(queryVacc)['value'].sum()
		totPpCheck = group.query(queryPpCheck)['value'].sum()
		totAnem = group.query(queryAnem)['value'].sum()
		totJSY = group.query(queryJSY)['value'].sum()
		if totBirths > birthThresh and \
			str(totIFA/totANC) != 'inf' and \
			totIFA/totAnem < 2 and \
			totDeaths/totBirths > 0 and \
			totVacc/totBirths < 2 and \
			totPpCheck / totANC < 2:
				y1.append(round(totDeaths/totBirths,4))
				x1.append(totVacc/totBirths)
				x2.append(totIFA/totAnem)
				x3.append(tot25kg/totBirths)
				x4.append(round(totPpCheck/totANC,4))
				x5.append(totJSY/totANC)
				listOfFac.append(facility)

createListOfFac(20)

reg = pd.DataFrame(columns=['y1','x1'])
reg['y1'] = y1
reg['x1'] = x1
reg['x2'] = x2
reg['x3'] = x3
reg['x4'] = x4
reg['x5'] = x5

test = reg[['y1','x4']]
test.columns = ['y','x']
test = test[["x","y"]]

ppcheck = test.to_dict('records')

with open(mainPath + '/web/json/ppcheckChart.json','w') as f:
	json.dump(ppcheck,f)

result = sm.ols(formula="y1 ~ x1 + x2 + x3 + x4 + x5", data=reg).fit()
print(result.params)
print(result.summary())

plt.plot(test['x'],test['y'],'o')
plt.show()

# logit regression

# def createListOfFacLogit(birthThresh):
# 	gg = data.groupby('facility')
# 	for facility, group in gg:
# 		totBirths = group.query(queryBirths)['value'].sum()
# 		totANC = group.query(queryANC)['value'].sum()
# 		totIFA = group.query(queryIFA)['value'].sum()
# 		totDeaths = group.query(queryDeaths)['value'].sum()
# 		tot25kg = group.query(query25kg)['value'].sum()
# 		totVacc = group.query(queryVacc)['value'].sum()
# 		totPpCheck = group.query(queryPpCheck)['value'].sum()
# 		totAnem = group.query(queryAnem)['value'].sum()
# 		totJSY = group.query(queryJSY)['value'].sum()
# 		if totBirths > birthThresh and \
# 			str(totIFA/totANC) != 'inf' and \
# 			totIFA/totAnem < 2 and \
# 			str(totDeaths/totBirths) != 'nan' and \
# 			str(totDeaths/totBirths) != 'inf' and \
# 			totVacc/totBirths < 2 and \
# 			totPpCheck / totANC < 2:
# 				y1.append(totDeaths/totBirths)
# 				x1.append(totVacc/totBirths)
# 				x2.append(totIFA/totAnem)
# 				x3.append(tot25kg/totBirths)
# 				x4.append(totPpCheck/totANC)
# 				x5.append(totJSY/totANC)
# 				listOfFac.append(facility)

# createListOfFacLogit(20)


# low = len([x for x in y1 if x < 0.025])
# probLowChildMort = low / len(y1)

# for mort in y1:
# 	if mort < 0.025:
# 		# y0.append(np.log(probLowChildMort/(1 - probLowChildMort)))
# 		y0.append(1)
# 	else:
# 		# y0.append(np.log((1-probLowChildMort)/probLowChildMort))
# 		y0.append(0)

# print('There is a total of '+str(len(y1))+' mortality values out of which '+str(low)+' facilities have mortality less than 25/1000 deaths')

# regLog = pd.DataFrame(columns=['y0','x1'])
# regLog['y0'] = y0
# regLog['x1'] = x1
# regLog['x2'] = x2
# regLog['x3'] = x3
# regLog['x4'] = x4
# regLog['x5'] = x5

# print(y0)

# resultLog = sm.Logit(regLog['y0'],regLog[['x1','x2','x3','x4','x5']]).fit()
# print(resultLog.params)
# print(resultLog.summary())






