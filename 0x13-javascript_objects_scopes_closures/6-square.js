#!/usr/bin/node
let column;
let row;

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (column = 0; column < this.height; column++) {
        for (row = 0; row < this.width; row++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
