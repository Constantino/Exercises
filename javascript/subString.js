var string = "Languages: java, python, php, ruby, c++."
var start = string.indexOf(':');
var end = string.indexOf('.', start+1);
var listStr = string.substring(start+1,end);

console.log('original string: '+string);
console.log('substring: '+listStr);
var x = listStr.split(',');

console.log('substring split commas: ',x);