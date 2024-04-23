#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(data).results;
    const match = films.filter((film) => film.characters.includes(character));
    console.log(`${match.length}`);
  }
});
