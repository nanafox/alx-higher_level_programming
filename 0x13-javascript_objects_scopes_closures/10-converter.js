#!/usr/bin/node

/**
 * Converts a number to a specified base
 * @param {number} base The base to convert to
 * @returns The function to convert a number to the base
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
