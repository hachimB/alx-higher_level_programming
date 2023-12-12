#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    let row;
    for (i = 0; i < this.height; i++) {
      row = '';
      for (j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
