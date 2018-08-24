# Child Mortality in Nagpur
**scripts**

- `scripts/createParameterTree.py`: In the raw files, the parameters/indicators are stacked on top of each other with no way of telling what the parameter is without looking at its parent. For example, 17.2.1 reads *Sepsis* without any context. This script creates a CSV file with each parameter and its parent. One can work their up to tie any child to its parent/grandparent. Generates `csv/componentTree.csv`
- `scripts/createMasterTable.py`: Chooses indicators from `csv/chosenIndicators.csv` and then aggregates data from the 377 Excel files into `masterTable2.csv` holding 8 columns - 'block', 'typeFac', 'panchayat', 'facility', 'indicId', 'quantType', 'period', 'value'
- `scripts/analysis.py`: Pulls from masterTable2.csv and runs the OLS and Logit models. Prints summary and results of the models.
- `scripts/analysisComparisons.py`:Generates the preliminary CSVs needed to produce the visualizations in the 'Variations Across Blocks in Nagpur' section on the website. Also creates basic plots of the visualisations. The visualisations on the website are ultimately created by `js/webcharts.js` using JSON conversions of the CSVs
- `scripts/interDistrict.py`: Uses `csv/nameMappings.csv` and `csv/interDistrictComparison.csv` to create `geojson/interDistrict.geojson` that ultimately powers the district comparison map tool.
- `createTreemap.py`: Organises the data in a format understood by d3plus to create the treemap.


**javascript libraries**
- [MapboxGL](https://www.mapbox.com/mapbox-gl-js/api)
- [Chart.js](http://www.chartjs.org/docs/latest/)
- [D3plus](http://d3plus.org/)

**further improvements**
- Child mortality ultimately seems like an outcome of a capacity-need mismatch. Both models presented in the website point to the correlation between the extent of post-partum checkups and child mortality. The reason behind fewer women getting checkups might just be that there aren't enough ASHAs or other frontline workers available. Reports like [this](https://cag.gov.in/content/report-no25-2017-performance-audit-union-government-reproductive-and-child-health-under) from the CAG and news articles like [this](https://www.bloombergquint.com/pursuits/2018/07/28/why-health-workers-paid-rs-4000-per-month-are-vital-to-indias-national-nutrition-mission#gs.rAApxWc) one, highlight this capacity-need mismatch. While the IFA/Anemia ratio was a simple attempt to proxy this, further improvements can be made by introducing more robust measures of capacity utilisation and need.


