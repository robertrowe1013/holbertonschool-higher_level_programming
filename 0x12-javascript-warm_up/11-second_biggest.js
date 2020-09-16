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
    if (process.argv[2] > process.argv[3]) {
      ultimate = process.argv[2];
      penultimate = process.argv[3];
    } else {
      ultimate = process.argv[3];
      penultimate = process.argv[2];
    }
  }
}
while (process.argv[i] !== undefined) {
  if (process.argv[i] > ultimate) {
    penultimate = ultimate;
    ultimate = process.argv[i];
  }
  i++;
}
console.log(penultimate);
