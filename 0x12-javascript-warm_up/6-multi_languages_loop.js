#!/usr/bin/node
let myVar;
let startPoint = 0;
let stopPoint;
if (process.argv[2] === undefined) {
  myVar = 'Missing number of occurrences';
  stopPoint = 1;
} else {
  myVar = 'C is fun';
  stopPoint = process.argv[2];
}
while (startPoint < stopPoint) {
  console.log(myVar);
  startPoint++;
}
