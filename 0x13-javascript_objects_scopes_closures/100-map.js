#!/usr/bin/node

// Imports an array and computes a new array with each value equal to the
// original value multiplied by the index in the array.

const list = require('./100-data').list;
const newList = list.map((elem, index) => elem * index);

console.log(list);
console.log(newList);
