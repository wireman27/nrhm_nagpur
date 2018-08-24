import pandas as pd
import os
import re

mainPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
dataPath = mainPath + '/data/DHIS (APRIL 15-MARCH 16)'
indicPath = mainPath + 'csv/chosenIndicators.csv'

indicData = pd.read_csv(indicPath)
indicList = [str(x) for x in indicData['indicId']]

dfColumns = ['block',
			'typeFac',
			'panchayat',
			'facility',
			'indicId',
			'quantType',
			'period',
			'value']

tableColumns = ['indicId','desc','quantType',
				'04-2015','05-2015','06-2015',
				'07-2015','08-2015','09-2015',
				'10-2015','11-2015','12-2015',
				'01-2016','02-2016','03-2016']

count = 0


def addPaths(path1,path2):
	return(path1+'/'+path2)

def createTable(excelFilePath,facType,block,isSC,panch):
	x = pd.DataFrame(columns=tableColumns)
	rawData = pd.read_excel(excelFilePath)

	blockList = []
	typeFacList = []
	panchayatList = []
	facilityList = []
	indicIdList = []
	quantTypeList = []
	periodList = []
	valueList = []

	table = dict()

	if not rawData.iloc[5,15] == 'Mar-2016':
		print('Problem with '+excelFilePath)
		return

	cleanData = rawData.iloc[6:rawData.shape[0],1:16]
	cleanData.columns = tableColumns

	indics = cleanData['indicId'].tolist()

	for indic in indicList:
		curIndex = indics.index(indic)
		term = False
		while term == False:
			if str(indics[curIndex + 1]) != 'nan':
				term = True
			else:
				cleanData.iat[curIndex + 1,0] = indic
				cleanData.iat[curIndex + 1,1] = indicData[indicData['indicId']==indic].iloc[0,1]
				curIndex = curIndex + 1

	for indicId in indicList:
		indicTable = cleanData[cleanData['indicId']==indicId]
		x = x.append(indicTable)

	for date in tableColumns[3:15]:
		counter = 0
		for indic in x['indicId'].tolist():
			blockList.append(block)
			typeFacList.append(facType)
			if isSC:
				panchayatList.append(panch)
			else:
				panchayatList.append('nan')
			facilityList.append(rawData.iloc[1,2])
			indicIdList.append(indic)
			quantTypeList.append(x.iloc[counter,2])
			periodList.append(date)
			valueList.append(x[(x['indicId']==indic)&(x['quantType']==x.iloc[counter,2])][date].iloc[0])
			counter = counter + 1

	listOfLists = [blockList,typeFacList,panchayatList,facilityList,
					indicIdList,quantTypeList,periodList,valueList]

	for y in range(0,len(listOfLists)):
		table[dfColumns[y]] = listOfLists[y]

	finalTable = pd.DataFrame(table)

	return(finalTable)

final = pd.DataFrame(columns=dfColumns)

for block in os.listdir(dataPath):
	print('Working on '+block)
	path1 = addPaths(dataPath,block)
	for facType in os.listdir(path1):
		path2 = addPaths(path1,facType)
		if facType != 'SC':
			for xls in os.listdir(path2):
				filePath = addPaths(path2,xls)
				x = createTable(filePath,facType,block,False,'nan')
				final = final.append(x)
		else:
			for panch in os.listdir(path2):
				path3 = addPaths(path2,panch)
				for xls in os.listdir(path3):
					filePath = addPaths(path3,xls)
					x = createTable(filePath,facType,block,True,panch)
					final = final.append(x)

final.to_csv(mainPath+'/masterTable2.csv',index=False)

