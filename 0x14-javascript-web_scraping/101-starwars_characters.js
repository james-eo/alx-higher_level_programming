#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  const fetchCharacterNames = (urls, index) => {
    if (index === urls.length) {
      return;
    }

    request.get(urls[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);

      fetchCharacterNames(urls, index + 1);
    });
  };

  fetchCharacterNames(characters, 0); // Start fetching characters from index 0
});
