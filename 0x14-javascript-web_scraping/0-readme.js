#!/usr/bin/node

// This script reads from a file and displays the contents on standard output.

const fs = require('fs');
const path = require('path');

function readFromFile () {
  if (process.argv.length !== 3) {
    console.error(`Usage: ${path.basename(process.argv[1])} <filename>`);
    return 1;
  }

  const filename = process.argv[2];
  fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

readFromFile();
