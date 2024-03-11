#!/usr/bin/node

// Prints the sum of two integers

function add (a, b) {
  return +a + +b;
}

console.log(add(process.argv[2], process.argv[3]));
