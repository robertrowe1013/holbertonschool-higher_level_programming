#!/usr/bin/node
let ultimate;
let penultimate;
let i = 4;
if (process.argv[2] === undefined) {
  penultimate = 0;
} else {
  if (process.argv[3] === undefined) {
    penultimate = 0;
  } else {
    if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
      ultimate = parseInt(process.argv[2]);
      penultimate = parseInt(process.argv[3]);
    } else {
      ultimate = parseInt(process.argv[3]);
      penultimate = parseInt(process.argv[2]);
    }
  }
}
while (process.argv[i] !== undefined) {
  if (parseInt(process.argv[i]) > penultimate) {
    if (parseInt(process.argv[i]) > ultimate) {
      penultimate = ultimate;
      ultimate = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) < ultimate) {
      penultimate = parseInt(process.argv[i]);
    }
  }
  i++;
}
console.log(penultimate);
