#!/usr/bin/node

// This script writes the contents received on the CLI to a file.

const fs = require('fs');
const path = require('path');

function writeToFile () {
  if (process.argv.length !== 4) {
    console.error(`Usage: ${path.basename(process.argv[1])} <filename> <data>`);
    return;
  }

  const filename = process.argv[2];
  const data = process.argv[3];
  fs.writeFile(filename, data, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

writeToFile();
