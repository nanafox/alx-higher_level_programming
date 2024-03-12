#!/usr/bin/node

/**
 * This script imports a dictionary of occurrences by user id and computes a
 * dictionary of user ids by occurrence.
 *
 * In order words, it computes a new dictionary with the values as keys and
 * the keys as values.
 */

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}

console.log(newDict);
