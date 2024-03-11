#!/usr/bin/node
'use strict';

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = () => {
  myObject.value++;
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
