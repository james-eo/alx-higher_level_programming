#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(data);
    console.log(movie.title);
  }
});
