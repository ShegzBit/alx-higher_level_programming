#!/usr/bin/node

console.log(process.argv);
console.log(process.argv.length);
if (process.argv.length <= 2) {
	console.log("No argument");
} else {
	console.log("Argument found");
}
