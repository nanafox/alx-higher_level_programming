#!/usr/bin/node

// Prints "C is fun" `n` number of times

const n = parseInt(process.argv[2]);

if (!n) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
