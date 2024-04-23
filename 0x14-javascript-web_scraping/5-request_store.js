#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Write to file
    fs.writeFile(file, body, { flag: 'w' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
