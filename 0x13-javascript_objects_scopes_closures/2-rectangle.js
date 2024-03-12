#!/usr/bin/node

// Defines a Rectangle class

class Rectangle {
  constructor (width, height) {
    // we don't want invalid data here
    if ((width > 0 && height > 0)) {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
