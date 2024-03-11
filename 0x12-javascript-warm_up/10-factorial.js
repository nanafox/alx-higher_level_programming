#!/usr/bin/node
'use strict';

// Computes the factorial of a given number

function factorial (n) {
  if (!n) {
    return 1;
  }

  return n * factorial(n - 1);
}

const n = parseInt(process.argv[2], 10);
console.log(factorial(n));
