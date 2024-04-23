#!/usr/bin/node
// Displays the status code of a GET request.
const request = require('request');
const url = process.argv[2];

request(url, (err, response, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(response);
  }
});

/*
const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    console.log("code:", response.status);
  })
  .catch(error => {
    console.error("Error:", error.message);
  });
*/
