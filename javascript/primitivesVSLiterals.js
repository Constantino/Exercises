var str1 = String("myString");
var num1 = Number(5.67);
var bool1 = Boolean(true);

if (str1 === "myString") {
	console.log('equal');
}

if (num1 === 5.67) {
	console.log('equal');
};

if (bool1 === true) {
	console.log('equal');
};

var str2 = new String("myString");
var num2 = new Number(5.67);
var bool2 = new Boolean(true);


if (str2 === "myString") {
	console.log('equal');
}else{
	console.log('not equal');
}

if (num2 === 5.67) {
	console.log('equal');
}else{
	console.log('not equal');
}

if (bool2 === true) {
	console.log('equal');
}else{
	console.log('not equal');
}
