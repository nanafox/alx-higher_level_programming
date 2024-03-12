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
}

module.exports = Rectangle;
