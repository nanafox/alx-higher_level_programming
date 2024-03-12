#!/usr/bin/node

const initialSquare = require('./5-square');

/**
 * Defines a Square class that inherits from Square (5-square.js)
 */
class Square extends initialSquare {
  /**
   * Prints the Square using the character 'X' by default.
   * @param {string} char The character to print the square with.
   */
  charPrint (char) {
    if (char === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
