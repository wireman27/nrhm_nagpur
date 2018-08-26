var COLORS = [
	'rgb(255, 99, 132)',
	'rgb(255, 159, 64)',
	'rgb(255, 205, 86)',
	'rgb(75, 192, 192)',
	'rgb(54, 162, 235)',
	'rgb(153, 102, 255)',
	'rgb(201, 203, 207)',
	'rgb(255, 153, 102)',
	'rgb(204, 102, 255)',
	'rgb(51, 204, 51)',
	'rgb(204, 102, 0)',
	'rgb(51, 102, 204)'
];


var blocks = [
'MOUDA BLOCK','UMRED BLOCK','KUHI BLOCK','KALMESHWAR BLOCK','RAMTEK BLOCK',
'KAMPTEE BLOCK','HINGNA BLOCK','KATOL BLOCK','NAGPUR BLOCK','SAONER BLOCK',
'PARSHIVNI BLOCK','NARKHED BLOCK','BHIWAPUR BLOCK']

var typeFac = ["PHC","RH","RH-SDH","SC","WH"];

var periods = [
'2015-04-01','2015-05-01','2015-06-01',
'2015-07-01','2015-08-01','2015-09-01',
'2015-10-01','2015-11-01','2015-12-01',
'2016-01-01','2016-02-01','2016-03-01'
]

// time series

function createDatasets(timeseries, valueField) {
	datasetsArray = []
	for(var x = 0; x < blocks.length; x++) {
		var blockArray = [];
		for(var y = 0; y < periods.length;y++) {
			for(var z = 0; z < timeseries.length;z++) {
				if(timeseries[z]['block']==blocks[x]&&timeseries[z]['period']==periods[y]) {
					blockArray.push(timeseries[z][valueField])
				}
			}
		}
		var colorName = COLORS[x % COLORS.length];
		var newColor = colorName;

		blockDataset = {
			label: blocks[x],
			backgroundColor: newColor,
			borderColor: newColor,
			data: blockArray,
			pointRadius: 0,
			fill: false,
		}
		datasetsArray.push(blockDataset)
	}
	return(datasetsArray)
}


function createDatasetBar(barChart,valueField,hierarchy,hierarchyName,color) {
	fullArray = []
	for(var x = 0; x < hierarchy.length; x++) {
		for(var z = 0;z < barChart.length;z++) {
			if(barChart[z][hierarchyName]==hierarchy[x]) {
				fullArray.push(barChart[z][valueField])
			}
		}
	}

	var colorName = COLORS[x % COLORS.length];
	var newColor = colorName;

	dataset = {
		label: 'Ratio',
		backgroundColor: color,
		borderColor: color,
		borderWidth: 1,
		data: fullArray,
		fill: true,
	}
	return([dataset])
}



var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		childMortality = JSON.parse(xhttp.responseText)
		var ctx = document.getElementById("myChart");
		datasetsArray = createDatasets(childMortality,'childMortalityList');
		var config = {
			type: 'line',
			data: {
				labels: ['Apr-15', 'May-15', 'June-15', 'July-15', 'Aug-15', 'Sept-15', 'Oct-15','Nov-15','Dec-15','Jan-16','Feb-16','Mar-16'],
				datasets: datasetsArray
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Child Mortality from Mar-2015 to Apr-2016',
					fontFamily: "'Montserrat', sans-serif",
					fontSize: 16,
					fontColor: 'black'

				},
				tooltips: {
					mode: 'point',
					intersect: true,
				},
				hover: {
					mode: 'nearest',
					intersect: false
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Month',
							fontStyle: "'Montserrat', sans-serif",
							fontSize: 14
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Deaths per Live Birth',
							fontStyle: "'Montserrat', sans-serif",
							fontSize: 14
						}
					}]
				}
			}
		};
		myLine = new Chart(ctx, config)
	}
};
xhttp.open("GET",'json/childMortality.json',true);
xhttp.send();


