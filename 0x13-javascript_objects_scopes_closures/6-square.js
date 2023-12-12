#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    let i;
    let j;
    let row;
    if (!c) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      row = '';
      for (j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
