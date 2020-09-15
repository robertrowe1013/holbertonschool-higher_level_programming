#!/usr/bin/node
let myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  myVar = 'Not a number';
}
console.log(myVar);
