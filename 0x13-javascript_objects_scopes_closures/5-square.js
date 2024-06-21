#!/usr/bin/node

/* Define a Square class as child of Rectangle */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square