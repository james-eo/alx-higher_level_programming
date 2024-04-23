#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (err, response, data) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(data).results;
    const count = films.reduce((total, film) => {
      if (film.characters.some(characterUrl => characterUrl.includes(characterId))) {
        return total + 1;
      }
      return total;
    }, 0);
    console.log(count);
  }
});
