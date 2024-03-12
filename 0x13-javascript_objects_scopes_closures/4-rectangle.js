#!/usr/bin/node

// Defines a Rectangle class

class Rectangle {
  constructor (width, height) {
    // we don't want invalid data here
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  /**
   * Prints the rectangle using the character 'X'
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  /**
   * Exchanges the width and the height of the rectangle
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * Multiplies the width and the height of the rectangle by 2
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
