#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let i;
    let j;
    let row;
    if (!c) {
      c = 'X';
    }
    for (i = 0; i < this.size; i++) {
      row = '';
      for (j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
