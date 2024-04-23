#!/usr/bin/node

const request = require('request');
const id  = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:' + id;

request.get(url, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
	  console.log(JSON.parse(data));
  }
});

/*
const axios = require('axios');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

axios.get(url)
  .then(response => {
    const { title } = response.data;
    console.log(title);
  })
  .catch(error => {
    console.error("Error:", error.message);
  });
  */
