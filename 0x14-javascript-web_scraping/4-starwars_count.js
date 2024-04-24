#!/usr/bin/node

// This script prints the number of movies where the character “Wedge Antilles”
// is present. This character has the ID 18.

const request = require('request');
const wedgeAntilles = 'people/18/';
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(response.body).results;

    const count = results.filter((film) => {
      return film.characters.find((character) => character.includes(wedgeAntilles));
    });

    console.log(count.length);
  }
});
