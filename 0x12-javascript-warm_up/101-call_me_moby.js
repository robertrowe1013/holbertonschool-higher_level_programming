#!/usr/bin/node
let i;
exports.callMeMoby = function (number, theFunction) {
  for (i = 0; i < number; i++) {
    theFunction();
  }
};
