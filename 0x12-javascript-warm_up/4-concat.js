#!/usr/bin/node
let var1;
let var2;
if (process.argv[2] === undefined) {
  var1 = 'undefined';
} else {
  var1 = process.argv[2];
}
if (process.argv[3] === undefined) {
  var2 = 'undefined';
} else {
  var2 = process.argv[3];
}
console.log(var1, 'is', var2);
