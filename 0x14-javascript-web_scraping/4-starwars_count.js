#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles”
// is present. This character has the ID 18.

const request = require('request');
const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(response.body).results;

    const count = results.reduce((count, film) => {
      if (film.characters.includes(wedgeAntilles)) {
        count++;
      }
      return count;
    }, 0);

    console.log(count);
  }
});
