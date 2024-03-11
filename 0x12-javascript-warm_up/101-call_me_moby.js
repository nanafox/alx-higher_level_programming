#!/usr/bin/node

// Calls a function `x` number of times

exports.callMeMoby = function (x, thefunction) {
  for (let i = 0; i < x; i++) {
    thefunction();
  }
};
