#!/usr/bin/node
let myVar = 'X';
let i;
let i2 = 1;
let stopPoint;
if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  myVar = 'Missing size';
  stopPoint = 1;
} else {
  stopPoint = process.argv[2];
}
while (i2 < stopPoint) {
  myVar = myVar.concat('X');
  i2++;
}
for (i = 0; i < stopPoint; i++) {
  console.log(myVar);
}
