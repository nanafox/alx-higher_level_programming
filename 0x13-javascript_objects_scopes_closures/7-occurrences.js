#!/usr/bin/node

/**
 * Returns the number of occurrences of `searchElement` in `list`
 * @param {Array} list The list to search in
 * @param {any} searchElement The element to search for
 * @returns The number of occurrences of `searchElement` in `list`
 */
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
