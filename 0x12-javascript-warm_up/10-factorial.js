#!/usr/bin/node
let result;
const myVar = parseInt(process.argv[2]);
function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
if (isNaN(myVar)) {
  result = 1;
} else {
  result = factorial(myVar);
}
console.log(result);
