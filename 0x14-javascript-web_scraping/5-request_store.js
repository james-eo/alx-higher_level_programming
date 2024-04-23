#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

if (!url || !file) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

request.get({ url, encoding: 'utf8' }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);

    // Write to file
    fs.writeFile(file, body, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
