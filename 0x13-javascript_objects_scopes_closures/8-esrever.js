#!/usr/bin/node

/**
 * Reverses a list.
 * @param {Array} list The list to reverse.
 * @returns The reversed list.
 */
exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
