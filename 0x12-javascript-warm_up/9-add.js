#!/usr/bin/node
const var1 = parseInt(process.argv[2]);
const var2 = parseInt(process.argv[3]);
let result;
function add (a, b) {
  return a + b;
}
if (isNaN(var1) || isNaN(var2)) {
  console.log('NaN');
} else {
  result = add(var1, var2);
  console.log(result);
}
