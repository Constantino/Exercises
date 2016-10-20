window.onload = function (){

	
	console.log(sessionStorage);

	LoadFromStorage();

	document.getElementById("btnAdd").onclick = function (){
		console.log("in Add");
		var key = document.getElementById("storageKey").value;
		var value = document.getElementById("storageValue").value;

		sessionStorage.setItem(key,value);

		resetStorageDiv();
		LoadFromStorage();
	};

	document.getElementById("btnRem").onclick  = function (){
		console.log("in Rem");
		var key = document.getElementById("storageKey").value;
		
		sessionStorage.removeItem(key);	

		console.log(key);
		
		resetStorageDiv();
		LoadFromStorage();
	};


	document.getElementById("btnClear").onclick = function (){
		console.log("in Clear");
		var key = document.getElementById("storageKey").value;
		var value = document.getElementById("storageValue").value;

		sessionStorage.clear();	
		resetStorageDiv();
		LoadFromStorage();
	};

}

function resetStorageDiv(){
	document.getElementById("myDivStorage").innerHTML = "";
}

function LoadFromStorage(){

	var storageDiv = document.getElementById("myDivStorage");
	
	storageDiv.innerHTML = "<p>Current storage contents:</p><br>";
	//storageDiv.innerHTML = sessionStorage.getItem("SithLord");
	for (var i = 0; i < sessionStorage.length; i++) {
		storageDiv.innerHTML += sessionStorage.key(i) + " - " +sessionStorage.getItem(sessionStorage.key(i)) +"<br>";
	}

}