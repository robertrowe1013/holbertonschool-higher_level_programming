#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
let key;
let newKey;
for (key in dict) {
  if (dict[key] in newDict) continue;
  else newDict[dict[key]] = [];
}
for (key in dict) {
  newKey = dict[key];
  newDict[newKey].push(key);
}
console.log(newDict);
