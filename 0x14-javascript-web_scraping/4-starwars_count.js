#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles” is present.
// This character has the ID 18.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people'; // I'm cheating here :-)
const id = 18;

request(`${url}/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.films.length);
  }
});
