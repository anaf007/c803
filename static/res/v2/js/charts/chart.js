$(function() {
 google.charts.load('upcoming', {'packages':['geochart']});
  google.charts.setOnLoadCallback(drawRegionsMap);
  function drawRegionsMap() {
	"use strict";
    var data = google.visualization.arrayToDataTable([
	  ['Country', 'Visitors'],
	  ['Germany', 200],
	  ['America', 600],
	  ['Brazil', 100],
	  ['Canada', 400],
	  ['France', 190],
	  ['RU', 210]
	]);
	var options = {};
	var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
	chart.draw(data, options);
	
  }


	$(window).load(function(){ 		
		// Initialize rickshaw chart
		var graph;

		var seriesData = [ [], []];
		var random = new Rickshaw.Fixtures.RandomData(50);

		for (var i = 0; i < 50; i++) {
			random.addData(seriesData);
		}

		graph = new Rickshaw.Graph( {
			element: document.querySelector("#realtime-rickshaw"),
			renderer: 'area',
			height: 200,
			series: [{
				name: 'Series 1',
				color: '#9675ce',
				data: seriesData[0]
			}, {
				name: 'Series 2',
				color: '#d4bdfa',
				data: seriesData[1]
			}]
		});

		/*var hoverDetail = new Rickshaw.Graph.HoverDetail( {
			graph: graph,
		});*/

		graph.render();

		setInterval( function() {
			random.removeData(seriesData);
			random.addData(seriesData);
			graph.update();

		},1000);
		//* Initialize rickshaw chart 

	});
    
});