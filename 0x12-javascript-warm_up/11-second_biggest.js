#!/usr/bin/node
'use strict';

// Searches for the second biggest integer in the list of CLI arguments

function getSecondLargest (array) {
  return (array.length > 1) ? array.sort((a, b) => b - a)[1] : 0;
}

function convertToIntegerArray (array) {
  return array.map((num) => parseInt(num));
}

const array = convertToIntegerArray(process.argv.slice(2));

console.log(getSecondLargest(array));
