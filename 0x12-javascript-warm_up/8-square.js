#!/usr/bin/node

// Prints a square using 'X' using `console.log()` only.

const size = parseInt(process.argv[2], 10);

if (!size) console.log('Missing size');
else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
