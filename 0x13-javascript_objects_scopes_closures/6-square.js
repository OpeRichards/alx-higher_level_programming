#!/usr/bin/node

/* Define a class Square is a child of Square of 5-square.js */
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
