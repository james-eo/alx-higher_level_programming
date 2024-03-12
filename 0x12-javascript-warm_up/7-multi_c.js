#!/usr/bin/node

const args = process.argv[2];
const arg = parseInt(args);

if (!isNaN(arg)) {
  let i = 0;
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

/*
const args = process.argv[2];
const arg = parseInt(args);

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
*/
