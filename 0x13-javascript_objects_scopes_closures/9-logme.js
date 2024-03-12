#!/usr/bin/node

/**
 * Logs an item to the console.
 * @param {any} item The item to log.
 */
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(`${this.count++}: ${item}`);
};
