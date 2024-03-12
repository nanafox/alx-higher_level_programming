#!/usr/bin/node

// This script concatenates the content of two files.

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Incorrect number of arguments');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

const content = content1 + content2;

fs.writeFileSync(file3, content);
