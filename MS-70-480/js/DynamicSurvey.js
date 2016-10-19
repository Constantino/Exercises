window.onload = function (){

	toggleEverything();
}

function toggleEverything(){

	var questions = document.querySelectorAll("[id^=Question]");
	questions.forEach(
		function (item){
			if (item !== questions[0]) {
				item.style.visibility = "collapse";	
			}

		}
		);
}

var myDict = {"Question1":1,"Question2":2,"Question3":3,
				"Question4":4,"Question5":5,"Question6":6,
				"Question7":7,"Question8":8,"Question9":9,"Question10":10};

function getNumber(prevQ, value){

	switch(myDict[prevQ]){
		
		case 1:
			if (value === "on") {
				return "Question2";
			} else {
				return "Question3";
			}
			
		case 2:

			if (value === "on") {
				return "Question4";
			} else {
				return "Question5";
			}
			
		case 3:
			return "Question6";
			
		case 4:
			return "Question10";
			
		case 5:
			return "Question10";
			
		case 6:
			if (value === "on") {
				return "Question7";
			} else {
				return "Question8";
			}
			
		case 7:
			return "Question9";
			
		case 8:
			return "Question9";
			
		case 9:
			return "Question10";
			
		default: return null;
	}
}

function nextQuestion(question,value){

	var next = getNumber(question,value);
	
	if (next !== null) {
		document.querySelector("[id="+next+"]").style.visibility = "visible";	
	}

}