#!/usr/bin/node
const Rectangle = require('./4-rectangle');
let column;
let row;

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
}
module.exports = Square;
