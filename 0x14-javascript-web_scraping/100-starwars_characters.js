#!/usr/bin/node

// This script prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(response.body).characters;
    characters.forEach((character) => {
      request(character, function (error, response) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(response.body).name);
        }
      });
    });
  }
});
