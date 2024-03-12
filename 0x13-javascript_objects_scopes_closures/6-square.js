#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Defines a Square class that inherits from Rectangle
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  /**
   * Prints the Square using the character 'X' by default.
   * @param {string} char The character to print the square with.
   */
  charPrint (char) {
    if (char === undefined) {
      char = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
