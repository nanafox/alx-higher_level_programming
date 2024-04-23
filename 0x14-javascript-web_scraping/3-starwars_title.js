#!/usr/bin/node

// This script uses the Star Wars and retrieves the title of given film id

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];

request(`${url}/${id}`, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(response.body).title);
  }
});
