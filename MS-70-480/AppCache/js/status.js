window.onload = function (){
	console.log("in onload");
	var appCache = window.applicationCache;
	appCache.oncached = function (e){ alert("cache successfully downloaded");};
	appCache.onupdateready = function (e) { appCache.swapCache(); };

}