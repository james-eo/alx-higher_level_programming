#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const charList = JSON.parse(body).characters;
  charList.forEach(character => {
    request.get(character, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
