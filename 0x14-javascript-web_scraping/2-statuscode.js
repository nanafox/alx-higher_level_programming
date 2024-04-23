#!/usr/bin/node

// This script makes a request to the received URL and displays the status code

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else { console.log(`code: ${response.statusCode}`); }
});
