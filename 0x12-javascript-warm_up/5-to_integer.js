#!/usr/bin/node
let myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
}
console.log('My number:', myVar);
