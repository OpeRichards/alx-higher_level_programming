#!/usr/bin/node

/* Define an empty Rectangle class */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /* Instance method to print the rectangle using 'X' */
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  /* Instance method to exchange the sides of the rectangle */
  rotate () {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  /* Instance method to double the sides of the rectangle */
  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}
module.exports = Rectangle;
