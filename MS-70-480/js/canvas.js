window.onload = function(){

	canvas = document.getElementById("myCanvas");
	context = canvas.getContext("2d");
	
}

function draw(x,y){
	
	context.beginPath();
	context.moveTo(x,canvas.height-y);
	context.lineTo(x, canvas.height);
	context.stroke();

}

function getData(){

	var data = document.getElementById("data").value;
	var points = data.split("\n");

	points.forEach(
			function (item){
				var point = item.split(",");
				draw(point[0], point[1]);
				
			}
		);

}