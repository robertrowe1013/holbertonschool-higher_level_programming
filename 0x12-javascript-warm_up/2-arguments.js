#!/usr/bin/node
let myVar;
if (process.argv[2] === undefined) {
  myVar = 'No argument';
} else {
  if (process.argv[3] === undefined) {
    myVar = 'Argument found';
  } else {
    myVar = 'Arguments found';
  }
}
console.log(myVar);
