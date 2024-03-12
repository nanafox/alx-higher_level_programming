#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Defines a Square class that inherits from Rectangle
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
