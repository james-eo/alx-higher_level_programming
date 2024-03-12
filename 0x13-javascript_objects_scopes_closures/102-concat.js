#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const fileA = fs.readFileSync(sourceFile1, 'utf8');
const fileB = fs.readFileSync(sourceFile2, 'utf8');

fs.writeFileSync(destinationFile, fileA + fileB);
