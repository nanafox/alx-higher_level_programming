#!/usr/bin/node

// This gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(path, response.body, (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
