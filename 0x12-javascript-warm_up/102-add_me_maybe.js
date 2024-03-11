#!/usr/bin/node
'use strict';

// Increments a value and calls a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
