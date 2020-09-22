#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  let i;
  let j = list.length - 1;

  for (i = 0; i < (list.length / 2); i++, j--) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