var xhttp2 = new XMLHttpRequest();
xhttp2.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		childInpRatio = JSON.parse(xhttp2.responseText)
		var ctx2 = document.getElementById("myChart2");
		datasetsArray = createDatasets(childInpRatio,'childInpatientRatioList');
		var config2 = {
			type: 'line',
			data: {
				labels: ['Apr-15', 'May-15', 'June-15', 'July-15', 'Aug-15', 'Sept-15', 'Oct-15','Nov-15','Dec-15','Jan-16','Feb-16','Mar-16'],
				datasets: datasetsArray
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Ratio of Child Inpatients to Total Inpatients',
					fontFamily: "'Montserrat', sans-serif",
					fontSize: 16,
					fontColor: 'black'

				},
				tooltips: {
					mode: 'point',
					intersect: true,
				},
				hover: {
					mode: 'nearest',
					intersect: false
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Month',
							fontStyle: "'Montserrat', sans-serif",
							fontSize: 14
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Ratio',
							fontStyle:"'Montserrat', sans-serif",
							fontSize: 14
						}
					}]
				}
			}
		};
		myLine2 = new Chart(ctx2, config2)
	}
};
xhttp2.open("GET",'json/childInpRatio.json',true);
xhttp2.send();


// barcharts


var xhttp3 = new XMLHttpRequest();
xhttp3.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		privPubDevRatio = JSON.parse(xhttp3.responseText)
		var ctx3 = document.getElementById("myChart3");
		dataset = createDatasetBar(privPubDevRatio,'privPubDevRatioList',blocks,'block','rgb(255, 205, 86,0.9)');
		var config3 = {
			type: 'bar',
			data: {
				labels: blocks,
				datasets: dataset
			},
			options: {
				maintainAspectRatio: false,
				responsive: true,
				title: {
					display: true,
					text: 'Ratio of Private Deliveries to Public Deliveries',
					fontFamily: "'Montserrat', sans-serif",
					fontSize: 16,
					fontColor: 'black'

				},
				tooltips: {
					mode: 'point',
					intersect: true,
				},
				hover: {
					mode: 'nearest',
					intersect: false
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Block',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 14
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Ratio',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 14
						}
					}]
				}
			}
		};
		myBar = new Chart(ctx3, config3)
	}
};
xhttp3.open("GET",'json/privPubDevRatio.json',true);
xhttp3.send();

var xhttp4 = new XMLHttpRequest();
xhttp4.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		ifaDispRatio = JSON.parse(xhttp4.responseText)
		var ctx4 = document.getElementById("myChart4");
		dataset = createDatasetBar(ifaDispRatio,'ifaDisp',typeFac,'typeFac',"rgb(153, 102, 255,0.6)");
		console.log(dataset)
		var config4 = {
			type: 'bar',
			data: {
				labels: typeFac,
				datasets: dataset
			},
			options: {
				maintainAspectRatio: false,
				responsive: true,
				title: {
					display: true,
					text: 'Ratio of Anemic Women Given 100 IFA Tablets',
					fontFamily: "'Montserrat', sans-serif",
					fontSize: 16,
					fontColor: 'black'

				},
				tooltips: {
					mode: 'point',
					intersect: true,
				},
				hover: {
					mode: 'nearest',
					intersect: false
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Type of Facility',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 14
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Ratio',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 14
						}
					}]
				}
			}
		};
		myBar = new Chart(ctx4, config4)
	}
};
xhttp4.open("GET",'json/ifaDispRatio.json',true);
xhttp4.send();



// regression

var xhttp5 = new XMLHttpRequest();
xhttp5.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
		ppCheck = JSON.parse(xhttp5.responseText)
		console.log(ppCheck)
		var ctx5 = document.getElementById("myChart5");
		var config5 = {
			type: 'scatter',
			data: {
				labels: '',
				datasets: [{
					label: "Each point represents a facility",
					data: ppCheck,
					backgroundColor: 'rgb(75, 192, 192)'
				}]
			},
			options: {
				maintainAspectRatio: false,
				responsive: true,
				title: {
					display: true,
					text: 'Child Mortality versus Extent of Post-Partum Checkups',
					fontFamily: "'Montserrat', sans-serif",
					fontSize: 16,
					fontColor: 'black'

				},
				tooltips: {
					mode: 'point',
					intersect: true,
				},
				hover: {
					mode: 'nearest',
					intersect: false
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Women Receiving PP Checkups / Total ANC-Registered Women',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 12
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Child Mortality - Deaths per Live Birth',
							fontStyle: "'Montserrat',sans-serif",
							fontSize: 12
						}
					}]
				}
			}
		};
		myScatter = new Chart(ctx5, config5)
	}
};
xhttp5.open("GET",'json/ppcheckChart.json',true);
xhttp5.send();












